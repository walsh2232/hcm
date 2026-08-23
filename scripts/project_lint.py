#!/usr/bin/env python3
"""Validate the project operating system in .project/.

Enforces the traceability rules described in .project/workflow.md that can be
checked mechanically:

  * identifier format and uniqueness
  * Kanban board <-> backlog consistency
  * reference integrity for DOC / GAP / ASM / ADR identifiers
  * assumption expiry
  * ADR structure, status, and source citation
  * WIP limits, read from the workflow definition rather than hardcoded
  * relative Markdown links resolve

Exit code 0 when clean, 1 when any error is found. Standard library only.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROJECT = ROOT / ".project"

KANBAN = PROJECT / "kanban.md"
BACKLOG = PROJECT / "backlog.md"
WORKFLOW = PROJECT / "workflow.md"
GAPS = PROJECT / "docs" / "gaps.md"
REGISTRY = PROJECT / "docs" / "source-registry.md"
ADR_DIR = PROJECT / "adr"

# The 000 suffix is reserved across every identifier class for documentation
# examples (see .project/README.md) and is never resolved as a reference.
RESERVED = {"000", "0000"}

ROLES = {"PO", "BA", "SA", "DEV", "QA", "DOC"}

ADR_SECTIONS = ["## Status", "## Context", "## Decision", "## Consequences", "## Sources"]
ADR_STATUS = re.compile(
    r"^(Proposed|Accepted|Provisional|Under review|Superseded by ADR-\d{4}|Rejected)\b"
)
CITATION = re.compile(r"DOC-\d{3}|NONE \(GAP-\d{3}\)|N/A")

BOARD_CARD = re.compile(r"^- (HCM-\d{3}) \[([A-Z]{2,3})\]")
BOARD_STATE = re.compile(r"^## (Backlog|Ready|In Progress|In Review|Done)\s*$")


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, where: str, msg: str) -> None:
        self.errors.append(f"{where}: {msg}")

    def warn(self, where: str, msg: str) -> None:
        self.warnings.append(f"{where}: {msg}")


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def read(path: Path, rep: Report) -> str:
    if not path.exists():
        rep.error(rel(path), "required file is missing")
        return ""
    return path.read_text(encoding="utf-8")


# --------------------------------------------------------------------------- #
# Board and backlog
# --------------------------------------------------------------------------- #

def parse_board(text: str) -> dict[str, list[tuple[str, str]]]:
    """Return {state: [(card_id, role), ...]} for cards written as board rows."""
    board: dict[str, list[tuple[str, str]]] = {}
    state = None
    for line in text.splitlines():
        heading = BOARD_STATE.match(line)
        if heading:
            state = heading.group(1)
            board.setdefault(state, [])
            continue
        if state is None:
            continue
        card = BOARD_CARD.match(line)
        if card:
            board[state].append((card.group(1), card.group(2)))
    return board


def parse_wip_limits(text: str, rep: Report) -> dict[str, object]:
    """Read WIP limits from the state table in workflow.md."""
    limits: dict[str, object] = {}
    for line in text.splitlines():
        m = re.match(r"^\|\s*\d+\s*\|\s*\*\*(.+?)\*\*\s*\|.*\|\s*([^|]+?)\s*\|\s*$", line)
        if not m:
            continue
        state, raw = m.group(1).strip(), m.group(2).strip()
        if raw in {"—", "-", ""}:
            limits[state] = None
        elif raw.endswith("per role"):
            limits[state] = ("per_role", int(raw.split()[0]))
        elif raw.isdigit():
            limits[state] = int(raw)
        else:
            rep.warn(rel(WORKFLOW), f"unrecognised WIP limit {raw!r} for state {state!r}")
    if not limits:
        rep.error(rel(WORKFLOW), "could not read the WIP limit table")
    return limits


def check_board(rep: Report, board: dict, backlog_text: str, limits: dict) -> None:
    where = rel(KANBAN)
    seen: dict[str, str] = {}
    for state, cards in board.items():
        for card_id, role in cards:
            if card_id in seen:
                rep.error(where, f"{card_id} appears in both {seen[card_id]} and {state}")
            seen[card_id] = state
            if role not in ROLES:
                rep.error(where, f"{card_id} has unknown role tag [{role}]")

    headings = set(re.findall(r"^### (HCM-\d{3})", backlog_text, re.M))
    dupes = [c for c in re.findall(r"^### (HCM-\d{3})", backlog_text, re.M)
             if list(re.findall(r"^### (HCM-\d{3})", backlog_text, re.M)).count(c) > 1]
    for card_id in sorted(set(dupes)):
        rep.error(rel(BACKLOG), f"{card_id} has more than one card body")

    for card_id in sorted(set(seen) - headings):
        rep.error(where, f"{card_id} is on the board but has no card body in backlog.md")
    for card_id in sorted(headings - set(seen)):
        rep.error(rel(BACKLOG), f"{card_id} has a card body but is not on the board")

    for state, cards in board.items():
        limit = limits.get(state)
        if limit is None:
            continue
        if isinstance(limit, tuple):
            per_role: dict[str, int] = {}
            for _, role in cards:
                per_role[role] = per_role.get(role, 0) + 1
            for role, count in sorted(per_role.items()):
                if count > limit[1]:
                    rep.error(where, f"WIP limit breached in {state}: "
                                     f"{count} cards for [{role}], limit {limit[1]} per role")
        elif len(cards) > limit:
            rep.error(where, f"WIP limit breached in {state}: {len(cards)} cards, limit {limit}")


# --------------------------------------------------------------------------- #
# Gaps and assumptions
# --------------------------------------------------------------------------- #

def parse_gaps(text: str) -> tuple[set[str], dict[str, dict]]:
    gaps = set(re.findall(r"^### (GAP-\d{3})", text, re.M))
    assumptions: dict[str, dict] = {}
    blocks = re.split(r"^### (ASM-\d{3})", text, flags=re.M)
    for i in range(1, len(blocks), 2):
        asm_id, body = blocks[i], blocks[i + 1]
        header = body.splitlines()[0] if body.splitlines() else ""
        expires = re.search(r"^-\s*Expires:\s*(\d{4}-\d{2}-\d{2})", body, re.M)
        owner = re.search(r"^-\s*Owner:\s*(\S.*)$", body, re.M)
        assumptions[asm_id] = {
            "open": "Open" in header,
            "reserved": "Reserved" in header,
            "expires": expires.group(1) if expires else None,
            "owner": owner.group(1).strip() if owner else None,
            "cost": bool(re.search(r"^-\s*If wrong:", body, re.M)),
        }
    return gaps, assumptions


def check_assumptions(rep: Report, assumptions: dict, today: dt.date, allow_expired: bool) -> None:
    where = rel(GAPS)
    for asm_id, a in sorted(assumptions.items()):
        if a["reserved"] or not a["open"]:
            continue
        if not a["owner"]:
            rep.error(where, f"{asm_id} is open but names no owner")
        if not a["cost"]:
            rep.error(where, f"{asm_id} is open but does not state the cost of being wrong "
                             "(required by ADR-0005)")
        if not a["expires"]:
            rep.error(where, f"{asm_id} is open but has no expiry date")
            continue
        expiry = dt.date.fromisoformat(a["expires"])
        if expiry < today:
            msg = (f"{asm_id} expired on {a['expires']}. Resolve it with a tier A/B citation, "
                   "or renew it with a new expiry and a stated reason (ADR-0005).")
            if allow_expired:
                rep.warn(where, msg + " [suppressed by --allow-expired]")
            else:
                rep.error(where, msg)
        elif (expiry - today).days <= 14:
            rep.warn(where, f"{asm_id} expires on {a['expires']} ({(expiry - today).days}d)")


# --------------------------------------------------------------------------- #
# Reference integrity
# --------------------------------------------------------------------------- #

def parse_registry(text: str) -> set[str]:
    return set(re.findall(r"^\|\s*(DOC-\d{3})\s*\|", text, re.M))


def check_references(rep: Report, docs: set[str], gaps: set[str],
                     assumptions: dict, adrs: set[str]) -> None:
    known = {"DOC": docs, "GAP": gaps, "ASM": set(assumptions), "ADR": adrs}
    pattern = re.compile(r"\b(DOC|GAP|ASM)-(\d{3})\b|\b(ADR)-(\d{4})\b")

    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts:
            continue
        # Templates carry ### / #### placeholders, not real identifiers.
        if path.parent.name == "templates":
            continue
        text = path.read_text(encoding="utf-8")
        unresolved: dict[str, set[str]] = {}
        for match in pattern.finditer(text):
            kind = match.group(1) or match.group(3)
            number = match.group(2) or match.group(4)
            if number in RESERVED:
                continue
            ident = f"{kind}-{number}"
            if ident not in known[kind]:
                unresolved.setdefault(kind, set()).add(ident)
        for kind, idents in sorted(unresolved.items()):
            for ident in sorted(idents):
                rep.error(rel(path), f"cites {ident}, which is not defined "
                                     f"({'source-registry.md' if kind == 'DOC' else 'gaps.md' if kind in ('GAP', 'ASM') else '.project/adr/'})")


# --------------------------------------------------------------------------- #
# Relative links
# --------------------------------------------------------------------------- #

LINK = re.compile(r"\]\(([^)\s]+)\)")


def check_links(rep: Report) -> None:
    """Every relative Markdown link must resolve to a file that exists."""
    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts:
            continue
        for target in LINK.findall(path.read_text(encoding="utf-8")):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            resolved = (path.parent / target.split("#", 1)[0]).resolve()
            if not resolved.exists():
                rep.error(rel(path), f"broken relative link: {target}")


# --------------------------------------------------------------------------- #
# ADRs
# --------------------------------------------------------------------------- #

def check_adrs(rep: Report) -> set[str]:
    known: set[str] = set()
    if not ADR_DIR.exists():
        rep.error(rel(ADR_DIR), "ADR directory is missing")
        return known

    for path in sorted(ADR_DIR.glob("*.md")):
        if path.name == "README.md":
            continue
        where = rel(path)
        m = re.match(r"^(ADR-\d{4})-[a-z0-9-]+\.md$", path.name)
        if not m:
            rep.error(where, "filename must be ADR-####-kebab-case-title.md")
            continue
        adr_id = m.group(1)
        if adr_id in known:
            rep.error(where, f"{adr_id} is already used by another file")
        known.add(adr_id)

        text = path.read_text(encoding="utf-8")
        title = text.splitlines()[0] if text.splitlines() else ""
        if not title.startswith(f"# {adr_id} "):
            rep.error(where, f"first heading must start '# {adr_id} '")

        for section in ADR_SECTIONS:
            if not re.search(rf"^{re.escape(section)}\s*$", text, re.M):
                rep.error(where, f"missing required section '{section}'")

        status = section_body(text, "## Status")
        if status and not ADR_STATUS.match(status.strip().splitlines()[0]):
            rep.error(where, "status must be one of Proposed / Accepted / Provisional / "
                             "Under review / Superseded by ADR-#### / Rejected")
        if status and status.strip().startswith("Provisional") and "ASM-" not in status:
            rep.error(where, "a Provisional ADR must name the assumption it rests on (ADR-0005)")

        sources = section_body(text, "## Sources")
        if sources is not None and not CITATION.search(sources):
            rep.error(where, "Sources must cite DOC-### §location, NONE (GAP-###), "
                             "or N/A — internal process decision")

    index = (ADR_DIR / "README.md")
    if index.exists():
        listed = set(re.findall(r"\[(ADR-\d{4})\]", index.read_text(encoding="utf-8")))
        for adr_id in sorted(known - listed):
            rep.error(rel(index), f"{adr_id} exists but is not in the index")
        for adr_id in sorted(listed - known):
            rep.error(rel(index), f"{adr_id} is indexed but has no file")
    return known


def section_body(text: str, heading: str) -> str | None:
    m = re.search(rf"^{re.escape(heading)}\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
    return m.group(1) if m else None


# --------------------------------------------------------------------------- #

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--quiet", action="store_true", help="print errors only")
    parser.add_argument("--allow-expired", action="store_true",
                        help="downgrade expired assumptions to warnings (use deliberately, "
                             "and say so in the pull request)")
    parser.add_argument("--today", metavar="YYYY-MM-DD",
                        help="override today's date, for testing")
    args = parser.parse_args()

    today = dt.date.fromisoformat(args.today) if args.today else dt.date.today()
    rep = Report()

    kanban_text = read(KANBAN, rep)
    backlog_text = read(BACKLOG, rep)
    workflow_text = read(WORKFLOW, rep)
    gaps_text = read(GAPS, rep)
    registry_text = read(REGISTRY, rep)

    adrs = check_adrs(rep)
    gaps, assumptions = parse_gaps(gaps_text)
    docs = parse_registry(registry_text)

    if kanban_text and backlog_text and workflow_text:
        limits = parse_wip_limits(workflow_text, rep)
        check_board(rep, parse_board(kanban_text), backlog_text, limits)

    check_assumptions(rep, assumptions, today, args.allow_expired)
    check_references(rep, docs, gaps, assumptions, adrs)
    check_links(rep)

    if rep.warnings and not args.quiet:
        for w in rep.warnings:
            print(f"warning  {w}")
    for e in rep.errors:
        print(f"error    {e}", file=sys.stderr)

    if rep.errors:
        print(f"\nproject lint FAILED — {len(rep.errors)} error(s), "
              f"{len(rep.warnings)} warning(s)", file=sys.stderr)
        return 1
    if not args.quiet:
        real_docs = {d for d in docs if d[-3:] not in RESERVED}
        real_asm = {a for a, v in assumptions.items() if not v["reserved"]}
        print(f"project lint passed — {len(adrs)} ADR(s), {len(real_docs)} registered source(s), "
              f"{len(gaps)} gap(s), {len(real_asm)} assumption(s), "
              f"{len(rep.warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
