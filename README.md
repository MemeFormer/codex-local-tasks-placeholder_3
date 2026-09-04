# 🚲 Bike-Swap – Teile-Datenbank & Werkstatt-Doku

Zwei Räder, ein Frankenstein-Bike, viele offene Punkte. Dieses Repo ist das **Gedächtnis**:
Hier stehen die **korrekten Namen** aller Teile, welche **Maße** noch fehlen, was schon
**gemacht** wurde und was als Nächstes ansteht. Ziel: Nie wieder am Rad stehen und nicht
wissen, wie das Ding heißt oder welche Größe man bestellen muss.

---

## 🎯 STAND 2026-09-04 – Teilenummern entschlüsselt

> **Fast alle Komponenten sind jetzt exakt identifiziert** – und drei Baustellen haben
> dadurch eine **konkrete Ursache** plus **exakte Ersatzteil-Spec** bekommen.

| 🔴 Baustelle | Ursache (jetzt bekannt) | Fix |
|---|---|---|
| **#6 Gewinde zu kurz** | SR Suntour **NEX**-Gewindeschäfte haben ab Werk nur **ca. 55 mm Gewinde oben**. Der Schaft wurde für das **kürzere Steuerrohr des Spenderrads gekürzt** – das STAIGER-Steuerrohr ist **ca. 23 mm länger** | 🎯 **NEX-Gabel mit 225-mm-Schaft** (50–90 €) oder **Ahead-Umbau** (EC34-Schalen bleiben im Rahmen!) |
| **#5 Bremsarme passen nicht** | Sockel-**Bund ca. 5,6 mm** vs. Deore-Arm-**Ausnehmung ca. 4,3 mm** = 1,3 mm Spalt. Gabel ist **Alu** → Sockel ist **eingeschraubt** | 💡 **Sockel 2–2,5 mm zurückdrehen** + Loctite 243 – **0 €!** |
| **#3 Bremse kehrt nicht zurück** | **Tektro 836 = 63 mm** Beläge in einer **Shimano-Deore-Zange, die für 70 mm gebaut ist** (+ Tektro-Scheibensatz) | 🔴 **Shimano-Beläge 70 mm** (M70T4/S65T), 8–15 € |
| **#13 Vorderrad dreht schwer** | Nabendynamo **DH-3N31** – Rollwiderstand normal, **ABER Shimano-Dynamos sind ab Werk zu stramm** und man **kann es nicht erfühlen** (Magnet-Rasten) | 💡 **nur links, nach Spiel** einstellen – **0 €** |
| **#9 Lenker-Gefühl** | 🟢 **ENTWARNT**: das originale Staiger Daytona hatte ab Werk eine **Suntour NCX-D LO 63 mm**-Gabel. Deine **NEX T63 = 63 mm** ist zeitlich passend | beobachten |

**Die entschlüsselten Teile:**

| Baugruppe | Identifikation |
|---|---|
| **Gabel** | SR Suntour **NEX** · `SF14 NEX P 700C TS T63` · 700C, **63 mm Federweg**, Gewindeschaft **1⅛″ × 24 tpi**, Schaft **210/225 mm**, **Alu**-Scheiden |
| **Antrieb** | Kurbel **FC-M530** (Hollowtech, **Octalink**, 170 mm) · Innenlager **BB-ES25** · Kette **CN-HG53** (9-fach) · Schaltwerk **RD-M511** (SGS, max. 34 Z.) · Umwerfer **FD-C050** (Top Swing) · Schalthebel **SL-M580** |
| **Bremsen** | Bremshebel **BL-M571** (V-Brake, long pull) · hinten **Shimano Deore**-Arme · vorne **Tektro**-Arme · Beläge **Tektro 836** (63 mm) |
| **Laufräder** | vorne Nabe **DH-3N31-NT** (Nabendynamo 6 V/3 W) + Felge **Shining A-M4** 622 × 19 + **Schwalbe Active Line K-Guard 42-622** · hinten Nabe **FH-M530** + Felge **Mach1 210** 622 × 19c + **Schwalbe Marathon Plus 47-622** |

