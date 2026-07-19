---
title: Lost in the Middle
category: Fundamentals
translation_de: lost-in-the-middle
translation_de_title: Lost in the Middle
image: assets/images/en/lost-in-the-middle.png
---

# Lost in the Middle

![lost-in-the-middle](assets/images/en/lost-in-the-middle.png)

> A positional bias of language models: material at the beginning and end of a long input is weighted more heavily than material in between, even when the context window has plenty of room left. The failure has a U-shape, for example release notes where the first and last commits are summarized precisely while the middle stretch collapses into "various bug fixes". Unlike Attention Dilution, which grows with the number of items competing for analysis, this effect depends purely on position, so it responds to positional fixes: place critical information at the edges of the prompt, or process long sequences in smaller batches.

**See also:** [Context Window](context-window.md) · [Context Rot](context-rot.md) · [Attention Dilution](attention-dilution.md)
{ .see-also }
