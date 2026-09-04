# 🔬 Diagnose: Vordere Bremsarme – zu weich + passen nicht auf den Bremssockel

**Baustelle #5 (Ursache korrigiert 2026-09-05)** · Priorität 🔴 · Status: 🔴 **Ursache bekannt – Lösung offen**

**Symptome:**
1. Die vorderen Bremsarme (vom Spenderrad) fühlen sich **weich** an und die Federn sind
   **zu schwach**
2. Die **kleinen Stellschrauben** (Federspannschrauben) ändern **wirklich nur wenig**
3. Die **guten weißen Bremsarme passten nicht auf die Aufnahme** der schwarzen Gabel

**Situation:** Vorne sind die schwarzen Bremsarme an der schwarzen Gabel montiert, weil die
weißen nicht auf den Bremssockel passten.

> ✅ **GEKLÄRT (2026-09-04, Stand 2):**
> - Gabel = **SR Suntour NEX** `SF14 NEX P 700C TS T63` vom **Bergamont Horizon 4.0**-Spenderrad,
>   1⅛″ Gewindeschaft, **Aluminium-Tauchrohre** → die Bremssockel sind **eingeschraubt**
> - Die Bremsarme, die nicht passten, sind **Shimano Deore** (passend zur BL-M571/SL-M580-Gruppe)
> - Verbaut sind jetzt **Tektro**-Bremsarme (vom Spenderrad, das dieselbe Suntour-Gabel hatte)
> - Bremssockel-Stift: Ø **7,95 mm gemessen** → **M8**, Aufnahmedurchmesser **Ø 8 mm** (V-Brake-Norm)
>
> 🔴 **UND DIE URSACHE IST VOM BESITZER SELBST GEMESSEN (2026-09-05 bestätigt):**
> Die Bremssockel-Stifte der schwarzen Gabel sind **„ein klein wenig kürzer"** als die der
> weißen RST-Gabel → die Shimano-Deore-Arme lassen sich **nicht richtig festschrauben**.
> **Das ist ein Längenproblem, kein Spalt- oder Lackproblem.**
>
> ⛔ **Deshalb ist eine frühere Empfehlung in dieser Datei FALSCH und wurde zurückgezogen:**
> „Sockel 2–2,5 mm zurückdrehen" würde den Stift **noch kürzer** machen und das Problem
> **verschlimmern**. Siehe Abschnitt „Ursache 1 im Detail" (korrigiert).

---

## 0. 🧭 Begriffe klären (wichtig – hier gab es eine Verwechslung)

Am Fahrrad mit Felgenbremse gibt es **zwei völlig verschiedene „Hebel“**:

| Umgangssprachlich | **Korrekte Bezeichnung** | Englisch | Wo |
|---|---|---|---|
| „Bremshebel“, „Armatur“ | **Bremshebel** | brake lever | **am Lenker** |
| „die zwei Hebel unten an der Bremse“ | **Bremsarme** / Bremsschenkel | brake arms | an der Gabel/am Hinterbau |
| „die Bremse“ als Ganzes | **Bremszange** / Bremskörper | brake caliper | – |
| „der Stahlstift, auf den man das aufsteckt“ | **Bremssockel** / Cantisockel | brake boss / canti stud | an Gabel/Hinterbau |
| „die kleine Stellschraube“ | **Federspannschraube** | spring tension screw | am Bremsarm |
| „der kleine Stift auf der Rückseite“ | **Federraste / Federstift** | spring retainer pin | am Bremsarm, greift in den Sockel |
| „die Löcher im Sockel“ | **Federrasten-Bohrungen** | spring tension holes | **3 Stück** im Bremssockel |
| „die Schraube, mit der man es festmacht“ | **Bremsbefestigungsschraube** | brake mounting bolt | M6, geht in das Innengewinde des Sockels |

> ✅ **Geklärt:** Am Lenker sind **beide Bremshebel vom weißen Rad** (die guten).
> Das Problem „weiche Hebel, schwache Federn“ betrifft also die **Bremsarme vorne**,
> nicht die Bremshebel. Das ist ein ganz anderer Reparaturweg – und ein viel einfacherer.

**Aktuelle Aufteilung:**