📄 **Alle Details:** [`01-bikes/weisses-trekkingbike.md`](01-bikes/weisses-trekkingbike.md) ·
[`06-logbuch/2026-09-04-komponenten-entschluesselt.md`](06-logbuch/2026-09-04-komponenten-entschluesselt.md)

---

## ⚡ Schnelleinstieg – wo steht was?

| Ich will … | Datei |
|---|---|
| Wissen, welche Baustellen offen sind | [`03-todos/offene-baustellen.md`](03-todos/offene-baustellen.md) |
| Ein Teil richtig benennen / identifizieren | [`02-teile/00-fachbegriffe-glossar.md`](02-teile/00-fachbegriffe-glossar.md) |
| Nachschlagen, was an einer Baugruppe verbaut ist | [`02-teile/`](02-teile/) → passende Baugruppe |
| Sehen, was ich kaufen/bestellen muss | [`03-todos/einkaufsliste.md`](03-todos/einkaufsliste.md) |
| Ein Maß am Rad ablesen und eintragen | [`04-messdaten/messdatenblatt.md`](04-messdaten/messdatenblatt.md) |
| Eine konkrete Anleitung (Lager einstellen, Bremse …) | [`05-anleitungen/`](05-anleitungen/) |
| Nachlesen, was ich wann gemacht habe | [`06-logbuch/`](06-logbuch/) |
| Alles auf einmal ausdrucken | `python3 tools/generate-print-sheet.py` |

---

## 🚴 Die beiden Räder

| Arbeitsname | Beschreibung | Rolle | Stammdaten |
|---|---|---|---|
| **Weißes Trekkingbike** | ✅ **STAIGER Daytona Sportline** (Stuttgart/Gerlingen, später Winora-Staiger) · Rahmen-Nr. **AWO7230329** · **Alu 6061** · 3×9 (27 Gänge) **Shimano Deore/LX** (FC-M530, RD-M511, SL-M580, BL-M571) · **V-Brake** · **Nabendynamo DH-3N31** · Gewindesteuersatz → jetzt mit schwarzer **Suntour NEX**-Gabel | **Hauptbike / Zielrad** | [`01-bikes/weisses-trekkingbike.md`](01-bikes/weisses-trekkingbike.md) |
| **Schwarzes Spenderrad** | ❓ deutsche Marke (muss noch nachgeschaut werden) · 3×8 · Metall-Schutzbleche · winkelverstellbarer Vorbau · Felge + City-Reifen · Gabel · Bremsarme vorne | **Teileträger** | [`01-bikes/schwarzes-spenderrad.md`](01-bikes/schwarzes-spenderrad.md) |

> ✅ **Modell geklärt: STAIGER Daytona Sportline.** Baujahr: ❓ **Hypothese 2007, KW 23**
> (aus `AWO` + `7 23` + `0329`) – passt zur Komponenten-Ära (Deore LX M570/M580 ≈ 2004–2008).
> Das originale Daytona hatte ab Werk: **Suntour NCX-D LO 63 mm**-Federgabel, **Mach1 210**-Felgen,
> **XLC Comp**-Vorbau/-Sattelstütze/-Griffe, **Shimano Deore V-Brakes**, **Schwalbe Marathon 37-622**.
> Siehe [`01-bikes/README.md`](01-bikes/README.md).

### Was von welchem Rad stammt (aktuelle Mischkonfiguration)

