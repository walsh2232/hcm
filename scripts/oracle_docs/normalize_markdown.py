#!/usr/bin/env python3
"""Conservatively normalize PDF-derived Markdown procedure formatting.

Input is a directory containing chapters/*.md. The tool does not paraphrase
source text, infer configuration, or rewrite identifiers. It repairs repeated
layout artefacts found in Oracle PDF text extraction.

Usage:
  python scripts/oracle_docs/normalize_markdown.py --root /path/to/local-wiki --check
  python scripts/oracle_docs/normalize_markdown.py --root /path/to/local-wiki --apply
"""
from __future__ import annotations
import argparse
import re
from pathlib import Path

NAV_BLOCK = re.compile(
    r"(?m)^(?P<intro>[ \t]*(?:\*\*\d{1,2}\.\*\*|\d{1,2}\.)[^\n]*?\bgo to:?)[ \t]*-?[ \t]*\n"
    r"(?:[ \t]*\n|[ \t]*-[ \t]*\n)*"
    r"(?P<off>Offering:[^\n]+?)[ \t]*-?[ \t]*\n"
    r"(?:[ \t]*\n|[ \t]*-[ \t]*\n)*"
    r"(?P<fa>Functional Area:[^\n]+?)[ \t]*-?[ \t]*\n"
    r"(?:[ \t]*\n|[ \t]*-[ \t]*\n)*"
    r"(?P<task>Task:[^\n]+)"
)
STEP_MARKER = re.compile(r"(?P<indent>[ \t]*)\*\*(?P<number>\d{1,2})\.\*\*[ \t]*")
ALPHA_MARKER = re.compile(r"(?P<indent>[ \t]*)\*\*(?P<letter>[a-z])\.\*\*[ \t]*", re.I)


def strip_trailing_separator(value: str) -> str:
    value = value.rstrip()
    if value.endswith(" -"):
        value = value[:-2].rstrip()
    return value