| Position | Bremshebel (Lenker) | Bremsarme (Zange) | Beläge |
|---|---|---|---|
| **vorne** | ✅ weiß (original, gut) | ⚠️ **schwarz** (Spenderrad) | ❓ welche? |
| **hinten** | ✅ weiß (original, gut) | ✅ **weiß** (original, gut) | ⚠️ **schwarz** (Spenderrad, weil die weißen runter waren) |

---

## 💡 DIE WICHTIGSTE ERKENNTNIS ZUERST

> **Die Federspannschraube ist nicht das richtige Werkzeug für „Federn zu schwach“.**

Die Federspannschraube hat nur einen Verstellweg von ca. **±2–3 Umdrehungen** und dient
hauptsächlich der **Zentrierung** (beide Arme gleich weit von der Felge) – nicht der
Erhöhung der Gesamtrückstellkraft. Deshalb „ändert sie wirklich nur wenig“. Das ist
konstruktiv so und **kein Defekt**.

### ✅ Die echte Stellgröße: die Federraste (3 Löcher im Bremssockel)

Der kleine **Federstift** auf der Rückseite jedes Bremsarms greift in **eine von drei
Bohrungen** im Bremssockel. Jede Bohrung = eine andere Federvorspannung:

```
   Bremssockel (an der Gabel)
        ┌───────┐
        │   ○   │ ← Loch 3 = schwächste Vorspannung (Arm steht am weitesten weg…
        │   ○   │ ← Loch 2 = mittel                   …bzw. je nach Bauart umgekehrt)
        │   ○   │ ← Loch 1 = stärkste Vorspannung
        └───┬───┘
            │  ← M6-Innengewinde für die Befestigungsschraube
            │  ← der Stift, auf den der Bremsarm aufgeschoben wird
     [Bremsarm mit Feder]
            ◄─ Federstift ragt nach hinten und sitzt in einem der 3 Löcher
```

**Vorgehen:**

1. Bremsbefestigungsschraube (M6-Inbus) lösen, Bremsarm vom Sockel abziehen
2. Federspannschraube **ganz herausdrehen** (damit sie nicht im Weg ist)
3. Feder aushängen, Bremsarm wieder aufsetzen und den **Federstift in das andere Loch**
   setzen
4. **Beide Arme in dasselbe Loch** (sonst zieht die Bremse einseitig)
5. Federspannschraube wieder **mittel** positionieren und danach fein zentrieren
6. Testen: Arme von Hand zusammendrücken und loslassen → müssen **kräftig und komplett**
   zurückschnappen

**Das ist die Maßnahme, die bei „Federn zu schwach“ wirklich etwas bringt.** Aufwand: 10 min,
Kosten: 0 €.

### Weitere Möglichkeiten bei zu schwachen Federn

| Maßnahme | Aufwand | Bewertung |
|---|---|---|
| **Federraste: anderes Loch** | gering | ✅ **erste Wahl** |
| **Federn der weißen Bremsarme in die schwarzen umsetzen** | mittel | ✅ zweite Wahl – Federn von V-Brakes sind meist baugleich (gleicher Draht, gleicher Haken). Vorher vergleichen: Drahtstärke, Windungen, Hakenform |
| Feder leicht nachbiegen (nur am Hakenende, max. 10–15°) | gering | ⚠️ Notlösung, nicht am Draht biegen |
| Pivot/Bolzen des Bremsarms reinigen + dünn fetten | gering | ✅ immer machen – trockene Sockel sind eine Hauptursache für schwergängige Arme |
| Neue V-Brake kaufen (z. B. Shimano BR-T4000 / BR-MT200 V / Tektro 855AL) | gering | 💰 15–30 €, sehr günstige und gute Ersatzteile |
| **Weiße Original-Gabel zurückbauen** | hoch | 💡 siehe Abschnitt 4 – löst **beide** Probleme auf einmal |

---

## 🔍 Warum passten die weißen Bremsarme nicht auf den Sockel?

### Ursachen-Ranking

