# 🚲 Bike-Swap – Teile-Datenbank & Werkstatt-Doku

Zwei Räder, ein Frankenstein-Bike, viele offene Punkte. Dieses Repo ist das **Gedächtnis**:
Hier stehen die **korrekten Namen** aller Teile, welche **Maße** noch fehlen, was schon
**gemacht** wurde und was als Nächstes ansteht. Ziel: Nie wieder am Rad stehen und nicht
wissen, wie das Ding heißt oder welche Größe man bestellen muss.

---

## 🎯 STAND 2026-09-04 – Spenderrad identifiziert, drei Baustellen erledigt, Vorgeschichte geklärt

> 🔴 **Diese Runde hat vier Annahmen umgeworfen – und eine Tür geöffnet.**
>
> | Neu geklärt | Konsequenz |
> |---|---|
> | 🔴 **Spenderrad = Bergamont Horizon 4.0** – Prägung `52 T4/T6 Heat Treated 6061 Lite Alloy` = Alu 6061 **wärmebehandelt**, **Größe 52 cm** | Gabel, Vorderrad, Reifen, Schutzblech, Licht, Bremsarme, Vorbau und Lenker stammen **alle** von dort |
> | 🔴 **Original-Gabel des weißen Rads = RST Vogue TNL** – **sie ist noch vorhanden!** (Coil/Öl, Vorspannung + Lockout, **defekt**) | 🆕 **Baustelle #14** – wenn sie zu retten ist, erledigt sie **#1, #5 und #6 auf einen Schlag** |
> | ✅ **#3 erledigt**: hintere Bremse kehrt wieder zurück | Ursache war die **Bremshebel-Klemmung am Lenker** (zu nah/fest → **Pivot geklemmt**) – ⛔ **nicht** die Beläge |
> | ✅ **#4 + #13 erledigt**: Hinterrad läuft normal, Dynamo-Rad läuft mehrere Umdrehungen | nur noch **Beobachtung** |
>
> 🟢 **Entscheidung des Besitzers: die RST Vogue TNL wird instand gesetzt.** Die NEX wirkt
> in der Dämpfung *„schwammig, weich, wie Spielzeug"*, die RST ist *„eine Nummer besser"* –
> technisch plausibel: die RST hat eine **echte hydraulische Öldämpfung**, die NEX nur
> **Feder + Elastomer**. Die Bastelei für Schutzblech/Licht wird dafür in Kauf genommen.
>
> 🔴🔴 **Der nächste Schritt ist NICHT der Fingernageltest, sondern ein 5-Sekunden-Check (0 €):**
>
> | ☐ | Prüfung | ⛔ Schlechtes Ergebnis |
> |---|---|---|
> | **0a** | **Ist am RST-Schaft ein Außengewinde sichtbar?** | **glatt = Ahead-Gabel** → passt **nicht** in den Gewinderahmen → **Plan A+ entfällt** |
> | **0b** | **MAGNET an den Schaft halten** – haftet er? | **haftet nicht = Aluschaft** → ein **Quill-Vorbau spreizt einen Keil** und kann den Schaft **aufreißen** |
> | **0c** | **Vorbau-Typ des originalen XLC-Comp-Vorbaus** (A-Head = klemmt außen · Quill = Rohrstutzen + Keil) | **A-Head** → der Rahmen war nie für Gewinde gebaut |
>
> ⚠️ **Warum:** Ein **Staiger-Katalogauszug von 2007** nennt die Vogue TNL **„mit Aluschaft"**
> in einem Rad mit **A-Head semi-integriert**-Steuersatz – **dieses Rad hat aber
> Gewindesteuersatz + Quill-Vorbau.** Wahrscheinlich ein anderes Baujahr, aber
> 🔴 **prüfen, nicht annehmen.** Ein Kühlschrankmagnet genügt.
>
> 💡 **Erst danach: Fingernageltest an den RST-Standrohren (5 min, 0 €).**
> Keine Grübchen → Dichtungen (**14,28 €**) + Öl → Gabel zurückbauen → drei Baustellen weg.
> Grübchen → Gabel unrettbar → Plan B (NEX 225 mm oder Ahead-Umbau).
> → [`04-diagnose/rst-vogue-tnl-federgabel.md`](04-diagnose/rst-vogue-tnl-federgabel.md) **Abs. 3.0**