def normalize(text: str) -> tuple[str, dict[str, int]]:
    counts = {
        "setup_navigation_blocks": 0, "numbered_steps": 0,
        "alphabetic_substeps": 0, "orphan_list_separators_removed": 0,
        "scheduled_process_lists": 0, "scheduled_process_bullets": 0,
        "bold_space_before": 0, "bold_space_after": 0,
    }

    def nav_repl(m: re.Match[str]) -> str:
        counts["setup_navigation_blocks"] += 1
        intro = re.sub(r"\*\*(\d{1,2})\.\*\*", r"\1.", m.group("intro"))
        intro = re.sub(r"^([ \t]*\d{1,2}\.)(?=[A-Za-z])", r"\1 ", intro)
        intro = strip_trailing_separator(intro)
        items = [strip_trailing_separator(m.group(k)) for k in ("off", "fa", "task")]
        return intro.rstrip() + "\n    - " + items[0] + "\n    - " + items[1] + "\n    - " + items[2]

    text = NAV_BLOCK.sub(nav_repl, text)

    process_names = (
        "Load and Index Master Geography Hierarchy",
        "Load and Index Job Requisitions",
        "Load and Index Candidates",
        "Index Job Summary for Each Requisition",
        "Maintain Candidates and Job Requisitions for Search",
        "Index Candidate Attachments",
    )
    trigger = re.compile(
        r"^([ \t]*\d{1,2}\.\s+.*(?:run these scheduled processes|schedule the following processes|cancel these scheduled processes).*)$",
        re.I,
    )
    process_line = re.compile(
        r"^(?P<indent>[ \t]*)(?P<bullet>-[ \t]+)?\*\*(?P<name>"
        + "|".join(re.escape(n) for n in process_names)
        + r")\*\*(?P<tail>.*)$",
        re.I,
    )
    lines = text.splitlines()
    normalized_lines = []
    in_process_sequence = False
    for line in lines:
        trigger_match = trigger.match(line.strip())
        if trigger_match:
            counts["scheduled_process_lists"] += 1
            if normalized_lines and normalized_lines[-1].strip() and normalized_lines[-1].startswith("    - "):
                normalized_lines.append("")
            in_process_sequence = True
            cleaned = re.sub(r"[ \t]+-[ \t]*$", "", line.rstrip())
            normalized_lines.append(cleaned)
            continue
        if in_process_sequence and re.match(r"^[ \t]*\d{1,2}\.\s+", line):
            if normalized_lines and normalized_lines[-1].strip():
                normalized_lines.append("")
            in_process_sequence = False
        if in_process_sequence and line.strip() == "-":
            continue
        match = process_line.match(line)
        if in_process_sequence and match:
            counts["scheduled_process_bullets"] += 1
            indent = match.group("indent") if match.group("bullet") else (match.group("indent") + "    ")
            tail = re.sub(r"[ \t]*-[ \t]*$", "", match.group("tail").rstrip())
            normalized_lines.append(indent + "- **" + match.group("name") + "**" + tail)
            continue
        if in_process_sequence and line.startswith("**") and line.rstrip().endswith("-"):
            line = re.sub(r"[ \t]+-[ \t]*$", "", line.rstrip())
        normalized_lines.append(line)
    text = "\n".join(normalized_lines) + "\n"

    def step_repl(m: re.Match[str]) -> str:
        counts["numbered_steps"] += 1
        line_start = text.rfind("\n", 0, m.start()) + 1
        prior_same_line = text[line_start:m.start()]
        if prior_same_line.strip():
            return "\n" + m.group("number") + ". "
        return m.group("indent") + m.group("number") + ". "

    text = STEP_MARKER.sub(step_repl, text)

    def alpha_repl(m: re.Match[str]) -> str:
        counts["alphabetic_substeps"] += 1
        para_start = text.rfind("\n\n", 0, m.start()) + 2
        paragraph_prefix = text[para_start:m.start()]
        nested = bool(re.match(r"^[ \t]*\d{1,2}\.\s+", paragraph_prefix))
        indent = "    " if nested else ""
        return "\n" + indent + "- " + m.group("letter").lower() + ". "

    text = ALPHA_MARKER.sub(alpha_repl, text)
    orphan_pattern = re.compile(
        r"(?m)^[ \t]*-[ \t]*\n(?:[ \t]*\n)*(?=[ \t]*-[ \t]+[a-z]\. )",
        re.I,
    )
    text, removed_orphans = orphan_pattern.subn("", text)
    counts["orphan_list_separators_removed"] += removed_orphans

    def fix_bold_span(m: re.Match[str]) -> str:
        content = m.group(1).strip()
        prefix = suffix = ""
        if m.start() > 0:
            prev = text[m.start() - 1]
            adjacent_bold = text[max(0, m.start() - 2):m.start()] == "**"
            if prev.isalnum() or prev in "-—–,:;" or adjacent_bold:
                prefix = " "
        if m.end() < len(text):
            nxt = text[m.end()]
            if nxt.isalnum() or nxt in "—–":
                suffix = " "
        counts["bold_space_before"] += int(bool(prefix))
        counts["bold_space_after"] += int(bool(suffix))
        return prefix + "**" + content + "**" + suffix

    text = re.sub(r"\*\*([^*\n]+?)\*\*", fix_bold_span, text)
    text = re.sub(r"(?m)^([ \t]*\d{1,2}\.)(?=[A-Za-z])", r"\1 ", text)
    text = re.sub(r"[ \t]+(?=\n)", "", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = text.rstrip() + "\n"
    return text, counts


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True, help="Local wiki root containing chapters/")
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--check", action="store_true", help="Report whether changes would be made")
    modes.add_argument("--apply", action="store_true", help="Write normalized chapter Markdown")
    args = parser.parse_args()
    chapters = sorted((args.root.resolve() / "chapters").glob("*.md"))
    if not chapters:
        parser.error(f"No chapter Markdown files beneath {args.root / 'chapters'}")
    changed_files = 0
    totals: dict[str, int] = {}
    for path in chapters:
        original = path.read_text(encoding="utf-8")
        revised, counts = normalize(original)
        if revised != original:
            changed_files += 1
            if args.apply:
                path.write_text(revised, encoding="utf-8")
        for key, value in counts.items():
            totals[key] = totals.get(key, 0) + value
    print({"mode": "check" if args.check else "apply", "chapter_files": len(chapters), "changed_files": changed_files, **totals})
    return 1 if args.check and changed_files else 0


if __name__ == "__main__":
    raise SystemExit(main())
