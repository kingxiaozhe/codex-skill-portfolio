# Self-hosted font sources

- IBM Plex Mono and IBM Plex Sans SC are published by IBM under the SIL Open Font License 1.1: <https://github.com/IBM/plex>
- The previous Geist assets came from Vercel's OFL-licensed Geist repository: <https://github.com/vercel/geist-font>

The active portfolio typography follows the IBM Plex family. English, Latin text, numbers, navigation, and project names use IBM Plex Mono. Chinese glyphs use IBM Plex Sans SC, which keeps the bilingual system in one related family instead of falling back to an unrelated system font.

All active `ibm-plex-*.woff2` files are deterministic subsets of IBM's official complete web fonts and contain only the glyphs used by the Chinese and English pages. This reduces each Chinese font from roughly 4 MB to about 75 KB and each Mono weight from roughly 50 KB to about 11 KB. IBM's OFL text is stored as `OFL-IBM-Plex.txt`; the existing Geist license remains in `OFL-1.1.txt`.
