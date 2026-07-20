---
title: Coverage Gap Annotation
category: Engineering & Control
translation_de: abdeckungsluecken-annotation
translation_de_title: Abdeckungslücken-Annotation
image: assets/images/en/coverage-gap-annotation.png
---

# Coverage Gap Annotation

![coverage-gap-annotation](assets/images/en/coverage-gap-annotation.png)

> Explicitly marking the places in agent-generated documentation, specs, or migration notes where a legacy source could not contribute, instead of silently filling the gap from what remains. The precondition is telling two situations apart: an access failure, where a file, log, or system could not be reached and a retry or an annotated gap is warranted, and a valid empty result, where the source was reached and genuinely has nothing to say, which is an answer, not an error. Without gap annotations, reviewers mistake a partial analysis of a legacy system for a complete one, and the missing part is invisible precisely where it matters most: in the code nobody looked at.

**See also:** [Attribution](attribution.md) · [Grounding](grounding.md) · [Structured Output](structured-output.md)
{ .see-also }
