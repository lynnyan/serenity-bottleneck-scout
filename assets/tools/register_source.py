#!/usr/bin/env python3
from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import datetime, timezone
import json
from pathlib import Path
import re
from typing import Any


ALLOWED_TIERS = {"T1", "T2", "T3", "T4"}


@dataclass(frozen=True)
class Entry:
    name: str
    url: str
    tier: str
    source_type: str
    why: str
    found_at: str
    date_published: str
    snapshot_path: str
    notes: str


def _iso_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _normalize_url(url: str) -> str:
    url = url.strip()
    # remove trailing slashes for dedupe
    url = re.sub(r"/+$", "", url)
    return url


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Register a newly discovered source into the skill registry.")
    p.add_argument("--name", required=True, help="Human readable source name")
    p.add_argument("--url", required=True, help="Canonical URL (or file path if no URL)")
    p.add_argument("--tier", required=True, choices=sorted(ALLOWED_TIERS), help="Credibility tier: T1..T4")
    p.add_argument(
        "--type",
        dest="source_type",
        default="",
        help="Source type, e.g. IR deck, filing, transcript, conference talk, interview, standards body, patent, media article",
    )
    p.add_argument("--why", default="", help="Why this source matters for this skill")
    p.add_argument("--date-published", default="", help="Publication date if known (YYYY-MM-DD or free text)")
    p.add_argument("--snapshot-path", default="", help="Optional local snapshot path (PDF/HTML) for reproducibility")
    p.add_argument("--notes", default="", help="Extra notes / caveats")
    p.add_argument(
        "--registry-md",
        default="",
        help="Override registry markdown path (default: references/source_registry.md)",
    )
    p.add_argument(
        "--registry-jsonl",
        default="",
        help="Override registry JSONL path (default: references/source_registry.jsonl)",
    )
    p.add_argument(
        "--task-dir",
        default="",
        help="Optional task folder; if set, also append a short entry to <task-dir>/sources/source_registry_task.md",
    )
    return p.parse_args()


def _load_jsonl_urls(path: Path) -> set[str]:
    if not path.exists():
        return set()
    urls: set[str] = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or not line.startswith("{"):
            continue
        try:
            obj = json.loads(line)
        except Exception:
            continue
        if isinstance(obj, dict) and obj.get("schema") == "serenity.source_registry.v1" and obj.get("url"):
            urls.add(str(obj["url"]))
    return urls


def _append_md(path: Path, entry: Entry) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    block = []
    block.append(f"### {entry.name}")
    block.append(f"- Tier: `{entry.tier}`")
    block.append(f"- Type: `{entry.source_type or 'unspecified'}`")
    block.append(f"- URL: {entry.url}")
    if entry.date_published:
        block.append(f"- Published: {entry.date_published}")
    block.append(f"- Found-at (UTC): {entry.found_at}")
    if entry.snapshot_path:
        block.append(f"- Snapshot: `{entry.snapshot_path}`")
    if entry.why:
        block.append(f"- Why: {entry.why}")
    if entry.notes:
        block.append(f"- Notes: {entry.notes}")
    block.append("")
    with path.open("a", encoding="utf-8") as f:
        f.write("\n".join(block))


def _append_jsonl(path: Path, entry: Entry) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    obj: dict[str, Any] = {
        "schema": "serenity.source_registry.v1",
        "name": entry.name,
        "url": entry.url,
        "tier": entry.tier,
        "type": entry.source_type,
        "why": entry.why,
        "date_published": entry.date_published,
        "snapshot_path": entry.snapshot_path,
        "notes": entry.notes,
        "found_at": entry.found_at,
    }
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(obj, ensure_ascii=False) + "\n")


def main() -> int:
    args = parse_args()
    skill_dir = Path(__file__).resolve().parents[2]

    registry_md = Path(args.registry_md).expanduser().resolve() if args.registry_md else (skill_dir / "references" / "source_registry.md")
    registry_jsonl = (
        Path(args.registry_jsonl).expanduser().resolve() if args.registry_jsonl else (skill_dir / "references" / "source_registry.jsonl")
    )

    url = _normalize_url(args.url)
    existing = _load_jsonl_urls(registry_jsonl)
    if url in existing:
        print(f"Already registered: {url}")
        return 0

    entry = Entry(
        name=args.name.strip(),
        url=url,
        tier=args.tier.strip(),
        source_type=args.source_type.strip(),
        why=args.why.strip(),
        found_at=_iso_now(),
        date_published=args.date_published.strip(),
        snapshot_path=args.snapshot_path.strip(),
        notes=args.notes.strip(),
    )

    _append_md(registry_md, entry)
    _append_jsonl(registry_jsonl, entry)

    if args.task_dir.strip():
        task_dir = Path(args.task_dir).expanduser().resolve()
        task_registry = task_dir / "sources" / "source_registry_task.md"
        if not task_registry.exists():
            task_registry.parent.mkdir(parents=True, exist_ok=True)
            task_registry.write_text("# Task source notes (append-only)\n\n", encoding="utf-8")
        _append_md(task_registry, entry)

    print(url)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

