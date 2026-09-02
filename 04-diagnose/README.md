# 🔬 Diagnose-Abläufe

Hier stehen die **Fehlersuchen**: Symptom → Schnelltest → Ursachenliste → Testprotokoll → Maßnahme.

Jede Datei ist so aufgebaut, dass man sie **ans Rad mitnehmen** und der Reihe nach abarbeiten
kann. Am Ende ist immer ein Protokoll zum Ausfüllen.

| Datei | Symptom | Baustelle | Prio |
|---|---|---|---|
| [`vorderrad-schwergaengig.md`](vorderrad-schwergaengig.md) | Vorderrad dreht nicht frei | #1 | 🔴 |
| [`hinterrad-lager-feder.md`](hinterrad-lager-feder.md) | Hinterrad schwerer laufend + verlorene Feder | #2 | 🔴 |
| [`hintere-bremse-kehrt-nicht-zurueck.md`](hintere-bremse-kehrt-nicht-zurueck.md) | Hintere Bremse kehrt nicht selbstständig zurück | #3 | 🔴 |

Neue Diagnose anlegen: [`../templates/diagnose-template.md`](../templates/diagnose-template.md)

## Gemeinsames Prinzip: Binärsuche

Immer so vorgehen, dass jeder Test die möglichen Ursachen **halbiert**:

1. System in zwei Hälften teilen (z. B. „Rad ausgebaut“ vs. „Rad eingebaut“)
2. Testen, in welcher Hälfte das Problem steckt
3. Diese Hälfte wieder teilen
4. Wiederholen, bis nur noch eine Ursache übrig ist

Das ist schneller und billiger als „alles einmal tauschen und hoffen“.

## Wichtige Grundregel

**Erst messen und testen, dann kaufen.** Jede Diagnose-Datei endet mit einer Liste der
benötigten Teile – die trägt man dann in
[`../03-todos/einkaufsliste.md`](../03-todos/einkaufsliste.md) ein.
