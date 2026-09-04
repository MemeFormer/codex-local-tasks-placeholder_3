# 📓 Logbuch

Was wurde wann gemacht. Kurz halten – drei Sätze pro Eintrag reichen.
Wichtig ist, dass man später nachvollziehen kann, **warum** etwas so ist, wie es ist.

## Aufbau

- Ein Datei pro Session: `YYYY-MM-DD-kurzbeschreibung.md`
- Vorlage: [`../templates/logbuch-eintrag-template.md`](../templates/logbuch-eintrag-template.md)
- Zusätzlich: Kurzeintrag in die Tabelle unten

## Index

| Datum | Session | Ergebnis | Baustelle |
|---|---|---|---|
| **2026-09-04** | [🎯 Komponenten entschlüsselt](2026-09-04-komponenten-entschluesselt.md) | **Alle Teilenummern dekodiert** · 🔴 **#6-Ursache gefunden**: NEX-Schaft hat nur 55 mm Gewinde, wurde gekürzt → Fix: 225-mm-Schaft oder Ahead-Umbau · 🔴 **#5-Ursache gefunden**: Sockel-Bund 5,6 mm vs. Deore-Arm 4,3 mm, Gabel ist Alu → Sockel 2–2,5 mm zurückdrehen (0 €!) · 🔴 **#3 belegt**: Tektro 836 = 63 mm in einer 70-mm-Deore-Zange · 🟠 **#13 wieder offen**: Nabendynamo-Lagervorspannung (nur links, nach Spiel) · 🟢 **#9 entwarnt**: original Daytona hatte Suntour 63 mm | #3 #5 #6 #7 #9 #13 |
| **2026-09-03** | [Rückfrage: drei Diagnosen korrigiert](2026-09-03-rueckfrage-korrekturen.md) | Nabendynamo bestätigt (#13 entwarnt) · V-Brake bestätigt · STAIGER · „Bremshebel“ waren **Bremsarme** → Federraste ist die Lösung · hintere Beläge sind Hauptverdacht für #3 | #3 #5 #6 #13 |
| **2026-09-02** | [Bestandsaufnahme & Doku aufgebaut](2026-09-02-bestandsaufnahme.md) | Repo-Struktur, Glossar, Baugruppen, Diagnosen, Anleitungen | alle |
| ❓ | Kettenreparatur | Kette mit Fremdschloss geflickt, Stift aus Außenlasche gedrückt → Kette ~½–1 Glied kürzer | → #8 |
| ❓ | Gabel- & Steuersatztausch | Schwarze Gewindegabel in weißen Rahmen, Quill-Vorbau übernommen, Steuersatz eingestellt | → #5 |
| ❓ | Vorbau / Lenker | winkelverstellbarer Vorbau mit Faceplate montiert | → #7 |
| ❓ | Schutzbleche | Metall-Schutzbleche montiert, streifenfrei | ✅ |
| ❓ | Lichtkabel | Flachstecker aus dem Rahmen geangelt, neu gelötet, verlegt | ✅ |
| ❓ | Hinterrad-Versuch | Kassette ließ sich nicht lösen → Original-Hinterrad zurück eingebaut | → #11 |
| ❓ | Zusammenbau + Test | Rad fahrbereit, Licht funktioniert, Schaltung läuft | ✅ |
| | | | |

> ⚠️ **Datumsangaben bitte ergänzen**, soweit erinnerlich (auch ungefähr: „ca. Woche XY“).
> Ohne Datumsangabe ist das Logbuch halb so nützlich.

## Offene Fragen aus den Sessions

| Datum | Frage | beantwortet? |
|---|---|---|
| ❓ | Warum ließ sich die Kassette nicht lösen? (💡 Vermutung: keine Kettenpeitsche) | ☐ |
| ❓ | Was war die verlorene kleine Feder? | ☐ |
| ✅ | ~~Welche Bremshebel sind montiert?~~ → **beide original weiß**; die „schwarzen Hebel“ waren die **Bremsarme vorne** | ☑ |
| ✅ | ~~Ist das Vorderrad ein Nabendynamo?~~ → **ja** | ☑ |
| ✅ | ~~Marke des weißen Rads?~~ → **STAIGER** | ☑ |
| 🔴 | **Ist die alte weiße Gabel noch vorhanden?** (löst Baustelle #5 + #6 gleichzeitig) | ☐ |
| ✅ | ~~Magnet-Test Gabel: Stahl oder Alu?~~ → ✅ **ALU** (SR Suntour NEX) → Bremssockel ist **eingeschraubt** und zurückdrehbar | ☑ |
| ✅ | ~~Modell des weißen STAIGER-Rads?~~ → ✅ **Daytona Sportline**, Rahmen-Nr. **AWO7230329** | ☑ |
| ✅ | ~~Welche Bremshebel?~~ → ✅ **Shimano BL-M571**, beide original weiß | ☑ |
| ✅ | ~~Warum passen die weißen Bremsarme vorne nicht?~~ → ✅ **Sockel-Bund ca. 5,6 mm vs. Deore-Arm-Ausnehmung ca. 4,3 mm** | ☑ |
| ✅ | ~~Warum ist das Gewinde zu kurz?~~ → ✅ **NEX-Schaft hat ab Werk nur ca. 55 mm Gewinde oben; er wurde für das kürzere Spender-Steuerrohr gekürzt** | ☑ |
| ✅ | ~~Welche Kette gehört rein?~~ → ✅ **Shimano CN-HG53, 9-fach** (Original-Spec zum FC-M530) | ☑ |
| 🔴 | **Steuerrohrlänge STAIGER** (mm) – entscheidet zwischen 225-mm-Schaft und Ahead-Umbau | ☐ |
| 🔴 | **Kassetten-Modell + Abstufung** (max. 34 Zähne wg. RD-M511) | ☐ |
| 🔴 | **Kettenblatt-Zähne** (48-36-26 oder 44-32-22?) | ☐ |
| 🔴 | **Sattelstützen-Ø unter der Klemme neu ablesen** (original Daytona = XLC Comp **27,2 mm**; „31,35 mm AD" ist vermutlich Sitzrohr/Klemme) | ☐ |
| 🔴 | **Crown-race-Sitz** der NEX-Gabel: 26,4 oder 30 mm? | ☐ |
| ❓ | Marke/Modell des Spenderrads? | ☐ |
| ❓ | Bremszangen-Modellnummern (vorne Tektro ❓, hinten Deore ❓) | ☐ |
| ❓ | Pedal-Modell | ☐ |