**Die entschlüsselten Teile:**

| Baugruppe | Identifikation |
|---|---|
| **Gabel (jetzt verbaut)** | ⛔ SR Suntour **NEX** · `SF14 NEX P 700C TS T63` · 700C, **63 mm Federweg**, Gewindeschaft **1⅛″ × 24 tpi**, Schaft **210/225 mm**, **Alu**-Scheiden – **Bergamont-Originalteil** |
| **Gabel (Original weißes Rad)** | 🔴 **RST Vogue TNL** · Coil/Öl · **Öldämpfung rechts, Stahlfeder + MCU links** · **hydraulischer Lockout** · Schaft CroMo **28,6 mm (1⅛″)** oder 25,4 mm (1″) · Standrohre **25,4 mm Stahl, Ti-Farbe** · ca. **50 mm** Federweg · **ausgebaut, vorhanden, defekt** |
| **Spenderrad-Rahmen** | ✅ **Bergamont Horizon 4.0** · `52 T4/T6 Heat Treated 6061 Lite Alloy` · Alu 6061 T4/T6 · **52 cm** · 3×8 · ca. 2012–2016 |
| **Antrieb** | Kurbelgarnitur **FC-M530** (Hollowtech, **Octalink**, 170 mm) · Innenlager **BB-ES25** · Kette **CN-HG53** (9-fach) · Schaltwerk **RD-M511** (SGS, max. 34 Z.) · Umwerfer ⛔ **FD-C050 – NICHT original** (Behelfsreparatur nach Sturz; original wäre **Deore FD-M530**) · Schalthebel **SL-M580** |
| **Bremsen** | Bremshebel **BL-M571** (V-Brake, long pull) · hinten **Shimano Deore**-Arme · vorne **Tektro**-Arme · Beläge **Tektro 836** (63 mm, Codes **B1/B44** = vermutlich Chargennummer) · 🔴 **Originalbeläge = Shimano ca. 72 mm, durchgefahren** |
| **Laufräder** | vorne ⛔ **vom Spenderrad**: Nabe **DH-3N31-NT** (Nabendynamo 6 V/3 W) + Felge **Shining A-M4** 622 × 19 + **Schwalbe Active Line K-Guard 42-622** · hinten ✅ **original**: Nabe **FH-M530** + Felge **Mach1 210** 622 × 19c + **Schwalbe Marathon Plus 47-622** |

📄 **Alle Details:** [`01-bikes/weisses-trekkingbike.md`](01-bikes/weisses-trekkingbike.md) ·
[`01-bikes/schwarzes-spenderrad.md`](01-bikes/schwarzes-spenderrad.md) ·
[`06-logbuch/2026-09-04-korrektur-runde.md`](06-logbuch/2026-09-04-korrektur-runde.md)

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
| 🔴 **Verstehen, warum dieses Rad vom Katalog abweicht** | [`06-logbuch/2026-09-04-vorgeschichte-haendlerfreund.md`](06-logbuch/2026-09-04-vorgeschichte-haendlerfreund.md) |
| Wissen, welche Baustelle welche Nummer hat | [`03-todos/offene-baustellen.md`](03-todos/offene-baustellen.md) – **maßgeblich** |
| Alles auf einmal ausdrucken | `python3 tools/generate-print-sheet.py` |

---

## 🚴 Die beiden Räder

