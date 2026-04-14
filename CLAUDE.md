# Agentic Software Modernization Glossary

A glossary of terms related to agent-assisted software modernization.

## Files

- `docs/` – English term files, one per concept, organized by category
- `docs/de/` – German term files, mirroring the same structure
- `CONCEPT_MAP.md` – Mermaid concept maps showing relationships between terms

English and German content must always be kept in sync. Every new or updated term needs a file in both `docs/<category>/` and `docs/de/<category>/`. English filenames use a slug derived from the English term heading. German filenames use a slug derived from their German term heading (e.g., `context-rot.md` in English, `kontextverfall.md` in German).

## Scripts

- `scripts/update_overview.py` — regenerates both `mkdocs.yml` and `mkdocs-de.yml` navs, `docs/index.md`, and `docs/de/index.md` from the `docs/` file structure. Run after adding or renaming terms.
- `build.sh` — builds both the English and German sites. Always run this (not just `mkdocs build`) to get a correct full build.
- `serve.sh` — builds both sites and serves the full output locally. English at `http://localhost:8000/asm-glossary/`, German at `.../de/`.

## Adding a new term

1. Create `docs/<category>/<term>.md` (English)
2. Create `docs/de/<category>/<term>.md` (German)
3. Run `python scripts/update_overview.py`
4. Update `mkdocs-de.yml` nav manually (or extend the update script)
5. Update `CONCEPT_MAP.md` if the term has meaningful relationships worth visualizing

## Images

Images outside of `raw-assets/` must be 1200 pixels wide and compressed with pngquant. If an image does not meet these requirements, resize it to 1200px width and run pngquant on it before committing. Place source/raw images in `raw-assets/images/`.

## Writing Style

- Do not use dashes (en-dashes, em-dashes). Rephrase instead.

## Language Conventions

- The German version uses Germanized terms where sensible (e.g., "Leitplanken", "Halluzination", "Kontextfenster").
- Terms without a meaningful German equivalent remain in English (e.g., "Strangler Fig Pattern", "Human-in-the-Loop").