| Position | Bauteil | Herkunft |
|---|---|---|
| Lenker | **Bremshebel** (die „Armaturen“) | ✅ **weiß** – **Shimano BL-M571** (original, gut) |
| Lenker | Schalthebel | ✅ **weiß** – **Shimano SL-M580** (original) |
| Lenker | Lenker + Griffe | ⚠️ **schwarz** (breiter, geschwungener) – Original war **XLC Comp** Flatbar |
| Lenker | Vorbau | ⚠️ **schwarz** (Quill, winkelverstellbar, Faceplate) |
| Vorne | Gabel | ⚠️ **schwarz** – **SR Suntour NEX SF14 … TS T63** (Schaft zu kurz → 🔴 Gewinde-Problem) |
| Vorne | Laufrad | ✅ **Nabendynamo Shimano DH-3N31** + Felge **Shining A-M4** + **Schwalbe Active Line 42-622** |
| Vorne | **Bremsarme** | ⚠️ **schwarz – Tektro** (die weißen **Deore**-Arme passten nicht auf den Sockel) |
| Hinten | Laufrad + Kassette | ✅ **weiß** (original, 9-fach) – Nabe **FH-M530** + Felge **Mach1 210** + **Marathon Plus 47-622** |
| Hinten | **Bremsarme** | ✅ **weiß – Shimano Deore** (original, gut) |
| Hinten | **Bremsbeläge** | 🔴 **schwarz – Tektro 836, 63 mm** → **7–10 mm zu kurz** für die Deore-Zange! |
| Antrieb | Kurbelgarnitur | ✅ **Shimano FC-M530**, Hollowtech, Octalink, 170 mm |
| Antrieb | Umwerfer (vorne) | ✅ **Shimano FD-C050**, Top Swing |
| Antrieb | Schaltwerk (hinten) | ✅ **Shimano RD-M511**, 9-fach, SGS |
| Antrieb | Kette | ⚠️ repariert, zu kurz → Neukauf **Shimano CN-HG53** |
| Beide | Schutzbleche (Metall, V-Streben) | ⚠️ **schwarz** |
| Beide | Lichtkabel | ✅ neu gelötet, am weißen Rad verlegt |

---

## 🔴 Sicherheitsrelevant (bitte zuerst prüfen)

1. **Quill-Vorbau-Einstecktiefe** 🔴 Wenn der Gabelschaft nur 1–2 Gewindegänge übersteht,
   könnte der Schaftvorbau **nicht tief genug** eingesteckt sein. Die
   „MIN INSERTION“-Markierung darf **nicht sichtbar** sein – sonst bricht bei Belastung der
   Gabelschaft. → [`02-teile/20-steuersatz-gabel-vorbau-lenker.md`](02-teile/20-steuersatz-gabel-vorbau-lenker.md)
2. **Steuersatz-Gewinde** – oben stehen nur noch 1–2 Gewindegänge über, es gibt aktuell
   **keine echte Kontermutter**, nur Mutter + Loctite. Das ist ein **Provisorium**.
   🔴 **Ursache jetzt bekannt:** Der NEX-Gewindeschaft hat ab Werk nur **ca. 55 mm Gewinde
   oben** und wurde für das kürzere Spender-Steuerrohr **gekürzt**.
   → [`02-teile/20-steuersatz-gabel-vorbau-lenker.md`](02-teile/20-steuersatz-gabel-vorbau-lenker.md) **Abschnitt 3a**
3. **Felgen-Bremsflanken** – am weißen Rad waren sie abgefahren; das **Original-Hinterrad
   wurde wieder eingebaut**. Abgefahrene Bremsflanke = Risiko Felgenbruch/Platzer beim Bremsen.
   **Und:** eine scharfe Felgenkante ist ein Hauptverdächtiger für die nicht zurückkehrende
   hintere Bremse. → [`02-teile/30-laufrad-reifen-nabe.md`](02-teile/30-laufrad-reifen-nabe.md)
4. **Bremsfunktion hinten** kehrt nicht selbstständig zurück. Solange das so ist:
   defensive Fahrweise, vorausschauend bremsen, keine langen Bergabfahrten.
   → [`04-diagnose/hintere-bremse-kehrt-nicht-zurueck.md`](04-diagnose/hintere-bremse-kehrt-nicht-zurueck.md)
5. **Kette ist ~½–1 Glied kürzer** als Soll. Große Gänge vorne + hinten (**Big-Big**) können
   das Schaltwerk überstrecken → **diese Kombination vermeiden**, bis neue Kette da ist.
   → [`02-teile/10-antrieb-schaltung-kette.md`](02-teile/10-antrieb-schaltung-kette.md)

