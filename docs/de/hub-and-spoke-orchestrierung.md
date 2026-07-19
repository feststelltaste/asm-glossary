---
title: Hub-and-Spoke-Orchestrierung
category: Infrastruktur
translation_en: hub-and-spoke-orchestration
translation_en_title: Hub-and-Spoke Orchestration
image: assets/images/hub-and-spoke-orchestrierung.png
---

# Hub-and-Spoke-Orchestrierung

![hub-and-spoke-orchestrierung](assets/images/hub-and-spoke-orchestrierung.png)

> Eine Multi-Agenten-Topologie, in der jeder spezialisierte Unteragent ausschließlich mit einem zentralen Koordinator spricht, nie mit einem anderen Unteragenten. Der Koordinator verteilt die Arbeit, empfängt jedes Ergebnis und entscheidet über den nächsten Schritt, sodass jede Entscheidung einen prüfbaren Punkt durchläuft und eine fehlerhafte Ausgabe nicht ungeprüft in die Eingabe eines anderen Agenten fließen kann. Das Muster erodiert schleichend, sobald ein Unteragent Werkzeuge erhält, mit denen er im Gebiet eines anderen handeln kann; die Architektur hält nur, wenn das Werkzeugset jeder Speiche auf ihre eigene Spezialität begrenzt bleibt.

**Siehe auch:** [Orchestrierung](orchestrierung.md) · [Unteragent](unteragent.md) · [Agententeams](agententeams.md) · [Werkzeugüberlastung](werkzeugueberlastung.md)
{ .see-also }