| Arbeitsname | Beschreibung | Rolle | Stammdaten |
|---|---|---|---|
| **Weißes Trekkingbike** | ✅ **STAIGER Daytona Sportline** (Stuttgart/Gerlingen, später Winora-Staiger) · Rahmen-Nr. **AWO7230329** · **Alu 6061** · 3×9 (27 Gänge) **Shimano Deore** + 🔴 **Deore-LX-Cockpit** (FC-M530, RD-M511, **SL-M580**, **BL-M571**) · **V-Brake** · **Nabendynamo DH-3N31** · Gewindesteuersatz → jetzt mit schwarzer **Suntour NEX**-Gabel · 🔴 **Cockpit = Spezialwunsch des Händler-Freundes** | **Hauptbike / Zielrad** | [`01-bikes/weisses-trekkingbike.md`](01-bikes/weisses-trekkingbike.md) |
| **Schwarzes Spenderrad** | ✅ **BERGAMONT Horizon 4.0** (Hamburg, **seit 2015 Scott-Gruppe**) · Rahmenprägung **`52 T4/T6 Heat Treated 6061 Lite Alloy`** = Alu 6061 T4/T6, **Größe 52 cm** · 3×8 · **V-Brake** · Nabendynamo **DH-3N31** · **Suntour NEX DS 63 mm** · ca. 2012–2016 | **Teileträger** | [`01-bikes/schwarzes-spenderrad.md`](01-bikes/schwarzes-spenderrad.md) |

> ✅ **Modell geklärt: STAIGER Daytona Sportline.** Baujahr: ❓ **Hypothese 2007, KW 23**
> (aus `AWO` + `7 23` + `0329`) – passt zur Komponenten-Ära (Deore LX M570/M580 ≈ 2004–2008).
>
> 🔴 **Prospekt ≠ dein Rad – jetzt mit Beleg und mit DREI Gründen.**
> Ein **Staiger-Katalogauszug von 2007** (Sport Line) wurde Zeile für Zeile mit dem
> Ist-Bestand abgeglichen →
> [`06-logbuch/2026-09-04-vorgeschichte-haendlerfreund.md`](06-logbuch/2026-09-04-vorgeschichte-haendlerfreund.md)
>
> | Grund | Befund |
> |---|---|
> | **1 – Baujahr/Variante** | Andere Serien-Recherche nennt eine **Suntour NCX-D LO 63 mm**-Gabel; der **Katalog 2007** nennt dagegen **RST Vogue TNL** ✅ = **dein Rad**. Und: der Katalog nennt **„A-Head semi-integriert"** – **dein Rad hat Gewindesteuersatz + Quill-Vorbau** → 🔴 **anderes Baujahr** |
> | **2 – Spezialwünsche des Händlers** | ✅ **BELEGT.** Zehn Bauteile = **exakt Daytona-Spec**. **Genau zwei** weichen ab – **beide zum teureren Idaho-Spec, beide am Lenker**: Schalthebel **SL-M580** + Bremshebel **BL-M571** (**Deore LX**). Der Besitzer erinnerte **„es ging um die Schaltarmaturen"** → 🔴 **Treffer.** Ein **Upgrade**, kein Mangel |
> | **3 – Umbauten über die Jahre** | ⛔ **Umwerfer FD-C050 ist NICHT original** (Behelf nach einem Sturz, original wäre **Deore FD-M530**) · Anbauten (Schutzblech/Träger/Licht) kamen später · zuletzt der **Teile-Swap** vom Bergamont |
>
> ✅ **Zusätzlich bestätigt der Katalog deine Erinnerung:** Gepäckträger und Ständer
> **„nachrüstbar"**, **keine Beleuchtung** gelistet → *„relativ nackt gekauft"* ✔.
> Und der Herren-Sattel war ein **Fizi:k Pave Sport** – schmal und hart → *„Sado-Maso-Foltergerät"* ✔.
> 🔴 **Lehre: Immer die Teile am Rad zählen, nicht den Prospekt.**
> Siehe [`01-bikes/README.md`](01-bikes/README.md) und
> [`02-teile/00-teil-identifizieren.md`](02-teile/00-teil-identifizieren.md) Abs. 4a