| # | Ursache | Wahrscheinlichkeit | Test | Lösung |
|---|---|---|---|---|
| **1** | 🔴🔴 **Bremssockel-Stift der schwarzen Gabel ist zu KURZ** – die M6-Befestigungsschraube des Deore-Arms findet nicht genug Gewinde, der Arm lässt sich nicht klemmen | 🔴 **BELEGT (selbst gemessen)** | Stiftlänge über dem Bund messen, **schwarze NEX-Gabel vs. weiße RST-Gabel vergleichen** | 🎯 **längere M8-Ersatz-Cantisockel** (15–16 €/Paar) **oder** Stifte der RST-Gabel umsetzen **oder** kürzere M6-Schraube |
| **2** | Unterschiedlicher **Scheibenstapel** der Bremsarme: Tektro und Shimano bauen verschieden hoch → die Schraube greift bei Shimano nicht | 🔴 hoch (erklärt, warum Tektro funktioniert!) | Scheiben/Buchsen beider Arme nebeneinander legen, **Gesamthöhe** messen | Scheibenstapel des Deore-Arms reduzieren |
| 3 | **Federstift sitzt nicht in der Bohrung**, sondern liegt auf | 🟢 erledigt – laut Besitzer über **Federn + Einstellschräubchen** gelöst | – | – |
| ~~4~~ | ~~Lack oder Rost auf dem Bremssockel~~ | 🟢 **entfällt** – kein Lackproblem | – | – |
| ~~5~~ | ~~Bund des Sockels länger als die Arm-Ausnehmung~~ | ⛔ **ZURÜCKGEZOGEN** – Fremdquelle zu einem **anderen** Symptom (Spalt statt zu kurz). Deine Messung zeigt das **Gegenteil** | – | – |
| ~~6~~ | ~~Sockel-Höhe passt nicht zur Laufradgröße~~ | 🟢 **entfällt** – Besitzer bestätigt: beide Gabeln haben die Stifte **unterhalb der Felge**, gleicher Aufbau | – | – |
| 7 | Bremsarm-Buchse ausgeschlagen / verrostet | gering | Buchse im Arm ansehen | reinigen + fetten |
| ~~8~~ | ~~Anderes Gewinde (M8 vs. M10)~~ | 🟢 **entfällt** – beide **7,95 mm = M8** | – | – |

### 🔴 Ursache 1 im Detail: Der Bremssockel-Stift ist zu kurz (korrigierte Diagnose)

> ⛔ **Korrektur in eigener Sache:** Eine frühere Fassung dieser Datei empfahl, den Sockel
> **2–2,5 mm zurückzudrehen**, weil angeblich der **Bund länger** sei als die Ausnehmung im
> Deore-Arm (Maße 5,6 mm / 4,3 mm aus einem Schrauber-Forum). **Das war auf deinen Fall
> nicht übertragbar.** Deine eigene Messung zeigt das Gegenteil: der Stift der schwarzen
> Gabel ist **kürzer**. Zurückdrehen würde ihn **noch kürzer** machen → **verschlimmern**.
> **Diese Empfehlung ist zurückgezogen.**

**Dein Befund (wörtlich):**
> *„Nur kann ich meine guten Shimano nicht auf den Boss-Stiften der schwarzen montieren, weil
> diese ein klein wenig kürzer sind, somit bekomm ich die da nicht richtig festgeschraubt.
> DESHALB habe ich ja vorne die TEKTRO-Dinger nehmen müssen."*

**Warum ein zu kurzer Stift das Festschrauben verhindert:**

```
So wird ein V-Brake-Arm gehalten:

   [Schraubenkopf] [Scheibe] | Bremsarm | [Bund/Flansch] || Gabel-Tauchrohr ||
                              |  Buchse  |      ▲
                              └──────────┘      |
                                     M6-Schraube ┘ ──► greift in das M6-Innen-
                                                        gewinde des Sockel-Stifts

Ist der Stift zu kurz:
   • die M6-Schraube findet nicht genug Gewindetiefe
   • sie setzt auf („bottoms out"), BEVOR der Arm gegen den Bund gepresst wird
   • Folge: der Arm hat Spiel, lässt sich nicht klemmen, „passt nicht"
```

**Warum die Tektro-Arme trotzdem funktionieren:** Tektro und Shimano bauen ihre Bremsarme
unterschiedlich hoch. Die **Tektro**-Arme haben vermutlich einen **kürzeren Befestigungs-**
**schraubenweg** bzw. einen anderen **Scheibenstapel**, dadurch reicht die kürzere
Gewindetiefe des NEX-Stifts gerade aus. **Das ist kein Qualitätsunterschied – nur ein
Maßunterschied.**

