# Portfolio visual refresh

## Design read

Redesign-preserve for a public developer and creator portfolio. Keep the current dark forest palette, information architecture, bilingual routes, public links, and accessibility baseline. Evolve the visual language toward experimental technology editorial with restrained glass material and kinetic CSS.

## Dials

- DESIGN_VARIANCE: 8
- MOTION_INTENSITY: 7
- VISUAL_DENSITY: 4

## Audit

- Typography: body, navigation, project metadata, links, and footer are undersized; the hero is oversized and wraps to three lines in Chinese.
- Material: the header is visually flat and does not separate itself from the page while scrolling.
- Motion: only the hero load reveal is present; lower sections and interactive surfaces have no narrative motion.
- Preserve: routes `/` and `/en/`, anchor IDs, copy voice, green accent, original images, public GitHub links, alt text, focus styles, reduced-motion behavior.

## Implementation slices

1. Self-host licensed Geist web fonts and use native system CJK fonts for Chinese.
2. Add a dedicated typography and motion CSS layer.
3. Build one frosted, feather-edged sticky header with a transparency fallback.
4. Add motivated CSS motion: hero hierarchy, project breadth rail, scroll entry, image drift, and hover feedback.
5. Verify Chinese and English desktop/mobile rendering, reduced-motion behavior, routes, assets, and CI.

## Reuse decision

Use the existing dependency-free static architecture and original image assets. Reuse the mature OFL-licensed Geist family for Latin glyphs and native system CJK fonts for Chinese. Do not add a JavaScript animation dependency because native CSS is sufficient for the requested motion layer and keeps deployment weight low.

## Verification verdict

- Chinese and English hero titles render in two lines at the desktop preview width.
- Browser-computed body text is 18px and navigation text is 16px.
- The header uses a 24px backdrop blur with saturation and contrast, plus a feathered filtered edge.
- The project rail, hero drift, sheen, underline, hover feedback, and view-timeline motion are active; reduced-motion disables them.
- Modern AVIF assets reduce the loaded page weight from more than 7MB of PNG sources to about 294KB while retaining the PNG social-card fallback.
- Lighthouse: Performance 99, Accessibility 100, Best Practices 100, SEO 100; LCP about 1.95s, CLS 0, TBT 0ms.
- `scripts/validate_inventory.py`, `scripts/validate_site.py`, `git diff --check`, local HTTP routes, CSS, fonts, images, and favicon pass.

Verdict: approved for commit and public repository synchronization.
