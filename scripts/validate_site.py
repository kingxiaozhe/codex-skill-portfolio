#!/usr/bin/env python3
"""Verify the static portfolio has its required files and public-safe copy."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
HTML = SITE / "index.html"
CSS = SITE / "styles.css"
ASSETS = [
    SITE / "assets" / "hero-workflow-desk.png",
    SITE / "assets" / "evidence-materials.png",
    SITE / "assets" / "visual-systems.png",
]


def main() -> None:
    assert HTML.is_file(), "missing site/index.html"
    assert CSS.is_file(), "missing site/styles.css"
    assert all(asset.is_file() and asset.stat().st_size > 0 for asset in ASSETS), "missing image asset"
    page = HTML.read_text(encoding="utf-8")
    stylesheet = CSS.read_text(encoding="utf-8")
    assert "kingxiaozhe" in page
    assert "https://github.com/kingxiaozhe" in page
    assert "<main id=\"main\">" in page
    assert "Skip to content" in page
    assert page.count("<img ") == 4, "expected four editorial image placements"
    assert page.count("alt=") >= 4, "every image needs alternative text"
    assert "prefers-reduced-motion" in stylesheet
    assert "@media (max-width: 640px)" in stylesheet
    assert "—" not in page and "–" not in page, "em or en dash is not allowed in page copy"
    assert "/Users/zero/" not in page and "/Users/zero/" not in stylesheet
    print("OK: static site markup, assets, public links, and responsive motion safeguards")


if __name__ == "__main__":
    main()
