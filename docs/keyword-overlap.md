---
title: Keyword Overlap
category: Infrastructure
translation_de: schluesselwortueberlappung
translation_de_title: Schlüsselwortüberlappung
image: assets/images/en/keyword-overlap.png
---

# Keyword Overlap

![keyword-overlap](assets/images/en/keyword-overlap.png)

> A tool-selection failure caused by instruction wording that echoes a tool's name: a prompt saying "check the security of each function" alongside a tool named check_security can pull the model toward the tool at the wrong moment, or toward following the text when it should call the tool. The overlap acts as an unintended routing cue that overrides well-written tool descriptions. The fix is vocabulary separation: phrase instructions in terms that do not mirror tool names, and revisit that wording after every system prompt change.

**See also:** [Tool Use](tool-use.md) · [Prompt Engineering](prompt-engineering.md) · [Tool Overload](tool-overload.md)
{ .see-also }