---

## 📋 Offene Baustellen (Priorität – korrigiert nach Rückfrage)

| # | Baustelle | Prio | Diagnose-Status |
|---|---|---|---|
| 1 | **Quill-Vorbau-Einstecktiefe prüfen** (Bruchgefahr) | 🔴 hoch | ungeprüft → [`02-teile/20-steuersatz-gabel-vorbau-lenker.md`](02-teile/20-steuersatz-gabel-vorbau-lenker.md) |
| 2 | **Felgen-Bremsflanken-Verschleiß prüfen** (v + h) | 🔴 hoch | [`02-teile/30-laufrad-reifen-nabe.md`](02-teile/30-laufrad-reifen-nabe.md) Abs. 2.3 |
| 3 | **Hintere Bremse kehrt nicht zurück** – 🔴 **Ursache belegt: Tektro-836-Beläge (63 mm) in einer 70-mm-Deore-Zange** | 🔴 hoch | [`04-diagnose/hintere-bremse-kehrt-nicht-zurueck.md`](04-diagnose/hintere-bremse-kehrt-nicht-zurueck.md) |
| 4 | Hinterrad schwerer laufend (Lager zu fest + verlorene Feder) | 🔴 hoch | [`04-diagnose/hinterrad-lager-feder.md`](04-diagnose/hinterrad-lager-feder.md) |
| 5 | **Vordere Bremsarme passen nicht** – 🔴 **Ursache belegt: Sockel-Bund 5,6 mm vs. Deore-Arm 4,3 mm** → 💡 **Sockel 2–2,5 mm zurückdrehen (0 €!)** | 🟡 mittel | [`04-diagnose/vordere-bremsarme-sockel.md`](04-diagnose/vordere-bremsarme-sockel.md) |
| 6 | Steuersatz-Gewinde – 🔴 **Ursache gefunden** (NEX-Schaft gekürzt) → **225-mm-Schaft oder Ahead-Umbau** | 🔴 hoch (sicherheitsrelevant) | [`02-teile/20-steuersatz-gabel-vorbau-lenker.md`](02-teile/20-steuersatz-gabel-vorbau-lenker.md) **Abs. 3a** |
| 7 | Neue Kette – ✅ **exakte Spec: Shimano CN-HG53, 9-fach** | 🟡 mittel | [`02-teile/10-antrieb-schaltung-kette.md`](02-teile/10-antrieb-schaltung-kette.md) |
| 8 | Ständer-Winkel zu schräg | 🟢 niedrig | [`02-teile/70-staender-gepaecktraeger.md`](02-teile/70-staender-gepaecktraeger.md) |
| 9 | Lenker-Ergonomie / Sitzposition – 🟢 **entwarnt** (original Daytona hatte Suntour 63 mm) | 🟢 niedrig – erst nach 3–5 Fahrten bewerten | [`02-teile/20-steuersatz-gabel-vorbau-lenker.md`](02-teile/20-steuersatz-gabel-vorbau-lenker.md) |
| 10 | Teile identifizieren – ✅ **~90 % erledigt** | 🟢 niedrig | [`04-messdaten/messdatenblatt.md`](04-messdaten/messdatenblatt.md) |
| 11 | Kassette vom Spenderrad lösen (optional) | 🟢 niedrig | 💡 **Kettenpeitsche fehlte vermutlich** – [`02-teile/10-antrieb-schaltung-kette.md`](02-teile/10-antrieb-schaltung-kette.md) Abs. 4 |
| 13 | **Nabendynamo-Lagervorspannung** – 🟠 **wieder offen** (Shimano-Dynamos ab Werk zu stramm) | 🟡 mittel | [`04-diagnose/vorderrad-schwergaengig.md`](04-diagnose/vorderrad-schwergaengig.md) |
| 12 | Testfahrt + Gesamtcheck | 🟡 mittel | [`03-todos/sicherheitscheck.md`](03-todos/sicherheitscheck.md) |
| 🟢 | ~~Vorderrad dreht nicht frei~~ (Rollwiderstand) | 🟢 **ENTWARNT** | ✅ **Nabendynamo DH-3N31!** Von Hand nur 1–2 Umdrehungen = **normal, kein Defekt.** 🔴 Aber Lagervorspannung prüfen → Baustelle **13** |