### 🎯 Fünf Lösungen (sortiert nach Aufwand)

| # | Lösung | Aufwand | 💰 | Bewertung |
|---|---|---|---|---|
| **A** | 🔴 **Original-Gabel (RST Vogue TNL) retten** → ihre Stifte sind lang genug, die Deore-Arme passen wieder | 1,5–2 h + Dichtsatz | **25–50 €** | 🎯 **Beste Lösung**, wenn die Standrohre nur Flugrost haben. Löst **auch Baustelle #6**! → [`rst-vogue-tnl-federgabel.md`](rst-vogue-tnl-federgabel.md) |
| **B** | **Längere M8-Ersatz-Cantisockel** in die NEX-Gabel schrauben | 30–45 min | **15–16 €** | ✅ **Sehr gut.** Die Deore-Arme bleiben am aktuellen Rad |
| **C** | **Stifte der RST-Gabel in die NEX-Gabel umsetzen** (falls Gewinde + Länge passen) | 30 min | **0 €** | 💡 **Erst probieren!** Aber die RST-Gabel nicht beschädigen, falls du sie retten willst |
| **D** | **Kürzere M6-Befestigungsschraube** oder dünnerer Scheibenstapel am Deore-Arm | 10 min | **0–3 €** | 💡 **Zuerst testen** – billigste Möglichkeit |
| **E** | **Tektro-Arme behalten** (aktueller Zustand) | 0 | 0 € | ✅ **funktioniert** – du hast die Backen bereits auf gleichen Abstand eingestellt, ohne Schleifen |

### 🔧 Lösung D zuerst testen (10 min, 0 €)

| ☐ | Schritt |
|---|---|
| ☐ | Deore-Bremsarm abnehmen, **alle Teile in Reihenfolge** auf ein Tuch legen + **Foto** |
| ☐ | **Gesamthöhe des Scheibenstapels** messen (Buchse + Scheiben + Arm) |
| ☐ | Dasselbe beim **Tektro**-Arm messen und **vergleichen** |
| ☐ | 🔴 Prüfen: Ist beim Deore-Arm eine Scheibe dabei, die man **weglassen** kann, ohne dass die Buchse kippt? |
| ☐ | Prüfen: Gibt es eine **kürzere M6-Befestigungsschraube** (Länge messen, z. B. 12 mm statt 15 mm)? |
| ☐ | Montieren, mit **5–7 Nm** anziehen, prüfen ob der Arm **spielfrei** sitzt |

### 🛒 Lösung B: Ersatzteile (konkret bestellbar)

Es gibt einen deutschen Hersteller (**BrakeSTUFF**, Amtsberg), der **CNC-gefertigte
Ersatz-Cantisockel** in verschiedenen Längen und Bauformen macht. Alle haben:
**M8-Außengewinde**, **Ø 8 mm Aufnahme** (V-Brake-Norm), **M6-Innengewinde** für die
Bremsarmschraube, **Anzugsmoment 5–6 Nm**.

| Produkt | Daten | 💰 | Besonderheit |
|---|---|---|---|
| **Cantisockel M8** (`CS-M8-VA`) | M8 · Ø 8 mm · M6 innen · **Einschraublänge 10 mm** · Edelstahl (19,3 g/Paar) oder Alu (7,6 g/Paar) | **14,90 €** | 🔴 **Kompatibilitätsliste nennt ausdrücklich „Staiger"** (neben Cannondale Fatty, Fox, Manitou, Zoom Tracker). Lieferzeit 1–3 Tage |
| **Cantisockel M8 für RST** (`CS-M8-RST`) | M8 · Ø 8 mm · M6 innen · Einschraublänge 10 mm · Edelstahl | **16,00 €** | 🔴 **„verlängertes Gewinde und zusätzlicher Bund"** – passend für **RST Hi-5, Hi-5 TL, Mozo, Zeta**. Lieferzeit 45–55 Tage |
| **Cantisockel M8 ohne Bund** (RockShox) | M8 · Einschraublänge **10 mm oder 16 mm** | ab **14,50 €** | 💡 **die 16-mm-Variante ist der Kandidat für „länger"** – aber **ohne Bund**! |
| **Cantisockel M8 mit 3-Loch-Federplatte** | M8, integrierte **3-Loch-Federaufnahme** | **18,50 €** | 💡 falls die Federrasten-Bohrungen nicht fluchten |
| **Federaufnahme für Cantisockel** (Adapter) | Edelstahl, für **M6, M8, M10** | **7,50 €** | 💡 separate Federplatte, wenn der Federstift nicht passt |
| **Cantisockel M10** | für **Merlin / RST / Salsa / Winora** | ab **12,90 €** | ⚠️ nur falls dein Gewinde doch M10 ist (deine Messung sagt **M8**) |

