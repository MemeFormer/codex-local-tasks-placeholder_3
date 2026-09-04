# 🔬 Diagnose-Abläufe

Hier stehen die **Fehlersuchen**: Symptom → Schnelltest → Ursachenliste → Testprotokoll → Maßnahme.

Jede Datei ist so aufgebaut, dass man sie **ans Rad mitnehmen** und der Reihe nach abarbeiten
kann. Am Ende ist immer ein Protokoll zum Ausfüllen.

| Datei | Symptom | Baustelle | Prio | Status |
|---|---|---|---|---|
| [`rst-vogue-tnl-federgabel.md`](rst-vogue-tnl-federgabel.md) | 🔴 **Original-Gabel RST Vogue TNL defekt** – gibt nach, aber nur die Feder; Öl ausgetreten, Rost an den Standrohren. **Rettbar?** | **#14** | 🔴 | 🔴 **offen – hat Vorrang** |
| [`vordere-bremsarme-sockel.md`](vordere-bremsarme-sockel.md) | Weiße Deore-Bremsarme lassen sich nicht befestigen – **Cantistifte zu KURZ** | #5 | 🔴 | 🔴 offen, **Ursache korrigiert** |
| [`hintere-bremse-kehrt-nicht-zurueck.md`](hintere-bremse-kehrt-nicht-zurueck.md) | Hintere Bremse kehrt nicht zurück | ~~#3~~ | 🟢 | ✅ **ERLEDIGT** – Ursache: **Bremshebel-Klemmung am Lenker** |
| [`hinterrad-lager-feder.md`](hinterrad-lager-feder.md) | Hinterrad schwerer laufend + verlorene Feder | #4 / **#4a** | 🟡 | ✅ läuft normal · 🟡 Feder offen |
| [`vorderrad-schwergaengig.md`](vorderrad-schwergaengig.md) | „Vorderrad dreht nicht frei“ → **Nabendynamo** | ~~#13~~ | 🟢 | ✅ **ERLEDIGT** – läuft mehrere Umdrehungen |

### Wichtigste Erkenntnisse vorab

| Baustelle | 💡 Erkenntnis |
|---|---|
| **#14 Schritt 0** 🔴🔴 | 🔴 **VOR dem Fingernageltest: MAGNET an den Gabelschaft + Gewinde-Prüfung.** Ein Staiger-Katalogauszug 2007 nennt die Vogue TNL **„mit Aluschaft"** in einem **A-Head**-Rad – dieses Rad hat aber **Gewindesteuersatz + Quill-Vorbau**. ⛔ **Glatter Schaft = Ahead-Gabel = passt nicht.** ⛔ **Aluschaft + Quill-Vorbau = der Keil kann den Schaft aufspreizen.** **5 Sekunden, 0 €.** → [`rst-vogue-tnl-federgabel.md`](rst-vogue-tnl-federgabel.md) **Abs. 3.0** |
| **#15 Schaltauge** 🔴 | 🆕 Vor Jahren ein **Sturz**, „hinten verbogen", Schaltung funktionierte nicht mehr – behoben wurde aber **vorne** (fremder Umwerfer). 🔴 **Symptom passt zur Lehrbuch-Signatur eines verbogenen Schaltauges.** Ein krummes Schaltauge kann zum **Speichen-Einlauf** des Schaltwerks führen. → [`../03-todos/offene-baustellen.md`](../03-todos/offene-baustellen.md) **#15** |
| **#14 RST Vogue TNL** 🔴 | **Die wichtigste Diagnose des ganzen Projekts.** Die **Original-Gabel ist noch vorhanden** und für **dieses** Steuerrohr gebaut → rettet sie Baustelle **#1, #5 und #6 auf einen Schlag**. **Fingernageltest an den Standrohren** entscheidet: keine Grübchen = rettbar (Dichtungen 14,28 € + Öl), Grübchen = verschrotten. |
| **#5 Bremssockel** 🔴 | ⛔ **Korrigiert:** Die Cantistifte der Bergamont-Gabel sind **KÜRZER**, nicht länger → die **M6-Armschraube findet keinen Gewindegriff**. **Nicht zurückdrehen!** Fix: **längere M8-Cantistifte** (brake-stuff.de **CS-M8-VA**, 14,90 €/Paar, listet **Staiger**), kürzere Armschraube oder Stifte der RST-Gabel. |
| **#5 Federraste** | Die Federspannschraube ist das **falsche Werkzeug** für „zu schwach“ – die echte Stellgröße ist die **Federraste** (3 Bohrungen im Sockel). 0 €, 10 min. |
| **#5 Sockel tauschen?** | ✅ **Beide Gabeln sind Alu** (NEX **und** RST Vogue) → Stifte **eingeschraubt (M8)**, Tausch möglich. Bei Stahlgabel wären sie angeschweißt → ❌ nicht selbst. |
| **#3 Hintere Bremse** ✅ | 🔴 **Merksatz: Erst am Lenker suchen, dann an der Zange.** Die **Bremshebel-Klemmschellen** waren zu nah/fest → **Pivot des hinteren Bremshebels geklemmt**. Die Belag-Theorie war falsch. |
| **#13 Vorderrad** ✅ | **Nabendynamo** – mehrere Umdrehungen frei hängend = **Sollbereich**. Nie nach Gefühl beurteilen (Magnet-Rasten täuscht), **nur nach Spiel**. |
| **#4 Hinterrad** ✅ | Lager hat sich **gesetzt/eingespielt**. Offen bleibt nur die **verlorene kleine Feder** (Wellenscheibe oder QR-Feder? → FH-M530-Explosionszeichnung). |

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
