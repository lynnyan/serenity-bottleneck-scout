#!/usr/bin/env python3
from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import datetime, timezone
import gzip
import json
from pathlib import Path
import sys
import urllib.error
import urllib.request


DEFAULT_UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/126.0.0.0 Safari/537.36"
)


@dataclass(frozen=True)
class Target:
    name: str
    url: str
    expect_any: list[str]
    min_bytes: int
    blocked_markers: list[str]
    allow_blocked: bool


def _iso_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Network smoke test for external sources (manual/integration).")
    p.add_argument(
        "--targets",
        default="",
        help="Path to targets JSON (default: references/source_smoke_targets.json)",
    )
    p.add_argument("--timeout", type=int, default=20)
    p.add_argument("--user-agent", default=DEFAULT_UA)
    p.add_argument("--out", default="", help="Optional JSON output path for results")
    return p.parse_args()


def _load_targets(path: Path) -> list[Target]:
    obj = json.loads(path.read_text(encoding="utf-8"))
    items = obj.get("targets", [])
    out: list[Target] = []
    for it in items:
        out.append(
            Target(
                name=str(it["name"]),
                url=str(it["url"]),
                expect_any=list(it.get("expect_any", [])),
                min_bytes=int(it.get("min_bytes", 0)),
                blocked_markers=list(it.get("blocked_markers", [])),
                allow_blocked=bool(it.get("allow_blocked", False)),
            )
        )
    return out


def _fetch(url: str, timeout: int, user_agent: str) -> tuple[int, str, bytes, str]:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": user_agent, "Accept": "text/html,*/*"},
        method="GET",
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        status = getattr(resp, "status", 200)
        content_type = resp.headers.get("Content-Type", "")
        data = resp.read(2_000_000)  # 2MB cap for smoke test
        final_url = resp.geturl()
        return int(status), str(content_type), data, final_url


def main() -> int:
    args = parse_args()
    skill_dir = Path(__file__).resolve().parents[1]
    targets_path = Path(args.targets).expanduser().resolve() if args.targets else (skill_dir / "references" / "source_smoke_targets.json")
    targets = _load_targets(targets_path)

    results = []
    failed = 0
    for t in targets:
        item = {
            "name": t.name,
            "url": t.url,
            "ok": False,
            "status": None,
            "bytes": 0,
            "final_url": "",
            "error": "",
            "content_type": "",
            "classification": "FAIL",
        }
        try:
            status, ctype, data, final_url = _fetch(t.url, args.timeout, args.user_agent)
            text = ""
            try:
                probe = data
                # Some sources may return gzipped bytes even without a transparent decoder.
                if probe[:2] == b"\x1f\x8b":
                    try:
                        probe = gzip.decompress(probe)
                    except Exception:
                        probe = data
                text = probe.decode("utf-8", errors="ignore").lower()
            except Exception:
                text = ""
            ok = True
            if status >= 400:
                ok = False
            if len(data) < t.min_bytes:
                ok = False
            if t.expect_any:
                if not any(s.lower() in text for s in t.expect_any):
                    ok = False

            blocked = False
            if t.blocked_markers:
                blocked = any(m.lower() in text for m in t.blocked_markers)

            classification = "OK"
            if blocked:
                classification = "BLOCKED"
            if not ok:
                classification = "FAIL"

            # allow_blocked means: treat BLOCKED as pass for availability, but keep classification.
            ok_effective = ok
            if blocked and t.allow_blocked and status < 400 and len(data) >= t.min_bytes:
                ok_effective = True
                if classification == "FAIL":
                    classification = "BLOCKED"

            item.update(
                {
                    "ok": ok_effective,
                    "status": status,
                    "bytes": len(data),
                    "final_url": final_url,
                    "content_type": ctype,
                    "classification": classification,
                }
            )
            if not ok_effective:
                failed += 1
        except urllib.error.HTTPError as e:
            item.update({"ok": False, "status": int(getattr(e, "code", 0) or 0), "error": f"HTTPError: {e}"})
            failed += 1
        except Exception as e:
            item.update({"ok": False, "error": str(e)})
            failed += 1
        results.append(item)

    payload = {"schema": "serenity.source_smoke_results.v1", "ran_at": _iso_now(), "targets": results}
    if args.out:
        out_path = Path(args.out).expanduser().resolve()
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    for r in results:
        status = r.get("status")
        tag = r.get("classification") or ("OK" if r.get("ok") else "FAIL")
        print(f"[{tag}] {r['name']} status={status} bytes={r.get('bytes')} url={r['url']}")
        if r.get("error"):
            print(f"      error: {r['error']}")

    return 0 if failed == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
