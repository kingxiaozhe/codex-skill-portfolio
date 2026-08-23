#!/usr/bin/env python3
"""Verify the static portfolio has its required files and public-safe copy."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
CSS = SITE / "styles.css"
EXPERIENCE = SITE / "experience.css"
PAGES = [SITE / "index.html", SITE / "en" / "index.html"]
ASSETS = [
    SITE / "assets" / "hero-workflow-desk.png",
    SITE / "assets" / "evidence-materials.png",
    SITE / "assets" / "visual-systems.png",
    SITE / "assets" / "hero-workflow-desk.avif",
    SITE / "assets" / "evidence-materials.avif",
    SITE / "assets" / "visual-systems.avif",
    SITE / "assets" / "favicon.png",
]
FONT_ASSETS = [
    SITE / "assets" / "fonts" / "geist-latin.woff2",
    SITE / "assets" / "fonts" / "geist-mono-latin.woff2",
    SITE / "assets" / "fonts" / "OFL-1.1.txt",
    SITE / "assets" / "fonts" / "SOURCES.md",
]


def main() -> None:
    assert all(page.is_file() for page in PAGES), "missing Chinese or English entry page"
    assert CSS.is_file(), "missing site/styles.css"
    assert EXPERIENCE.is_file(), "missing site/experience.css"
    assert all(asset.is_file() and asset.stat().st_size > 0 for asset in ASSETS), "missing image asset"
    assert all(asset.is_file() and asset.stat().st_size > 0 for asset in FONT_ASSETS), "missing font or font license asset"
    stylesheet = CSS.read_text(encoding="utf-8")
    experience = EXPERIENCE.read_text(encoding="utf-8")
    chinese, english = (page.read_text(encoding="utf-8") for page in PAGES)
    for page in (chinese, english):
        assert "kingxiaozhe" in page
        assert "https://github.com/kingxiaozhe" in page
        assert "<main id=\"main\">" in page
        assert page.count("<img ") == 4, "expected four editorial image placements"
        assert page.count("alt=") >= 4, "every image needs alternative text"
        assert "experience.css" in page, "enhanced typography and motion layer must load"
        assert "skill-rail" in page, "project breadth rail must exist"
        assert "—" not in page and "–" not in page, "em or en dash is not allowed in page copy"
        assert "/Users/zero/" not in page
    assert '<html lang="zh-CN">' in chinese
    assert '<html lang="en">' in english
    assert 'href="en/"' in chinese and 'href="../"' in english
    assert "prefers-reduced-motion" in stylesheet
    assert "@media (max-width: 640px)" in stylesheet
    assert "text-wrap: balance" in stylesheet and "text-wrap: pretty" in stylesheet
    assert "PingFang SC" in stylesheet and "html[lang=\"en\"]" in stylesheet
    assert "@font-face" in experience and "Geist Portfolio" in experience
    assert "backdrop-filter: blur(24px)" in experience and "prefers-reduced-transparency" in experience
    assert "animation-timeline: view()" in experience and "prefers-reduced-motion" in experience
    assert "font-size: 18px" in experience, "body text scale must remain readable"
    assert "hero-workflow-desk.avif" in chinese and "hero-workflow-desk.avif" in english
    assert "/Users/zero/" not in stylesheet and "/Users/zero/" not in experience
    print("OK: bilingual static site, self-hosted licensed fonts, glass header, CSS motion, public links, and accessibility safeguards")


if __name__ == "__main__":
    main()
