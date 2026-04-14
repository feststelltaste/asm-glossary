# Agentic Software Modernization Glossary

A glossary of terms related to agent-assisted software modernization, available in English and German.

Live site: [feststelltaste.github.io/asm-glossary](https://feststelltaste.github.io/asm-glossary/)

**Agentic software modernization** is the practice of using AI agents, LLM-based systems capable of autonomous, multi-step reasoning and tool use, to analyze, refactor, and migrate legacy software systems. Rather than relying solely on manual effort or purely rule-based automation, this approach aims for the sweet spot between non-deterministic and deterministic workloads, keeping a high level of automation while preserving controlled autonomy. Agentic modernization acknowledges the limitations of AI agents working with legacy code and applies supporting techniques such as sprouting, seams, incremental improvement, and domain-driven refactoring to shape the codebase into something agents can meaningfully work with. Within this scaffolding, agents generate transformation plans, execute changes, and verify results, reducing technical debt without introducing cognitive debt, all under human supervision.

## Contents

- English terms: [`docs/`](docs/)
- German terms: [`docs/de/`](docs/de/)
- Concept map: [`CONCEPT_MAP.md`](CONCEPT_MAP.md)

## Local Development

```bash
pip install mkdocs-material
bash serve.sh
```

English site: `http://localhost:8000/asm-glossary/`
German site: `http://localhost:8000/asm-glossary/de/`

## Image Generation Prompt

For generating term illustrations, use this prompt with Nano Banana 2 (prompt version 2):

> Create an image as a clean, minimalist black and white line art illustration. Style: Modern vector-style textbook diagram. Solid black outlines on a pure white background. No shading, no textures, no text, no titles. High contrast, isolated on white. Keep the illustration extremely minimalistic: use as few lines and shapes as possible to convey the concept. Avoid decorative elements, unnecessary details, and visual clutter. Professional and clinical. Topic: [TOPIC and DESCRIPTION]

## Adding a Term

Use the `/add-term` skill in Claude Code, which guides you through the full workflow interactively.

## Origin

This glossary was initially brainstormed and drafted using [Claude Code](https://claude.ai/code) with Claude Opus 4.6, working from Markus's own material and notes. The generated content was then reviewed, reworked, and curated by [Markus Harrer](https://markusharrer.de).

## License

Published under [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/). Free to share and adapt with attribution.
