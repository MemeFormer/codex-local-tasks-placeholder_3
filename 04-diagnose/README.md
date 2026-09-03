# 🔬 Diagnose-Abläufe

Hier stehen die **Fehlersuchen**: Symptom → Schnelltest → Ursachenliste → Testprotokoll → Maßnahme.

Jede Datei ist so aufgebaut, dass man sie **ans Rad mitnehmen** und der Reihe nach abarbeiten
kann. Am Ende ist immer ein Protokoll zum Ausfüllen.

| Datei | Symptom | Baustelle | Prio |
|---|---|---|---|
| [`hintere-bremse-kehrt-nicht-zurueck.md`](hintere-bremse-kehrt-nicht-zurueck.md) | Hintere Bremse kehrt nicht zurück – **neue Beläge sind Hauptverdacht** | #3 | 🔴 |
| [`hinterrad-lager-feder.md`](hinterrad-lager-feder.md) | Hinterrad schwerer laufend + verlorene Feder | #4 | 🔴 |
| [`vordere-bremsarme-sockel.md`](vordere-bremsarme-sockel.md) | Vordere Bremsarme zu weich + passen nicht auf den Bremssockel | #5 | 🟡 |
| [`vorderrad-schwergaengig.md`](vorderrad-schwergaengig.md) | „Vorderrad dreht nicht frei“ → ✅ **Nabendynamo, normal!** Nur Verifikationstest | ~~#13~~ | 🟢 |

### Wichtigste Erkenntnisse vorab

| Baustelle | 💡 Erkenntnis |
|---|---|
| #3 Hintere Bremse | Zange/Federn/Zug sind original – **nur die Beläge wurden getauscht**. Deshalb: **erst Abschnitt 0 (Beläge)**, nicht den Zug. |
| #5 Vordere Bremsarme | Die Federspannschraube ist das **falsche Werkzeug** – die echte Stellgröße ist die **Federraste** (3 Bohrungen im Sockel). 0 €, 10 min. |
| #5 Bremssockel | „Passt nicht auf die Aufnahme“ ist meist **Lack/Rost auf dem Sockel** → mit 400er Schleifleinen abziehen. |
| #5 Sockel tauschen? | **Nur bei Alugabel** (eingeschraubt). Bei Stahlgabel angeschweißt → ❌ nicht selbst. **Magnet-Test!** |
| #13 Vorderrad | **Nabendynamo** dreht von Hand nur 1–2 Umdrehungen – das ist **normal**, kein Defekt. |
| #4 Hinterrad | Fehlende **QR-Feder** → Schnellspanner verkantet → drückt das Lager zusammen. Test: QR raus, drehen. |

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
