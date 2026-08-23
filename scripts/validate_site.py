#!/usr/bin/env python3
"""Verify the static portfolio has its required files and public-safe copy."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
CSS = SITE / "styles.css"
PAGES = [SITE / "index.html", SITE / "en" / "index.html"]
ASSETS = [
    SITE / "assets" / "hero-workflow-desk.png",
    SITE / "assets" / "evidence-materials.png",
    SITE / "assets" / "visual-systems.png",
]


def main() -> None:
    assert all(page.is_file() for page in PAGES), "missing Chinese or English entry page"
    assert CSS.is_file(), "missing site/styles.css"
    assert all(asset.is_file() and asset.stat().st_size > 0 for asset in ASSETS), "missing image asset"
    stylesheet = CSS.read_text(encoding="utf-8")
    chinese, english = (page.read_text(encoding="utf-8") for page in PAGES)
    for page in (chinese, english):
        assert "kingxiaozhe" in page
        assert "https://github.com/kingxiaozhe" in page
        assert "<main id=\"main\">" in page
        assert page.count("<img ") == 4, "expected four editorial image placements"
        assert page.count("alt=") >= 4, "every image needs alternative text"
        assert "—" not in page and "–" not in page, "em or en dash is not allowed in page copy"
        assert "/Users/zero/" not in page
    assert '<html lang="zh-CN">' in chinese
    assert '<html lang="en">' in english
    assert 'href="en/"' in chinese and 'href="../"' in english
    assert "prefers-reduced-motion" in stylesheet
    assert "@media (max-width: 640px)" in stylesheet
    assert "text-wrap: balance" in stylesheet and "text-wrap: pretty" in stylesheet
    assert "PingFang SC" in stylesheet and "html[lang=\"en\"]" in stylesheet
    assert "/Users/zero/" not in stylesheet
    print("OK: bilingual static site, localized typography, assets, public links, and responsive motion safeguards")


if __name__ == "__main__":
    main()