**Montagehinweis des Herstellers:**
> *„Vor der Montage das Loch und die Auflagefläche an Gabel/Rahmen sauber reinigen und
> trocknen lassen. Einige Tropfen Schraubensicherung (z. B. **Loctite 243**) auf das Gewinde,
> dann mit **5–6 Nm** einschrauben. Vor der ersten Fahrt **2–3 h warten**, bis die
> Schraubensicherung ausgehärtet ist."*

📄 **Maßblatt zum Vergleichen:** BrakeSTUFF stellt ein PDF mit **Gewinde, Aufnahme-Ø,
Einschraublänge und GESAMTLÄNGE** bereit → `brake-stuff.de` → Cantisockel → „Abmessungen
der Cantisockel für V-Brakes und U-Brakes". 🔴 **Vor dem Bestellen die Gesamtlänge der
vorhandenen Stifte messen und mit dem Maßblatt abgleichen!**

### 📐 Messwerte eintragen (das entscheidet über die Lösung)

| Messung | schwarze NEX-Gabel | weiße RST-Gabel | Differenz |
|---|---|---|---|
| 🔴 **Stiftlänge über dem Bund** (freistehend) | ❓ ____ mm | ❓ ____ mm | ❓ ____ mm |
| Stift-Gesamtlänge | ❓ ____ mm | ❓ ____ mm | |
| Einschraubtiefe im Tauchrohr | ❓ ____ mm | ❓ ____ mm | |
| Ø des Stifts | ✅ **7,95 mm → M8** | ✅ **7,95 mm → M8** (vom Besitzer gemessen) | gleich ✅ |
| **M6-Innengewinde** vorhanden? Tiefe? | ❓ ____ mm | ❓ ____ mm | |
| Bund-/Flanschhöhe | ❓ ____ mm | ❓ ____ mm | |
| Zwei Abflachungen für Gabelschlüssel? | ❓ | ❓ | |
| M6-Befestigungsschraube Shimano: Länge | ❓ ____ mm | – | |
| M6-Befestigungsschraube Tektro: Länge | ❓ ____ mm | – | |
| Scheibenstapel-Höhe Shimano-Arm | ❓ ____ mm | – | |
| Scheibenstapel-Höhe Tektro-Arm | ❓ ____ mm | – | |
| Abstand Mitte Ausfallende → Mitte Sockel | ❓ (Soll 28″: **283 mm**) | ❓ | ✅ laut Besitzer **baugleich** |

---

### 🔴 Ursache 1 im Detail: Lack auf dem Sockel

Das ist **die häufigste Ursache** bei genau diesem Symptom („Bremse passt nicht auf die
Aufnahme“). Der Bremssockel wird beim Lackieren der Gabel mitlackiert, die Lackschicht
(0,1–0,3 mm) reicht schon, damit der Bremsarm nicht ganz aufgeschoben werden kann.

**Vorgehen:**
1. Bremsarm abziehen
2. Sockel mit **Schleifleinen Körnung 400** rundherum abziehen, bis das Metall blank ist
3. Mit 600er nachschleifen, glätten
4. Reinigen (Isopropanol), **dünn fetten**
5. Bremsarm aufschieben: er muss **bis zur Sockel-Schulter** gehen
6. ⚠️ Nicht mit der Feile „arbeiten wie ein Grobian“ – der Sockel soll rund und maßhaltig bleiben

### Sockel-Höhe prüfen (Ursache 4)

**Shimano-Referenzmaße** für den Abstand **Mitte Ausfallende → Mitte Bremssockel**:

