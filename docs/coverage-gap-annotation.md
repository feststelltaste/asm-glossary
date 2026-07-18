---
title: Coverage Gap Annotation
category: Engineering & Control
translation_de: abdeckungsluecken-annotation
translation_de_title: Abdeckungslücken-Annotation
image: assets/images/en/coverage-gap-annotation.png
---

# Coverage Gap Annotation

![coverage-gap-annotation](assets/images/en/coverage-gap-annotation.png)

> Explicitly marking the places in generated output where a source could not contribute, instead of silently producing something from what remains. The precondition is telling two situations apart: an access failure, where a source could not be reached and a retry or an annotated gap is warranted, and a valid empty result, where the source was reached and genuinely has nothing, which is an answer, not an error. Without gap annotations, readers mistake partial output for complete output, and the missing part is invisible precisely where it matters.

**See also:** [Attribution](attribution.md) · [Grounding](grounding.md) · [Structured Output](structured-output.md)
{ .see-also }