Vollständige Liste inkl. Zwischenstatus: [`03-todos/offene-baustellen.md`](03-todos/offene-baustellen.md)

### 💡 Eine Maßnahme löst zwei Baustellen

Baustelle **5** (Bremsarme vorne passen nicht auf den Sockel) und Baustelle **6**
(zu wenig Gewinde für die Kontermutter) haben dieselbe Wurzel: **die fremde Suntour-NEX-Gabel**.

| Weg | Was | 💰 |
|---|---|---|
| **A** | 🔴 **Weiße Original-Gabel zurück** (falls noch vorhanden) | 0–10 € |
| **B** | 🎯 **Neue NEX-Gabel mit 225-mm-Schaft** + Bremssockel 2–2,5 mm zurückdrehen | 50–90 € |
| **C** | 🔴 **Ahead-Umbau** (NEX Ahead 255 mm + Ahead-Steuersatz EC34 + Ahead-Vorbau) – 💡 die **EC34-Lagerschalen bleiben im Rahmen!** | 70–130 € |

Bei Weg A müsste man nur die Schutzblech-Befestigung vorne neu lösen
(Universal-Schellen, 💰 3–8 €).
→ **Erst klären: Ist die alte weiße Gabel noch vorhanden?**

### 💡 Die 0-€-Maßnahme für Baustelle 5

🔴 **Neu (2026-09-04): Die Ursache ist jetzt exakt bekannt.**

| Maß | Wert |
|---|---|
| Länge des Sockel-**Bunds** an der Suntour-NEX-Gabel | ca. **5,6 mm** |
| Tiefe der Ausnehmung im **Shimano-Deore**-Bremsarm | ca. **4,3 mm** |
| → Spalt | ca. **1,3 mm** – der Arm liegt nicht an, „passt nicht" |

🎯 **Fix: den eingeschraubten Bremssockel 2–2,5 mm zurückdrehen** (möglich, weil die
NEX-Gabel **Alu**-Scheiden hat) + **Loctite 243**. 💰 **0 €**, ca. 30 min.

**Und für die schwachen Federn:** Die „kleinen Stellschrauben" (Federspannschrauben) haben
konstruktiv nur ±2–3 Umdrehungen Verstellweg und dienen der **Zentrierung**, nicht der
Rückstellkraft. Die **echte** Federvorspannung stellt man über die **Federraste** ein:
der kleine Federstift am Bremsarm kann in **eine von drei Bohrungen** im Bremssockel
gesetzt werden.
→ 10 Minuten, 0 €, und das ist der Punkt, der „wirklich etwas ändert“.

---

## ✅ Erledigt (Kurzfassung)

- Kette gerissen → mit altem Kettenschloss repariert, Stift aus Außenlasche gedrückt (Kette dadurch kürzer)
- Schwarze Gabel (Gewindeschaft) in weißen Rahmen umgebaut, inkl. Quill-Vorbau (Innenkeil)
- Steuersatz eingestellt: freigängig, kein axiales Spiel
- Winkelverstellbarer Vorbau + Faceplate montiert → Lenkerwechsel ohne Griffe abziehen möglich
- Metall-Schutzbleche mit V-Streben und integrierter Rücklicht-Kabelführung montiert, streifenfrei
- Rücklicht-Kabel: Flachstecker waren in den Rahmen gerutscht → **neu gelötet**, am weißen Rad verlegt
- Nabendynamo + Vorder-/Rücklicht funktionieren
- Hinterrad: **Kassette ließ sich nicht lösen** → komplettes Original-Hinterrad wieder eingebaut
- Bremsbeläge hinten getauscht (weiße waren runter) → ⚠️ **danach trat Baustelle 3 auf**