| Laufradgröße | Felgendurchmesser | Soll-Abstand |
|---|---|---|
| 26" | 559 mm | **ca. 253,5 mm** |
| 27,5" | 584 mm | ca. 266 mm |
| **28" / 29"** | **622 mm** | **ca. 283 mm** |
| Abstand der Sockel zueinander | – | 77–85 mm |

> Wenn die schwarze Gabel für **26"** gebaut ist, das weiße Rad aber **28"** hat, sitzt der
> Sockel ca. **30 mm zu tief** → die Bremsarme stehen zu tief, die Beläge treffen den Reifen
> oder liegen unter der Felge. Dann passen die „guten“ Bremsarme geometrisch nicht, auch
> wenn sie mechanisch auf den Sockel gehen.
>
> **Messen und eintragen:**

| Messung | Schwarze Gabel | Weißes Rad (Hinterbau) | Soll |
|---|---|---|---|
| Abstand Mitte Ausfallende → Mitte Bremssockel | ❓ ____ mm | ❓ ____ mm | s. Tabelle |
| Laufradgröße des weißen Rads (ETRTO) | – | ❓ ____-____ | |

Es gibt **Bremssockel-Adapter** (z. B. Sinz, Mavic Speed City Adapter), die den Sockel um
16–26 mm versetzen. Die überbrücken aber **keine** 30 mm – bei einem echten 26"/28"-Versatz
hilft nur die richtige Gabel.

---

## 3. ⚠️ Kann man den Stahlstift (Bremssockel) selbst tauschen?

Dein Plan war, die Stahlstifte zu tauschen, damit die guten weißen Bremsarme passen.
**Ob das geht, hängt vom Gabelmaterial ab:**

| Gabel | Wie ist der Sockel befestigt? | Tauschbar? |
|---|---|---|
| **Stahlgabel** | **angeschweißt / aufgelötet** („Schweißsockel“) | ❌ **nein** – nur mit Lötbrenner + neuem Sockel in einer Werkstatt. Am Rahmen/Gabel schweißen = 🔴 sicherheitskritisch, lieber nicht selbst |
| **Alugabel** | oft **eingeschraubt**: Stahlbolzen mit **zwei Abflachungen** für einen Gabelschlüssel, Gewinde M8 oder M10 in der Gabel | ✅ **ja** – Bolzen mit Gabelschlüssel/Schraubstock rausdrehen, neuen Cantisockel mit passendem Gewinde + **Schraubensicherung** rein |

### ✅ Geklärt: Alu-Tauchrohre → Sockel eingeschraubt

