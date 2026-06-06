import json
import os
from pathlib import Path

import pytest


def test_targets_file_is_valid_json():
    skill_dir = Path(__file__).resolve().parents[1]
    path = skill_dir / "references" / "source_smoke_targets.json"
    obj = json.loads(path.read_text(encoding="utf-8"))
    assert obj.get("schema") == "serenity.source_smoke_targets.v1"
    assert isinstance(obj.get("targets"), list)
    assert len(obj["targets"]) >= 3
    # basic schema sanity: each target has url + name
    for t in obj["targets"]:
        assert "name" in t and "url" in t


@pytest.mark.skipif(os.environ.get("SERENITY_RUN_NET_TESTS") != "1", reason="Network tests are opt-in")
def test_sources_are_reachable_smoke():
    # Keep this light to reduce flakiness; it only checks we can GET a few KB.
    import urllib.request

    skill_dir = Path(__file__).resolve().parents[1]
    obj = json.loads((skill_dir / "references" / "source_smoke_targets.json").read_text(encoding="utf-8"))
    targets = obj["targets"]

    ua = (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/126.0.0.0 Safari/537.36"
    )
    for t in targets:
        req = urllib.request.Request(t["url"], headers={"User-Agent": ua, "Accept": "text/html,*/*"})
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = resp.read(50_000)
            assert len(data) >= int(t.get("min_bytes", 0))
