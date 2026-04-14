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

4. **Determine category**: Decide which category fits best based on existing categories in `CLAUDE.md`. Confirm with the user.

5. **Create files** (only after user confirms the final text):
   - `docs/<category>/<term>.md` (English) with format:
     ```
     # <Term Name>
     *draft version*

     <definition text>

     **See also:** [Related](link.md) · [Terms](link.md)
     { .see-also }
     ```
   - `docs/de/<category>/<term>.md` (German) with format:
     ```
     # <Term Name>
     *Entwurfsversion*

     <German translation of definition>

     **Siehe auch:** [Verwandter](link.md) · [Begriff](link.md)
     { .see-also }
     ```

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