| Gabel | Material Tauchrohre | Sockel-Befestigung | Tauschbar? |
|---|---|---|---|
| **schwarz: SR Suntour NEX** | ✅ **Aluminium** | **eingeschraubt** (vermutet) | ✅ **ja** |
| **weiß: RST Vogue TNL** | ✅ **Aluminium** (RST-Katalog: „Outer leg: Aluminum") | **eingeschraubt** (vermutet) | ✅ **ja** |

💡 **Hinweis:** Bei Federgabeln sind die **Tauchrohre (lowers)** Alu/Magnesium, der
**Schaft** ist Stahl (CroMo) – der Magnet-Test gehört also an die **Tauchrohre**, nicht an
den Schaft. ❓ Kurzer Magnet-Test zur Bestätigung steht noch aus.

### Wenn es ein eingeschraubter Sockel ist – Ablauf

1. Bremsarm ab, Befestigungsschraube raus
2. **Foto** machen (Position des Federstift-Lochs!)
3. Gabelschlüssel oder Schraubstock an den **zwei Abflachungen** des Bolzens ansetzen
4. Gegenhalten an der Gabel (nicht am Schaft verdrehen!)
5. Bolzen **herausdrehen** (Rechtsgewinde = gegen den Uhrzeigersinn lösen)
6. Gewinde in der Gabel messen: **M8 oder M10**, Steigung bestimmen
7. Neuen Cantisockel mit **passendem Gewinde** besorgen (💰 5–15 €, „Cantisockel zum
   Einschrauben“ / „canti boss threaded“)
8. Gewinde reinigen, **Schraubensicherung mittelfest (Loctite 243)** auftragen
9. Neuen Sockel eindrehen, **Federstift-Loch auf dieselbe Position** ausrichten
   („Fixierstift auf 6.00 oder 12.00 Uhr stellen“)
10. Aushärten lassen, Bremsarm montieren, einstellen

⚠️ **Wenn der Sockel angeschweißt ist:** nicht abschneiden, nicht aufbohren, nicht biegen.
Eine Gabel ist ein **sicherheitstechnisches Bauteil**. In dem Fall gilt Abschnitt 4.

---

## 4. 💡 Die elegante Lösung: weiße Original-Gabel zurückbauen

**Zwei deiner Baustellen haben dieselbe Wurzel:**

| Baustelle | Problem | Ursache |
|---|---|---|
| #5 | Steuersatz: zu wenig Gewinde, keine Kontermutter | schwarze Gabel hat einen **zu kurzen Schaft** |
| #4 | Vorne passen die guten Bremsarme nicht | schwarze Gabel hat einen **fremden Bremssockel** |

**Beides verschwindet, wenn die weiße Original-Gabel zurückkommt:**

| | mit schwarzer Gabel | mit weißer Original-Gabel |
|---|---|---|
| Schaftlänge / Kontermutter | ⚠️ zu kurz | ✅ passend (war ja original) |
| Bremssockel vorne | ⚠️ passt nicht | ✅ original passend |
| Schutzblech-Ösen | ✅ passten „easy“ | ⚠️ müssen neu gelöst werden (Universal-Schellen, 💰 3–8 €) |
| Lenkgeometrie | ⚠️ evtl. verändert (nervöser) | ✅ original |

**Voraussetzung:** Die weiße Original-Gabel ist noch vorhanden und nicht defekt.
→ **Bitte klären: Wo ist die alte Gabel?** (siehe
[`../03-todos/werkzeug-und-material.md`](../03-todos/werkzeug-und-material.md) Abschnitt 4 „Ersatzteilkiste“)

**Abwägung:**

| Variante | Aufwand | Kosten | Ergebnis |
|---|---|---|---|
| A. Alte Gabel zurück + Schutzblech mit Schellen | mittel (Steuersatz neu einstellen, Schutzblech neu montieren) | 💰 3–10 € | ✅ löst #4 **und** #5, Geometrie original |
| B. Schwarze Gabel behalten, Federraste nutzen + ggf. neue V-Brake vorne | gering | 💰 0–30 € | ⚠️ löst #4 teilweise, #5 bleibt Provisorium |
| C. Schwarze Gabel behalten + gebrauchte Gabel mit langem Schaft kaufen | mittel | 💰 20–60 € | ✅ löst #5, #4 offen |
| D. Sockel tauschen (nur bei Alugabel) | mittel | 💰 5–15 € | ⚠️ löst nur #4, riskant bei Stahlgabel |

**Empfehlung:** Erst **B** machen (kostet nichts, 15 min: Federraste + Sockel schleifen),
dann prüfen, ob die alte Gabel noch da ist → wenn ja, **A**.

---

## 🧪 Test-Protokoll

| # | Test | Ergebnis |
|---|---|---|
| 1 | Magnet-Test Gabel: Stahl oder Alu? | ❓ |
| 2 | Bremssockel: Lack/Rost sichtbar? | ❓ |
| 3 | Sockel mit 400er Schleifleinen abgezogen → Bremsarm geht jetzt ganz drauf? | ❓ |
| 4 | Federstift sitzt in einer Bohrung? | ❓ |
| 5 | **Federraste in anderes Loch gesetzt → Rückstellkraft besser?** | ❓ |
| 6 | Abstand Mitte Ausfallende → Mitte Sockel (schwarze Gabel) | ❓ ____ mm |
| 7 | Abstand Mitte Ausfallende → Mitte Sockel (weißer Hinterbau, als Referenz) | ❓ ____ mm |
| 8 | Laufradgröße weißes Rad (ETRTO) | ❓ ____-____ |
| 9 | Spalt zwischen Bremsarm und Sockel-Schulter | ❓ ____ mm |
| 10 | Federn der weißen Bremsarme: Drahtstärke/Windungen/Hakenform gleich wie die schwarzen? | ❓ |
| 11 | Sockel/Bolzen gereinigt und dünn gefettet? | ❓ |
| 12 | Ist die weiße Original-Gabel noch vorhanden? | ❓ |
| 13 | Modellnummer der weißen Bremsarme | ❓ |
| 14 | Modellnummer der schwarzen Bremsarme | ❓ |

**Ergebnis:** ____________________________
**Gewählte Maßnahme:** ____________________________

---

## 📸 Fotos zum Machen

| ☐ | Foto |
|---|---|
| ☐ | Bremssockel der schwarzen Gabel, Nahaufnahme, seitlich beleuchtet (Lack? Rost? Abflachungen?) |
| ☐ | Bremssockel ohne Bremsarm, von vorne (die 3 Bohrungen sichtbar) |
| ☐ | Rückseite eines Bremsarms (Federstift sichtbar) |
| ☐ | Weiße Bremsarme und schwarze Bremsarme nebeneinander |
| ☐ | Federn beider Bremsarme nebeneinander |
| ☐ | Modellnummer/Aufdruck der Bremsarme |
| ☐ | Seitenansicht der Gabel mit Maßband am Sockel (Abstand zum Ausfallende) |

## 💰 Einkaufsbedarf

| Teil | Spec | Prio | ca. Preis |
|---|---|---|---|
| 🔴 **Cantisockel M8** (`CS-M8-VA`, BrakeSTUFF) | M8 · Ø 8 mm · M6 innen · Einschraublänge **10 mm** · Edelstahl/Alu · 🔴 Kompatibilitätsliste nennt **„Staiger"** | 🎯 | **14,90 €** |
| 🔴 **Cantisockel M8 für RST** (`CS-M8-RST`) | M8 · **verlängertes Gewinde + zusätzlicher Bund** | 🎯 | **16,00 €** |
| **Cantisockel M8 ohne Bund, 16 mm** | 💡 **die längere Version** – 🔴 **Gesamtlänge vorab messen/abgleichen!** | 🎯 | ab **14,50 €** |
| **Cantisockel M8 mit 3-Loch-Federplatte** | falls die Federrasten-Bohrungen nicht fluchten | 🟢 | 18,50 € |
| **Federaufnahme für Cantisockel** (M6/M8/M10) | separate Federplatte aus Edelstahl | 🟢 | 7,50 € |
| **M6-Befestigungsschrauben, kürzer** | ❓ Länge der vorhandenen messen, dann 1–2 mm kürzer | 🟡 | 1–3 € |
| **Loctite 243** | für die neuen Cantisockel (5–6 Nm, 2–3 h aushärten lassen) | 🔴 | 8 € |
| 🔴 **RST Dust Seal Kit** | Abstreifdichtung für RST-Gabeln · Version **28,6 mm** (Vogue/VIVair/F1RST) oder **30 mm** · ❓ **Standrohr-Ø messen!** | 🔴 | **14,28 €** |
| **Gabelöl** | ❓ Viskosität klären (Standardannahme 5W–10W), 100–250 ml | 🔴 | 8–15 € |
| **Chrompolitur / Stahlwolle 0000** | Flugrost von den RST-Standrohren entfernen | 🔴 | 5–10 € |
| ~~Schleifleinen 400/600~~ | ❌ **entfällt** – kein Lackproblem | – | – |
| ~~Bremssockel-Adapter~~ | ❌ **entfällt** – kein 26″/28″-Versatz | – | – |
| Universal-Schellen für Schutzblech | nur falls die RST-Gabel keine Öse hat | 🟢 | 3–8 € |
| Ersatz-V-Brake vorne | nur falls alle Lösungen scheitern · V-Brake, **long pull** | 🟢 | 15–30 € |

## Verknüpfungen

- Baugruppe: [`../02-teile/40-bremsen.md`](../02-teile/40-bremsen.md)
- Gabel/Steuerkopf: [`../02-teile/20-steuersatz-gabel-vorbau-lenker.md`](../02-teile/20-steuersatz-gabel-vorbau-lenker.md)
- Anleitung Einstellen: [`../05-anleitungen/bremsen-einstellen.md`](../05-anleitungen/bremsen-einstellen.md)
- Baustellenliste: [`../03-todos/offene-baustellen.md`](../03-todos/offene-baustellen.md)
