---
title: Validierungsschleife
category: Entwicklung & Kontrolle
translation_en: validation-retry-loop
translation_en_title: Validation-Retry Loop
image: assets/images/validierungsschleife.png
---

# Validierungsschleife

![validierungsschleife](assets/images/validierungsschleife.png)

> Ein Selbstkorrekturmuster, bei dem die strukturierte Ausgabe eines Agenten programmatisch geprüft und bei einem Fehlschlag mit einer gezielten Fehlermeldung für einen weiteren Versuch zurückgeschickt wird. Entscheidend ist, dass das Ausgabeschema die Argumentation externalisiert, etwa über ein Feld, das die erkannten Muster neben der finalen Klassifikation auflistet, sodass die Validierung Widersprüche zwischen Belegen und Schlussfolgerung erkennen kann, nicht nur fehlerhaftes JSON. Rückmeldungen wie "du hast X erkannt, aber Y geschlossen" geben dem Modell etwas Konkretes zum Korrigieren; ein bloßes "versuch es noch einmal" tut das nicht.

**Siehe auch:** [Strukturierte Ausgabe](strukturierte-ausgabe.md) · [Feedbackschleife](feedbackschleife.md) · [Leitplanken](leitplanken.md)
{ .see-also }