> ℹ️ **Marken-Hintergrund (nicht verwechseln):** **Staiger** – Stuttgart 1898/99, ab 1997
> Winora-Staiger, **seit 2002 Accell**. **Bergamont** – Hamburg 1993, 2008 BMC,
> **seit 2015 Scott-Gruppe**. ⛔ Bergamont gehört **nicht** zu Accell.

### Was von welchem Rad stammt (aktuelle Mischkonfiguration)

| Position | Bauteil | Herkunft |
|---|---|---|
| Lenker | **Bremshebel** (die „Armaturen“) | ✅ **weiß** – **Shimano BL-M571** (original, gut) |
| Lenker | Schalthebel | ✅ **weiß** – **Shimano SL-M580** (original) |
| Lenker | Lenker + Griffe | ⚠️ **schwarz** – **Bergamont-Riser** (Serie: 30–33° Backsweep, breiter) – Original war **XLC Comp** Flatbar |
| Lenker | Vorbau | ⚠️ **schwarz** – **Bergamont BGM-Vario-Quill**, winkelverstellbar, Faceplate, **über dem Steuersatz länger** als der Staiger-Originalvorbau |
| Lenker | **Bremshebel** (die „Armaturen“) | ✅ **weiß** – **BL-M571** · 🔴 **Klemmschellen nicht zu nah/fest!** (→ Baustelle #3) |
| Vorne | Gabel | ⚠️ **schwarz** – **SR Suntour NEX SF14 … TS T63** (**Bergamont-Teil**, Schaft zu kurz → 🔴 Gewinde-Problem) |
| Vorne | 🔴 **Original-Gabel** | **RST Vogue TNL** – **ausgebaut, vorhanden, defekt** → **Baustelle #14** |
| Vorne | Laufrad | ⚠️ **komplett vom Spenderrad**: **Nabendynamo Shimano DH-3N31** + Felge **Shining A-M4** + **Schwalbe Active Line 42-622** |
| Vorne | **Bremsarme** | ⚠️ **schwarz – Tektro** (die weißen **Deore**-Arme passten nicht: **Cantistifte zu kurz**) |
| Vorne | Schutzblech + Licht | ⚠️ **vom Spenderrad** |
| Hinten | Laufrad + Kassette | ✅ **weiß** (original, 9-fach) – Nabe **FH-M530** + Felge **Mach1 210** + **Marathon Plus 47-622** |
| Hinten | **Bremsarme** | ✅ **weiß – Shimano Deore** (original, gut) |
| Hinten | **Bremsbeläge** | 🟡 **schwarz – Tektro 836, 63 mm** → **ca. 9–10 mm kürzer** als die Originalbeläge (**72 mm**, durchgefahren). **Kein Sicherheitsproblem** |
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
   Gabelschaft. 🔴 **Verschärft:** das Staiger-Steuerrohr ist **20–30 mm länger** als das
   Bergamont-Steuerrohr, und der **Bergamont-Vorbau ist über dem Steuersatz länger** → er
   **braucht mehr Schaft**. → [`02-teile/20-steuersatz-gabel-vorbau-lenker.md`](02-teile/20-steuersatz-gabel-vorbau-lenker.md) **Abs. 3b**
2. **Steuersatz-Gewinde** – oben stehen nur noch 1–2 Gewindegänge über, es gibt aktuell
   **keine echte Kontermutter**, nur Mutter + Loctite. Das ist ein **Provisorium**.
   🔴 **Ursache jetzt vollständig bekannt:** Der NEX-Gewindeschaft hat ab Werk nur **ca. 55 mm
   Gewinde oben** und wurde für das **20–30 mm kürzere** Bergamont-Steuerrohr **gekürzt**.
   → [`02-teile/20-steuersatz-gabel-vorbau-lenker.md`](02-teile/20-steuersatz-gabel-vorbau-lenker.md) **Abschnitt 3a + 3b**
3. **Felgen-Bremsflanken** – am weißen Rad waren sie abgefahren; das **Original-Hinterrad
   wurde wieder eingebaut**. Abgefahrene Bremsflanke = Risiko Felgenbruch/Platzer beim Bremsen.
   🔴 **Verschärft durch einen neuen Befund:** die **Original-Bremsbeläge (ca. 72 mm) waren
   komplett durchgefahren** – wer Beläge durchfährt, fährt meist auch die Felgenflanke an.
   ⛔ Die alte Vermutung „scharfe Felgenkante = Ursache der nicht zurückkehrenden Bremse" ist
   **hinfällig** (Baustelle #3 war die Bremshebel-Klemmung).
   → [`02-teile/30-laufrad-reifen-nabe.md`](02-teile/30-laufrad-reifen-nabe.md) Abs. 2.3
4. ✅ **Bremsfunktion hinten ist wiederhergestellt** – die Bremse kehrt zurück.
   🔴 **Aber die Ursache merken:** zu fest/zusammen angezogene **Bremshebel-Klemmschellen**
   klemmen den **Angelpunkt (Pivot)** des Hebels. Alu-Lenker: **4–6 Nm**, Klemmungen **mit
   Abstand**, Griffweite **vor** dem Festziehen einstellen.
   → [`04-diagnose/hintere-bremse-kehrt-nicht-zurueck.md`](04-diagnose/hintere-bremse-kehrt-nicht-zurueck.md)
5. **Kette ist ~½–1 Glied kürzer** als Soll. Große Gänge vorne + hinten (**Big-Big**) können
   das Schaltwerk überstrecken → **diese Kombination vermeiden**, bis neue Kette da ist.
   → [`02-teile/10-antrieb-schaltung-kette.md`](02-teile/10-antrieb-schaltung-kette.md)

---

## 📋 Offene Baustellen (Priorität – korrigiert nach Rückfrage)

| # | Baustelle | Prio | Diagnose-Status |
|---|---|---|---|
| **14** | 🆕🔴 **RST Vogue TNL retten?** – Original-Gabel vorhanden, Öl ausgetreten, Rost an den Standrohren | 🔴 **höchste – hat Vorrang** | 🟢 **Entscheidung: retten.** 🔴🔴 **Erst Schritt 0: MAGNET + Gewinde am Schaft** → [`04-diagnose/rst-vogue-tnl-federgabel.md`](04-diagnose/rst-vogue-tnl-federgabel.md) **Abs. 3.0** |
| **15** | 🆕🔴 **Schaltauge prüfen** – Folge eines Sturzes vor Jahren („hinten verbogen", behoben wurde aber **vorne**) | 🟡 mittel | 🔴 neu, ungeprüft → [`06-logbuch/2026-09-04-vorgeschichte-haendlerfreund.md`](06-logbuch/2026-09-04-vorgeschichte-haendlerfreund.md) Abs. 5 |
| 1 | **Quill-Vorbau-Einstecktiefe prüfen** (Bruchgefahr) – 🔴 verschärft durch 20–30 mm Steuerrohr-Δ | 🔴 hoch | ungeprüft → [`02-teile/20-steuersatz-gabel-vorbau-lenker.md`](02-teile/20-steuersatz-gabel-vorbau-lenker.md) **Abs. 3b** |
| 2 | **Felgen-Bremsflanken-Verschleiß prüfen** (v + h) – 🔴 Originalbeläge waren **durchgefahren** | 🔴 hoch | [`02-teile/30-laufrad-reifen-nabe.md`](02-teile/30-laufrad-reifen-nabe.md) Abs. 2.3 |
| 6 | Steuersatz-Gewinde – 🔴 **Ursache vollständig bekannt** (NEX-Schaft für ein 20–30 mm kürzeres Rohr gekürzt) | 🔴 hoch (sicherheitsrelevant) | [`02-teile/20-steuersatz-gabel-vorbau-lenker.md`](02-teile/20-steuersatz-gabel-vorbau-lenker.md) **Abs. 3a + 3b** |
| 5 | **Vordere Bremsarme passen nicht** – 🔴 **Ursache korrigiert: Cantistifte sind KÜRZER** → **längere M8-Stifte** (CS-M8-VA, 14,90 €/Paar). ⛔ **Nicht zurückdrehen!** | 🔴 hoch | [`04-diagnose/vordere-bremsarme-sockel.md`](04-diagnose/vordere-bremsarme-sockel.md) |
| 7 | Neue Kette – ✅ **exakte Spec: Shimano CN-HG53, 9-fach** | 🟡 mittel | [`02-teile/10-antrieb-schaltung-kette.md`](02-teile/10-antrieb-schaltung-kette.md) |
| 3a | 🟡 **Hintere Beläge 9–10 mm kürzer** als die Originalbeläge (72 mm) – Qualitäts-, kein Sicherheitsproblem | 🟡 mittel | [`04-diagnose/hintere-bremse-kehrt-nicht-zurueck.md`](04-diagnose/hintere-bremse-kehrt-nicht-zurueck.md) Abs. 0a |
| 4a | 🟡 **Verlorene Feder** am Hinterrad (Wellenscheibe oder QR-Feder?) | 🟡 mittel | [`04-diagnose/hinterrad-lager-feder.md`](04-diagnose/hinterrad-lager-feder.md) |
| 12 | Testfahrt + Gesamtcheck | 🟡 mittel | [`03-todos/sicherheitscheck.md`](03-todos/sicherheitscheck.md) |
| 10 | Teile identifizieren – ✅ **~95 % erledigt** | 🟢 niedrig | [`04-messdaten/messdatenblatt.md`](04-messdaten/messdatenblatt.md) |
| 11 | Kassette vom Spenderrad lösen (optional) | 🟢 niedrig | 💡 **Kettenpeitsche fehlte vermutlich** – [`02-teile/10-antrieb-schaltung-kette.md`](02-teile/10-antrieb-schaltung-kette.md) Abs. 4 |
| 8 | Ständer-Winkel zu schräg | 🟢 niedrig | [`02-teile/70-staender-gepaecktraeger.md`](02-teile/70-staender-gepaecktraeger.md) |
| 9 | Lenker-Ergonomie / Sitzposition – ⚠️ **Begründung korrigiert** (Original-Gabel war **RST 50 mm**, nicht Suntour 63 mm) | 🟢 niedrig | [`02-teile/20-steuersatz-gabel-vorbau-lenker.md`](02-teile/20-steuersatz-gabel-vorbau-lenker.md) |
| ✅ **3** | ~~Hintere Bremse kehrt nicht zurück~~ | 🟢 **ERLEDIGT** | Ursache: **Bremshebel-Klemmschellen zu nah/fest am Lenker** → **Pivot geklemmt**. ⛔ **nicht** die Beläge |
| ✅ **4** | ~~Hinterrad schwerer laufend~~ | 🟢 **ERLEDIGT** | *„läuft normal, hat sich wohl eingespielt"* – Nachkontrolle nach ca. 100 km |
| ✅ **13** | ~~Nabendynamo-Lagervorspannung~~ | 🟢 **ERLEDIGT** | Rad läuft **mehrere Umdrehungen** nach = **Sollbereich** für ein Nabendynamo-Rad |

Vollständige Liste inkl. Zwischenstatus: [`03-todos/offene-baustellen.md`](03-todos/offene-baustellen.md)

### 💡💡 Eine Maßnahme löst **vier** Baustellen

Baustelle **1** (Einstecktiefe), **5** (Bremssockel), **6** (Gewinde) und **14** (Gabel defekt)
haben dieselbe Wurzel: **die fremde Bergamont-Gabel in einem Staiger-Rahmen mit 20–30 mm
längerem Steuerrohr**.

| Weg | Was | 💰 | Bewertung |
|---|---|---|---|
| **A+** ⭐ | 🔴 **RST Vogue TNL zurückbauen** – die **Original-Gabel ist vorhanden**, für **dieses** Steuerrohr gebaut | **25–50 €** (Dichtungen 14,28 € + Öl + Politur) | ✅✅ **beste Lösung** – löst **1 + 5 + 6 + Höhenproblem**. Bedingung: **Fingernageltest** |
| **A0** | **Neue NEX-Gabel mit 225-mm-Schaft** + **längere M8-Cantistifte** | 65–105 € | ⚠️ Plan B: **+15 mm** reicht bei 20–30 mm Δ **allein nicht** |
| **C** | 🔴 **Ahead-Umbau** (NEX Ahead 255 mm + Ahead-Steuersatz EC34 + Ahead-Vorbau) – 💡 die **EC34-Lagerschalen bleiben im Rahmen!** | 70–130 € | ✅ dauerhafteste Lösung |
| **E** | 🟢 **Riser-Lenker** mit mehr Rise + Staiger-Originalvorbau | 20–40 € | ✅ billigste **Höhen**-Lösung |
| ⛔ | ~~Quill-Vorbau kürzen~~ | – | ⛔ **niemals** – schwächt den Schaft, Bruchgefahr |

✅ **Die Frage „Ist die alte weiße Gabel noch vorhanden?" ist beantwortet: JA – eine RST Vogue TNL.**
🔴 **Die nächste Frage: Besteht sie den Fingernageltest?**
Bei Weg A+ müsste man nur die **Schutzblech-Befestigung vorne** neu lösen
(Universal-/P-Schellen, 💰 3–8 €) – die Ösen der NEX entfallen dann.

### 🔴 Die korrigierte Diagnose für Baustelle 5

⛔ **Zurückgezogen (2026-09-04):** „Der Sockel-**Bund** ist **länger** (5,6 mm) als die
Ausnehmung im Deore-Arm (4,3 mm) → Sockel **2–2,5 mm zurückdrehen**."
**Diese Richtung war falsch** – Zurückdrehen würde das Problem **verschlimmern**.

| Maß | ✅ korrigierter Wert |
|---|---|
| Cantistift-Ø gemessen | **7,95 mm = M8** |
| Gabelmaterial | ✅ **beide Alu** (NEX **und** RST Vogue) → Stifte **eingeschraubt**, tauschbar |
| Stiftlänge NEX vs. RST | 🔴 **NEX kürzer** |
| → Folge | Die **M6-Befestigungsschraube** des Shimano-Bremsarms findet **keinen ausreichenden Gewindegriff** im Stift → Arm hat Spiel / lässt sich nicht festziehen |

🎯 **Fix: längere M8-Cantistifte** – **brake-stuff.de CS-M8-VA, 14,90 €/Paar**
(M8, Ø8, **M6-Innengewinde**, **Einschraublänge 10 mm**, **5–6 Nm**, **listet ausdrücklich
Staiger**). Alternative **CS-M8-RST** 16 € (verlängertes Gewinde + Zusatzflansch).
Oder: **kürzere M6-Armschraube**, oder die **Stifte der RST-Gabel übernehmen**.
Montage: reinigen/entfetten, **Loctite 243**, **5–6 Nm**, **2–3 h warten**.
🔴 **Gesamtlänge vorher mit dem Datenblatt-PDF vergleichen!**

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
- Bremsbeläge hinten getauscht (weiße waren **durchgefahren**, ca. **72 mm**) → 🟡 jetzt **Tektro 836, 63 mm**
- ✅ **Hintere Bremse wieder gangbar gemacht** – Bremshebel-Klemmschellen am Lenker nachgesetzt (Baustelle #3)
- ✅ **Hinterrad läuft normal** (Lager hat sich eingespielt, Baustelle #4)
- ✅ **Nabendynamo-Lager eingestellt** – Rad läuft mehrere Umdrehungen nach (Baustelle #13)
- ✅ **Spenderrad identifiziert**: Bergamont Horizon 4.0 · **Original-Gabel gefunden**: RST Vogue TNL

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
