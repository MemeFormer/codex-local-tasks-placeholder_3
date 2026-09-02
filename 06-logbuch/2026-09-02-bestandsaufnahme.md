# Logbuch – 2026-09-02 – Bestandsaufnahme & Doku aufgebaut

**Dauer:** – · **Baustellen:** alle (Bestandsaufnahme) · **Nächster Schritt:** Session 1 – Diagnose & Messen

## Was wurde gemacht

Bestand aus zwei Zusammenfassungen (von einem anderen Assistenten erstellt) in eine
strukturierte Teile-Datenbank überführt:

- Beide Räder mit Stammdaten-Blättern angelegt (`01-bikes/`)
- Fachbegriffe-Glossar DE ↔ EN erstellt (`02-teile/00-fachbegriffe-glossar.md`)
- 8 Baugruppen-Dateien mit Ist-Zustand, Messlisten und Einkaufsbedarf (`02-teile/`)
- Diagnose-Abläufe für die drei 🔴-Baustellen (`04-diagnose/`)
- Anleitungen + Referenzwerte (`05-anleitungen/`)
- Messdatenblatt zum Ausfüllen am Rad (`04-messdaten/`)
- Einkaufsliste, Werkzeugliste, Sicherheitscheck (`03-todos/`)

## Neue Erkenntnisse / Hypothesen

Diese Punkte standen in der Ursprungs-Zusammenfassung **nicht** und sollten geprüft werden:

1. **Die Kassette ließ sich vermutlich deshalb nicht lösen, weil keine Kettenpeitsche
   verwendet wurde.** Ohne Kettenpeitsche dreht sich das Ritzelpaket mit – exakt das
   beschriebene Symptom („Lockring hat nichts gebracht, Ritzel haben sich nicht bewegt“).
   Zusätzlich: erst klären, ob es überhaupt eine **Kassette** und kein **Schraubkranz** ist.

2. **„Weiche Bremshebel“ könnten ein Zugweg-Problem sein**, nicht ein Feder-Problem.
   Wenn die schwarzen Hebel short-pull sind und die Zangen long-pull (oder umgekehrt),
   ist das Gefühl konstruktiv schwammig – **dann helfen weder Bolzen noch Federn**.
   → Erst Modellnummern ablesen und den Zugweg abgleichen.

3. **Die hintere Bremse und die weichen Hebel könnten dieselbe Ursache haben**, falls der
   hintere Bremshebel einer der schwarzen ist. → Prüfen.

4. **Beim Vorderrad „dreht nicht frei“ zuerst klären, ob es ein Nabendynamo ist.**
   Ein Nabendynamo-Rad dreht konstruktionsbedingt nur 1–2 Umdrehungen weiter – das ist
   normal und kein Defekt.

5. **Die verlorene „kleine Feder“ ist mit hoher Wahrscheinlichkeit eine
   Schnellspanner-Feder.** Falls sie fehlt, verkantet der Schnellspanner beim Spannen und
   drückt das Lager zusammen → **könnte allein schon die Schwergängigkeit erklären.**

6. **🔴 Neue Sicherheitsbaustelle: Quill-Vorbau-Einstecktiefe.** Wenn der Gabelschaft nur
   1–2 Gewindegänge über dem Steuerrohr steht, kann der Schaftvorbau möglicherweise nicht
   tief genug eingesteckt sein. Dann wirkt eine große Hebelkraft an der Schaftkante →
   **Bruchgefahr**. Unbedingt prüfen, ob die „MIN INSERTION“-Markierung im Schaftrohr liegt.

7. **🔴 Felgen-Bremsflanken:** Die abgefahrenen Bremsflanken wurden im Bericht erwähnt,
   danach wurde das **Original-Hinterrad wieder eingebaut**. Der Verschleißzustand muss
   geprüft werden – eine durchgebremste Flanke kann unter Bremsdruck brechen.
   Zusätzlich: eine scharfe Felgenkante kann die Ursache für die nicht zurückkehrende
   Bremse sein (der Belag hakt an der Kante).

8. **Die alte weiße Gabel aufheben!** Falls ihr Schaft lang genug für den weißen Steuerkopf
   ist, löst das die Steuersatz-Baustelle kostenlos.

9. **Lenker-Gefühl könnte auch an der Geometrie liegen:** Falls die schwarze Gabel eine
   geringere Einbauhöhe hat, wird der Lenkwinkel steiler und der Nachlauf kleiner →
   nervöseres Lenkverhalten. Das ist keine reine Gewöhnungssache.

10. **Die gekürzte Kette + Big-Big** kann das Schaltwerk überstrecken und im Extremfall das
    Schaltauge abreißen. Bis zur neuen Kette: diese Kombination vermeiden.

## Offene Punkte nach dieser Session

- Alle `❓ TODO`-Werte in den Baugruppen-Dateien
- Messdatenblatt ist komplett leer
- Fotos fehlen
- Datumsangaben im Logbuch fehlen

## Nächster Schritt

**Session 1: Diagnose & Messen** (ca. 60–90 min, kaum Werkzeug nötig).
Reihenfolge: [`../03-todos/offene-baustellen.md`](../03-todos/offene-baustellen.md)
→ „Empfohlene Reihenfolge der Werkstatt-Sessions“.