Details & Datumsangaben: [`06-logbuch/`](06-logbuch/)

---

## 🧭 Arbeitsweise mit diesem Repo

1. **Ans Rad gehen = Messen + Fotografieren.** Nicht nur schrauben. Jedes Mal, wenn du am Rad
   bist, trage offene Werte aus [`04-messdaten/messdatenblatt.md`](04-messdaten/messdatenblatt.md) ein.
2. **Foto-Regel:** jede Baugruppe mindestens 3× fotografieren – Gesamtansicht, Detail,
   **und die Beschriftung/Aufdruck auf dem Teil** (daraus ergibt sich die exakte Bezeichnung).
   Fotos **nicht** ins Repo (siehe `.gitignore`), sondern lokal ablegen und hier nur den
   Dateinamen/Pfad notieren.
3. **Teil identifiziert?** → korrekten Namen + Maße in die passende Datei unter [`02-teile/`](02-teile/) eintragen
   und die `❓ TODO`-Markierung löschen.
4. **Etwas bestellt/verbaut?** → in [`03-todos/einkaufsliste.md`](03-todos/einkaufsliste.md) abhaken und
   einen Logbuch-Eintrag machen ([Vorlage](templates/logbuch-eintrag-template.md)).
5. **Neues Teil/eine neue Baugruppe?** → [Vorlage](templates/teilegruppe-template.md) kopieren.

### Konventionen

- `❓ TODO` = Wert fehlt noch, muss am Rad gemessen/abgelesen werden
- `⚠️` = sicherheitsrelevant oder Provisorium
- `💰` = es wird etwas bestellt werden müssen
- `💡` = Erkenntnis/Tipp, der Zeit oder Geld spart
- Maße immer in **mm**, Gewinde immer als **Nenndurchmesser × Steigung** (z. B. M10 × 1,0)
- Bei Kaufteilen immer angeben: **Hersteller + Modell + Größe** (z. B. „Shimano HG40 9-fach 11-32“)

### ⚠️ Begriffe, die hier sauber getrennt werden

Am Fahrrad mit Felgenbremse gibt es **zwei verschiedene „Hebel“** – das war in der
Ursprungs-Zusammenfassung vermischt:

| Umgangssprachlich | Korrekt | Wo |
|---|---|---|
| „Bremshebel“, „Armatur“ | **Bremshebel** (brake lever) | **am Lenker** |
| „die zwei Hebel unten an der Bremse“ | **Bremsarme** (brake arms) | an Gabel / Hinterbau |
| „der Stahlstift, auf den man das aufsteckt“ | **Bremssockel / Cantisockel** (brake boss) | an Gabel / Hinterbau |
| „die kleine Stellschraube“ | **Federspannschraube** (spring tension screw) | am Bremsarm |
| „der kleine Stift hinten am Arm“ | **Federraste / Federstift** (spring retainer pin) | Bremsarm → Sockel |

→ Komplettes Glossar: [`02-teile/00-fachbegriffe-glossar.md`](02-teile/00-fachbegriffe-glossar.md)

---

## 📁 Struktur

```
.
├── README.md                     ← du bist hier
├── 01-bikes/                     Stammdaten der beiden Räder + Vorlage für weitere
├── 02-teile/                     Teileträger: eine Datei pro Baugruppe (mit Fachbegriffen)
├── 03-todos/                     offene Baustellen, Einkaufsliste, Werkzeug & Material, Sicherheitscheck
├── 04-diagnose/                  Fehlersuche: Symptom → Test → Ursache → Maßnahme
├── 04-messdaten/                 Messdatenblatt: alles, was noch am Rad abgelesen werden muss
├── 05-anleitungen/               Schritt-für-Schritt-Anleitungen + Referenzwerte
├── 06-logbuch/                   was wurde wann gemacht
├── templates/                    Vorlagen (Baugruppe, Diagnose, Messung, Logbuch)
└── tools/                        generate-print-sheet.py (alles in eine Druckdatei)
```
