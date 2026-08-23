# Codex Skill Portfolio

An audited public index of the Skill ecosystem used in this Codex workspace.

This repository deliberately separates three things that are often mixed together:

1. original work published under `kingxiaozhe`;
2. upstream or runtime dependencies that must retain their original attribution; and
3. local-only packages that need a provenance, consent, privacy, or safety decision before public release.

It is an index, not a bulk mirror. That keeps installation convenient while making authorship and licensing honest.

## Portfolio website

The dependency-free public showcase lives in [`site/`](site/). It includes original visual assets, responsive layouts, reduced-motion support, and no tracking or server-side dependency. See [the deployment guide](site/DEPLOY.md) to publish it on your own domain server.

## Published work

| Project | What it contributes |
| --- | --- |
| [dao-skill](https://github.com/kingxiaozhe/dao-skill) | Turn ambiguous requirements into reusable, evaluable Skill systems. |
| [editorial-tech-cover](https://github.com/kingxiaozhe/editorial-tech-cover) | Premium business-technology cover-art workflow. |
| [craft-diorama-still-life](https://github.com/kingxiaozhe/craft-diorama-still-life) | Craft-diorama image direction and production workflow. |
| [xbrief](https://github.com/kingxiaozhe/xbrief) | Evidence-bounded X/Twitter capture, with the Nuwa business panel included. |
| [article-to-social-cards](https://github.com/kingxiaozhe/article-to-social-cards) | Markdown-to-social-card visual pipeline. |
| [wewrite](https://github.com/kingxiaozhe/wewrite) | Modular Chinese WeChat writing workflow. |
| [cover-systems-studio](https://github.com/kingxiaozhe/cover-systems-studio) | Original, license-safe cover-system alternative. |
| [readme-storyboard](https://github.com/kingxiaozhe/readme-storyboard) | Original README narrative and visual-direction workflow. |
| [evidence-person-lens](https://github.com/kingxiaozhe/evidence-person-lens) | Evidence-only public-person research, deliberately excluding diagnosis and private-life speculation. |
| [photo-to-hand-drawn-video-skill](https://github.com/kingxiaozhe/photo-to-hand-drawn-video-skill) | Deterministic, verifiable photo-to-hand-drawn-video production. |
| [oh-story-claudecode](https://github.com/kingxiaozhe/oh-story-claudecode) | Long- and short-form online-fiction workflow package. |

## Audit boundary and result

The audit covers the **74 direct entries** in `~/.codex/skills` as observed on 2026-08-23. OpenAI's `.system` bundle and plugin caches are used only to identify origin; they are not treated as personal publishable source material.

The authoritative machine-readable list is [inventory.tsv](inventory.tsv). Its decisions mean:

| Decision | Meaning |
| --- | --- |
| `published` / `existing-public-project` | Available in an existing public `kingxiaozhe` project. |
| `upstream-reference` | Link to the upstream project; do not mirror it as personal work. |
| `runtime-component` / `system-bundle` | Installed as a runtime dependency, not a standalone personal release. |
| `private-*` | Retained locally because of missing provenance, machine/credential coupling, third-party permission, privacy, or safety constraints. |
| `upstream-no-republish` | A known third-party source whose installed copy lacks a verified redistributable license. |

The inventory contains no local filesystem paths, credentials, user content, or private repository metadata.

## Reproduce the audit check

```bash
git clone https://github.com/kingxiaozhe/codex-skill-portfolio.git
cd codex-skill-portfolio
python3 scripts/validate_inventory.py
```

Expected output:

```text
OK: 74 direct installed skills, 11 disposition types
```

## Contribution policy

New entries must first answer four questions:

1. Is the author and license verifiable?
2. Is publication portable, with no local secret, personal data, or machine-specific credential dependency?
3. Does the workflow make bounded claims and protect people from unsupported high-stakes inference?
4. Should it be published as its own package, contributed upstream, or simply linked here?

Only a positive, evidence-backed answer can move an entry from `private-*` to `published`.
