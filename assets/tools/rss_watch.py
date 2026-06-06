#!/usr/bin/env python3
"""
RSS fetcher for monitoring partner PR / company news.

Input: one or more RSS/Atom URLs.
Output: JSONL with (feed_url, title, link, published).
"""

from __future__ import annotations

import argparse
import json
import time
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class Item:
    feed_url: str
    title: str
    link: str
    published: str


def _fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "rss-watch/1.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read()


def _text(el: ET.Element | None, default: str = "") -> str:
    if el is None or el.text is None:
        return default
    return el.text.strip()


def parse_rss(feed_url: str, xml_bytes: bytes) -> list[Item]:
    root = ET.fromstring(xml_bytes)

    # RSS 2.0: channel/item
    channel = root.find("channel")
    if channel is not None:
        out: list[Item] = []
        for it in channel.findall("item"):
            out.append(
                Item(
                    feed_url=feed_url,
                    title=_text(it.find("title")),
                    link=_text(it.find("link")),
                    published=_text(it.find("pubDate")),
                )
            )
        return out

    # Atom: entry
    out = []
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    for entry in root.findall("atom:entry", ns):
        title = _text(entry.find("atom:title", ns))
        link_el = entry.find("atom:link", ns)
        link = link_el.attrib.get("href", "") if link_el is not None else ""
        published = _text(entry.find("atom:updated", ns)) or _text(entry.find("atom:published", ns))
        out.append(Item(feed_url=feed_url, title=title, link=link, published=published))
    return out


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--feed", action="append", required=True, help="RSS/Atom feed URL (repeatable)")
    p.add_argument("--out", default="rss_items.jsonl", help="Output JSONL path")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    all_items: list[Item] = []
    for url in args.feed:
        xml_bytes = _fetch(url)
        items = parse_rss(url, xml_bytes)
        all_items.extend(items)
        time.sleep(0.2)

    with open(args.out, "w", encoding="utf-8") as f:
        for it in all_items:
            f.write(json.dumps(it.__dict__, ensure_ascii=False) + "\n")
    print(args.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

