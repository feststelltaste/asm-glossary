---
name: add-term
description: Add a new glossary term through an interactive definition workflow
argument-hint: <term-name>
allowed-tools: Read Write Edit Bash Glob Grep
---

# Add Glossary Term

Interactive workflow for adding new definitions to the Agentic Software Modernization Glossary.

## Workflow

1. **Check existence**: Verify the term `$ARGUMENTS` does not already exist in `docs/` (search by filename and content). If it exists, tell the user and stop.

2. **Propose three definitions**: Offer three different angles on the term in the context of agentic software modernization. Label them Option A, B, C. Keep each to 2-4 sentences.

3. **Iterate**: The user picks one option (or a mix). Revise the text based on their feedback. Repeat until the user confirms.

4. **Determine category**: Decide which category fits best. Confirm with the user. The authoritative list of valid categories and their German translations lives in `scripts/update_overview.py` in the `CATEGORY_LABEL_DE` dict — read it from there, do not hardcode the list elsewhere.

5. **Create files** (only after user confirms the final text). Term files live flat in `docs/` and `docs/de/`. English filenames use a slug derived from the English term; German filenames use a slug derived from the German term (e.g., `guardrails.md` ↔ `leitplanken.md`).
   - `docs/<en-slug>.md` (English) with format:
     ```
     ---
     title: <Term Name>
     category: <English Category>
     translation_de: <de-slug>
     translation_de_title: <German Term Name>
     ---

     # <Term Name>

     > <definition text as a single blockquote>

     **See also:** [Related](related.md) · [Terms](terms.md)
     { .see-also }
     ```
   - `docs/de/<de-slug>.md` (German) with format:
     ```
     ---
     title: <German Term Name>
     category: <German Category>
     translation_en: <en-slug>
     translation_en_title: <Term Name>
     ---

     # <German Term Name>

     > <German translation of definition as a single blockquote>

     **Siehe auch:** [Verwandter](verwandter.md) · [Begriff](begriff.md)
     { .see-also }
     ```
   - "See also" links use bare filenames in the same language (e.g., `guardrails.md` in English files, `leitplanken.md` in German files).

6. **Update metadata**:
   - Run `python scripts/update_overview.py`
   - Add the term to the mindmap in `CONCEPT_MAP.md` under the right category

7. **Commit and push**:
   - Stage only the changed files
   - Commit with message: `Add glossary term: <Term Name>`
   - Push to the current branch

8. **Suggest next terms**: After finishing, suggest 3-5 terms that are not yet in the glossary but would complement the one just added. Check existing files before suggesting.

## Rules

- Follow all writing style rules from `CLAUDE.md` (no dashes of any kind, rephrase instead)
- German translations use Germanized terms where sensible; terms without a meaningful German equivalent stay in English
- Always read an existing term file first to match the current format exactly
- Pick 2-3 "See also" links from existing terms that are genuinely related
- Do not skip the iteration step; always wait for user confirmation before creating files
