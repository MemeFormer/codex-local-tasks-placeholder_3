# 🚲 Weißes Trekkingbike – STAIGER Daytona Sportline

**Hauptbike / Zielrad** · Datenstand: 2026-09-04 · **viele Werte jetzt belegt** ✅

---

## 1. Identifikation ✅

| Feld | Wert |
|---|---|
| **Hersteller** | ✅ **STAIGER** |
| **Modell** | ✅ **Daytona Sportline** |
| **Rahmennummer** | ✅ **AWO7230329** |
| **Rahmen** | ✅ **Alloy 6061, Double Butted** (Aluminium, doppelt konifiziert) |
| Baujahr | ❓ **Hypothese: 2007, KW 23** – `AWO` + `7 23` + `0329`. Passt zur Komponenten-Ära (Deore LX M570/M580 ≈ 2004–2008). Bitte gegenprüfen |
| Radstand / Laufradgröße | ✅ **28 Zoll / 700C / ETRTO 622** |
| Gänge | ✅ **27 (3×9)** |
| Bremssystem | ✅ **V-Brake** (Felgenbremse, long pull) |
| Rahmenfarbe | weiß |

### 💡 Was die Original-Ausstattung bestätigt

Recherche zum Staiger Daytona ergab für spätere Baujahre: **Federgabel Suntour mit 63 mm
Federweg**, **Felgen Mach1 210**, **Vorbau/Sattelstütze/Griffe XLC Comp**, **Shimano Deore
V-Brakes**, **Schwalbe Marathon**. Das deckt sich fast vollständig mit deinen Funden:

| Original-Daytona-Spec (Recherche) | Dein Fund am Rad | Treffer |
|---|---|---|
| Federgabel **Suntour, 63 mm Federweg** | **SR Suntour NEX … T63** (= 63 mm) | ✅ |
| Felgen **Mach1 210** Alu-Hohlkammer | **Mach1 210**, ETRTO 622×19c | ✅ |
| **XLC Comp** Vorbau, Sattelstütze, Griffe | **XLC-comp** Sattelstütze + Schnellspanner | ✅ |
| Shimano **Deore V-Brakes** | Bremszangen hinten **Shimano Deore** | ✅ |
| Schwalbe **Marathon** | **Schwalbe Marathon Plus** 47-622 hinten | ✅ |
| Shimano Deore, 27 Gänge | Deore LX M570/M580 + Deore M511/M530, 3×9 | ✅ |

> 🎉 **Wichtigste Konsequenz:** Die schwarze **SR Suntour NEX mit 63 mm Federweg (T63)** ist
> **geometrisch ein passender Ersatz** für die originale Suntour-Federgabel (ebenfalls 63 mm).
> Das Lenkverhalten ist also **nicht** durch eine falsche Einbauhöhe verfälscht – die
> „ungewohnte Lenkung" liegt woanders. **Dennoch:** Achse-zu-Krone-Maß vergleichen (unten).

---

## 2. 🔴 Die zentrale Erkenntnis: warum das Gewinde nicht reicht

Die **SR Suntour NEX mit Gewindeschaft** hat ab Werk diese Daten (Händler-Spezifikation):

| Größe | Wert | Bedeutung für dich |
|---|---|---|
| Schaft-Außendurchmesser | **28,6 mm = 1⅛ Zoll** | ✅ Steuerkopf ist **1⅛ Zoll**, nicht 1 Zoll! |
| Schaftmaterial | **Stahl** | |
| Schaftlänge (Handelsvarianten) | **210 mm** oder **225 mm** | |
| 🔴 **Gewindelänge ab Werk** | **nur 55 mm** (am oberen Ende!) | **der Rest des Schafts ist glatt** |
| Achse bis Gabelkrone (axle-to-crown) | **445–469 mm** (50 mm) bzw. **477 mm** (63 mm) | |
| Gabelvorlauf / Offset | 42 mm | |
| Bremsaufnahme | **Cantilever-/V-Brake-Sockel** | |
| Einbaubreite / Achse | 100 mm / QR | |
| Gabelscheiden | **Aluminium** | 🔴 **→ Bremssockel ist wahrscheinlich EINGESCHRAUBT** |
| Tauchrohre / Standrohre | Alu / Stahl, Ø 28 mm | |
| Federung | Stahlfeder, Vorspannung einstellbar | |

### Die Rechnung, die dein Problem erklärt

```
Ein Gewindesteuersatz braucht über dem Steuerrohr:
   oberer Lagerkonus  ~7 mm
   Mutter            ~10 mm
   Kontermutter      ~10 mm
   ─────────────────────────
   Summe             ~27 mm

NEX-Gewindeschaft: nur die obersten 55 mm haben Gewinde.
```

Ein Gewindeschaft wird beim Einbau **auf Länge gekürzt** – und zwar **oben**, also genau dort,
wo das Gewinde ist. **Jeder Millimeter, der abgesägt wurde, ist verlorener Gewindelänge.**

| Szenario | Ergebnis |
|---|---|
| Spenderrad-Steuerkopf war **kürzer** → Schaft wurde dafür gekürzt | Schaft = Steuerkopf_Spenderrad + ca. 25 mm |
| STAIGER-Steuerkopf ist **ca. 23 mm länger** | → es bleiben nur noch **ca. 2 mm = 1–2 Gewindegänge** übrig |

> 🎯 **Das ist exakt dein Befund.** Der Schaft wurde also für den **kürzeren Steuerkopf des
> Spenderrads** gekürzt, und der STAIGER-Rahmen hat ein längeres Steuerrohr.
> ⚠️ Zusätzlich: Weil das Gewinde nur 55 mm lang ist, war der Vorrat von vornherein knapp.

### 🔴 Sicherheitsaspekt Quill-Vorbau im Gewindeschaft

Ein Quill-Vorbau spreizt sich mit dem Innenkeil **gegen die Schaft-Innenwand**. Im
**Gewindebereich ist die Wand dünner** (das Gewinde schneidet Material weg). Ein Keil, der
sich im Gewindebereich spreizt, kann den Schaft **aufreißen**.

| ☐ | Prüfung | Soll |
|---|---|---|
| ☐ | Wo liegt der **Innenkeil/Expander** des Vorbau-Einsteckteils relativ zum Gewindebereich? | 🔴 **unterhalb** des Gewindes, im glatten Schaftbereich |
| ☐ | Ist die „MIN INSERTION"-Markierung des Vorbaus **im** Schaftrohr? | ✅ darf nicht sichtbar sein |
| ☐ | Wie tief steckt das Einsteckteil mindestens? | ≥ 50–65 mm |
| ☐ | Schaft-Innendurchmesser gemessen | 1⅛ Zoll Gewindeschaft → ca. **25,4 mm** für den Quill |

---

## 3. 💡 Lösungswege für das Gewinde-Problem – jetzt mit echten Zahlen

| # | Lösung | Aufwand | Kosten | Bewertung |
|---|---|---|---|---|
| 1 | **Flache Kontermutter 1⅛ Zoll × 24 tpi** (niedrige Form) | gering | 💰 3–10 € | ⚠️ bringt nur ca. 5 mm – bei 1–2 Gängen **vermutlich nicht genug** |
| 2 | Zahnring entfernen + Gewinde entfetten + Loctite 243 neu | gering | 💰 0–8 € | 🟡 Provisorium verbessern, ersetzt keine Kontermutter |
| 3 | 🔴 **NEX-Gewindegabel mit 225 mm Schaft** statt 210 mm | mittel | 💰💰 50–90 € | 💡 **+15 mm Schaft = Lösung**, gleiche Geometrie (63 mm, 700C) |
| 4 | 💡💡 **Auf Ahead umbauen**: NEX **gewindelos** (Schaft 255 mm) + Ahead-Steuersatz + Ahead-Vorbau | mittel | 💰💰💰 70–130 € | ✅ **beste Dauerlösung** – Ahead braucht **kein Gewinde**, Problem verschwindet komplett. Der 34-mm-Außendurchmesser der Lagerschalen ist bei 1⅛ Zoll **Gewinde und Ahead identisch**, die Rahmenschalen können oft bleiben |
| 5 | Ahead-Konverter auf den vorhandenen Gewindeschaft (Quill-zu-Ahead-Adapter) | gering | 💰 15–25 € | 🟡 funktioniert, spreizt aber ebenfalls im Schaft |
| 6 | Gebrauchte originale Daytona-Gabel (Suntour NCX/NEX 63 mm) mit langem Schaft | mittel | 💰💰 25–60 € | ✅ gut, wenn verfügbar |

> ⚠️ **Wichtig bei Variante 1:** Es ist **1⅛ Zoll × 24 tpi (28,6 mm)**, **nicht** 1 Zoll!
> Keine Baumarkt-Mutter – das ist ein Zoll-Sondergewinde mit 1,058 mm Steigung.

---

## 4. Antrieb & Schaltung ✅

| Komponente | Verbaut | Daten | Zustand |
|---|---|---|---|
| **Kurbelgarnitur** | ✅ **Shimano Deore FC-M530/531** | **Hollowtech** (hohlgeschmiedete Arme), **Octalink**-Verzahnung, Kurbelarmlänge **170 mm** | ❓ Zustand |
| Kettenblätter | Shimano, 3-fach | ❓ **Zähne zählen!** FC-M530 gab es als **44-32-22** (MTB) und **48-36-26** (Trekking). Da der Umwerfer FD-C050 max. 48 Zähne kann und es ein Trekkingrad ist: **vermutlich 48-36-26** | ❓ |
| **Innenlager** | ❓ zum FC-M530 gehört **BB-ES25 Octalink** | **BSA 68 mm** (1,37" × 24 tpi), Achslänge 113/118/121/126 mm, Kettenlinie 47,5 oder 50 mm | ❓ auf Abdruck prüfen |
| **Kette (Neukauf-Spec!)** | aktuell: repariert, ⚠️ zu kurz | ✅ **Shimano CN-HG53 oder CN-HG73** (Original-Spec zum FC-M530), **9-fach** | 💰 neu kaufen |
| Kassette | Shimano, **9-fach** (9 Ritzel) | ❓ Modell + Abstufung ablesen (Deore-Ära: CS-HG50-9 **11-32**; Daytona 2016: HG200 **11-34**) | ❓ |
| Freilaufkörper | HG-Spline auf der FH-M530-Nabe | 8/9-fach kompatibel | ✅ läuft feiner als der vom Spenderrad |
| **Schalthebel** | ✅ **Shimano Deore LX SL-M580** | **9-fach Rapidfire (Triggerhebel)**, Lenkerklemmung **22,2 mm** | ✅ „laufen top" |
| **Bremshebel** | ✅ **Shimano Deore LX BL-M571** | **V-Brake / long pull**, Lenkerklemmung **22,2 mm** | ✅ **die guten, original** |
| **Umwerfer** (vorne!) | ✅ **Shimano FD-C050** (Aufdruck als „GD-C050" gelesen – F/G verwechselt) | „OP Swing" = **Top Swing**, SIS, 3-fach, Klemmung **28,6 / 31,8 mm**, Befestigung **5 mm Inbus, 5–7 Nm**, für **Octalink/Spline**-Kurbel, max. 48 Zähne, Kapazität 20 Zähne, Kettenlinie 46–52,5 mm | ✅ |
| **Schaltwerk** (hinten) | ✅ **Shimano Deore RD-M511** (bzw. M510-Familie) | **9-fach, SGS-Langkäfig**: max. größtes Ritzel **34 Zähne**, max. Differenz vorne **22 Zähne**, Gesamtkapazität **45 Zähne** | ✅ |
| Pedale | ❓ **unbekannt** | Gewinde **9/16" × 20 tpi** (bestätigt über die Shimano-Doku zum FC-M530) | ❓ |

> ⚠️ **Begriffskorrektur:** „Schaltwerk vorne" heißt korrekt **Umwerfer** (front derailleur).
> „Schaltwerk" allein meint immer das **hintere** (rear derailleur).
> ⚠️ **Und:** „Pedale Shimano Deore Hollowtech (170 FC M530/531)" – **FC-M530/531 ist die
> Kurbelgarnitur**, nicht die Pedale. „FC" = Front Chainwheel. **170** = Kurbelarmlänge in mm.
> Die Pedale selbst sind noch unbekannt.

### Rechnerische Prüfung der Schaltkapazität

```
RD-M511:  max. größtes Ritzel   34 Zähne
          max. Differenz vorne  22 Zähne
          Gesamtkapazität       45 Zähne

Fall A  Kurbel 48-36-26 + Kassette 11-32:
        Differenz vorne  = 48 − 26 = 22  ✅ (exakt am Limit)
        Differenz hinten = 32 − 11 = 21
        Gesamtbedarf     = 22 + 21 = 43  ✅ ≤ 45

Fall B  Kurbel 44-32-22 + Kassette 11-34:
        Differenz vorne  = 44 − 22 = 22  ✅ (exakt am Limit)
        Differenz hinten = 34 − 11 = 23
        Gesamtbedarf     = 22 + 23 = 45  ✅ = exakt an der Grenze

→ Beide Fälle passen, aber es ist KEIN Spielraum mehr.
→ Big-Big ist konstruktiv gerade noch erlaubt, wegen der zu kurzen Kette trotzdem meiden.
```

### Kettenlänge für den Neukauf

```
L = (2 × Kettenstrebenlänge in mm) / 12,7 + (Z_groß + Z_ritz) / 2 + 2

Kettenstrebenlänge (Mitte Tretlager → Mitte Achse):  ❓ ____ mm  (Daytona ca. 445–450 mm)
Z_groß  = ____ Zähne (großes Kettenblatt)
Z_ritz  = ____ Zähne (größtes Ritzel)

→ Standard-Ketten kommen mit 114/116 Gliedern und werden gekürzt.
→ ⚠️ NICHT die reparierte alte Kette als Maß nehmen – die ist zu kurz!
```

💰 **Konkrete Bestellung:** **Shimano CN-HG53 9-fach** (Original-Spec, ca. 12–18 €) oder
**KMC X9** (ca. 15–20 €). Zusätzlich ein **KMC MissingLink 9-fach** als wiederverwendbares
Schloss (ca. 4 €) – praktisch für die Reinigung.

---

## 5. Bremsen ✅ – jetzt mit echten Daten

**System:** ✅ **V-Brake** (long pull). Bremshebel **Shimano Deore LX BL-M571** –
die passen konstruktiv zu V-Brakes. ✅ **Kein Zugweg-Problem.**

| Position | Bremshebel (Lenker) | Bremsarme (Zange) | Bremsbeläge |
|---|---|---|---|
| **vorne** | ✅ **Shimano Deore LX BL-M571** (weiß, original) | ⚠️ **Tektro** (vom Spenderrad, an der Suntour-Gabel) | ⚠️ **Tektro 836**, **62 mm**, „EN-STANDARD **B61**" (li + re) |
| **hinten** | ✅ **Shimano Deore LX BL-M571** (weiß, original) | ✅ **Shimano Deore** (weiß, original) | ⚠️ **Tektro 836**, **62 mm** – li. „**B1**", re. „**B44**" |

### 🔴 Befund 1: Die Beläge sind zu kurz für die Shimano-Deore-Zange

| Größe | Wert |
|---|---|
| Verbaute Beläge | **Tektro 836** – Nennlänge **63 mm** (deine Messung 62 mm ✅ bestätigt) |
| Shimano-Deore-V-Brakes sind ausgelegt für | **70 mm** (z. B. Shimano M70T4 = 72 mm, S65T = 70 mm) |
| Differenz | **ca. 7–10 mm kürzer** |

**Konsequenzen:**

| Effekt | Bewertung |
|---|---|
| Weniger Auflagefläche → weniger Bremsleistung | ⚠️ spürbar, ca. 10–15 % |
| Belag deckt die Bremsspur nicht vollständig ab | ⚠️ die Felge nutzt ungleichmäßig ab |
| Belagkanten sitzen näher an der Felgenkante | 🔴 **bei abgefahrener Bremsflanke hakt der Belag an der Kante → Bremse kehrt nicht zurück** |
| Tektro-Beläge haben **eigenes Befestigungsmaterial** | 🔴 **Konvex-/Konkavscheiben passen evtl. nicht zur Shimano-Zange** → Belag steht schräg → verkantet |

> 🎯 **Das ist ein sehr starker Kandidat für Baustelle #3 (hintere Bremse kehrt nicht zurück).**
> Die Shimano-Deore-Zange hinten ist original, Federn und Zug sind original – **aber die
> Beläge sind fremde, zu kurze Tektro-Beläge mit fremdem Scheibensatz.**

💰 **Empfehlung:** Hinten auf **Shimano-V-Brake-Beläge 70 mm** wechseln
(z. B. **Shimano M70T4**, **S65T** oder **M65T**, ca. 8–15 €/Paar inkl. korrektem
Scheibensatz). Das ist die sauberste Lösung.

### 🔴 Befund 2: Links und rechts unterschiedliche Belag-Codes

Hinten: links **B1**, rechts **B44**. Vorne: beide **B61**.
Wahrscheinlich sind das **Produktions-/Formcodes**, aber falls es unterschiedliche
**Mischungen** sind, bremst die Bremse einseitig und der Arm mit dem härteren Belag kehrt
schlechter zurück. → **Prüfen: sind beide Beläge gleich hart/gleich dick/gleich lang?**

### 🔴 Befund 3: Warum die weißen Shimano-Bremsarme nicht auf die Suntour-Gabel passten

Die Suntour NEX hat **Aluminium-Gabelscheiden**. Bei Alu-Gabeln ist der V-Brake-Sockel
(Bremsboss) in der Regel ein **eingeschraubter Stahlbolzen** mit **zwei Abflachungen** für
einen Gabelschlüssel – nicht angeschweißt.

Ein bekanntes und gut dokumentiertes Problem: **Der Bund des Sockels ist länger als die
Ausnehmung im Shimano-Bremsarm.**

| Maß | typischer Wert |
|---|---|
| Länge des Sockel-Bunds | ca. **5,6 mm** |
| Tiefe der Ausnehmung im Bremsarm | ca. **4,3 mm** |
| → Spalt | ca. **1,3 mm** – der Arm liegt nicht an, „passt nicht" |

**Belegter Fix:** Den eingeschraubten Sockel **ca. 2–2,5 mm zurückdrehen**, dann passt der
Bremsarm bündig. Genau das hattest du selbst vorgeschlagen („die Stahlstifte selbst tauschen") –
**dein Plan ist machbar**, weil die Suntour-Gabel Alu-Scheiden hat.

| Schritt | Detail |
|---|---|
| 1. Prüfen | **Magnet-Test** an den Gabelscheiden (Alu = unmagnetisch). Hat der Sockel **zwei Abflachungen**? → eingeschraubt |
| 2. Markieren | Position des **Federstift-Lochs** fotografieren (12-Uhr- oder 6-Uhr-Stellung) |
| 3. Lösen | Gabelschlüssel an den Abflachungen, gegenhalten, **herausdrehen** (Rechtsgewinde) |
| 4. Gewinde messen | **M8 oder M10** + Steigung bestimmen |
| 5. Neu setzen | Sockel **2–2,5 mm tiefer** einschrauben, **Loctite 243**, Federstift-Loch auf dieselbe Position |
| ⚠️ Grenze | Nicht so weit herausdrehen, dass die **Gewindeeinschraubtiefe** zu gering wird. Mindestens **8–10 mm** Eingriff müssen bleiben |
| Alternative | Passenden **Ersatz-Cantisockel** mit kürzerem Bund (💰 5–15 €) |

→ Details: [`../04-diagnose/vordere-bremsarme-sockel.md`](../04-diagnose/vordere-bremsarme-sockel.md)

### Noch zu messen

| ☐ | Wert |
|---|---|
| ☐ | Abstand **Mitte Ausfallende → Mitte Bremssockel** an der Suntour-Gabel (Soll 700C: ca. **283 mm**) |
| ☐ | Derselbe Abstand am STAIGER-Hinterbau (als Referenz) |
| ☐ | Abstand der beiden Sockel zueinander (Soll 77–85 mm) |
| ☐ | Länge des Sockel-Bunds vs. Tiefe der Ausnehmung im Deore-Bremsarm |
| ☐ | Modellnummer der Bremszangen: Tektro (vorne) und Shimano Deore (hinten, z. B. BR-M530/M590) |
| ☐ | Länge der Nudel (Zugführungs-Röhrchen), Standard 92 mm |
| ☐ | Innenzug-Ø (V-Brake-Standard **1,5 mm**) |

---

## 6. Laufräder ✅ – jetzt mit echten Daten

### 6.1 Vorderrad

| Feld | Wert |
|---|---|
| **Nabe** | ✅ **Shimano DH-3N31-NT** – **Nabendynamo**, **6 V / 3 W**, Anschlusskabel **400–716 mm**, Code K911 |
| Einbaubreite / Achse | 100 mm / QR |
| Lagertyp | ✅ **Konuslager** (cup & cone) |
| 🔴 **Lager-Einstellseite** | ⚠️ **nur LINKS** (Seite **ohne** Kabelanschluss). Die Dynamo-Seite **nicht öffnen** – die Kabel sind extrem empfindlich |
| **Felge** | ✅ **Shining Double Wall A-M4**, **622 × 19** (Alu-Hohlkammer, Innenbreite 19 mm) |
| **Reifen** | ✅ **Schwalbe Active Line, K-Guard, 42-622** (28 × 1.60 / 700 × 40C), Code **HS 377** |
| Zustand | 🟢 „dreht nicht frei" = **normal** (Nabendynamo). Aber: **Lagervorspannung ist bei Shimano-Nabendynamos ab Werk fast immer zu fest** → siehe unten |

### 6.2 Hinterrad

| Feld | Wert |
|---|---|
| **Nabe** | ✅ **Shimano Deore FH-M530** (VIAM) – **Freilaufnabe hinten**, 9-fach HG |
| Einbaubreite / Achse | ❓ vermutlich **135 mm** / QR 10 mm – bitte messen |
| Lagertyp | ✅ **Konuslager** – wurde geöffnet und wieder montiert |
| 🔴 **Lager-Einstellseite** | ⚠️ **nur LINKS** (ohne Kassette). Rechts ist der Freilaufkörper aufgeschraubt |
| **Kassette** | Shimano **9-fach** (9 Ritzel), ❓ Modell + Abstufung |
| **Felge** | ✅ **Mach1 210**, **ETRTO 622 × 19c**, **Alloy 6060**, TB Frame → **Original-Daytona-Felge** ✅ |
| **Reifen** | ✅ **Schwalbe Marathon Plus 47-622** (28 × 1.75), **3.0–5.0 bar** |
| Zustand | ⚠️ schwerer laufend (Konus zu fest + eine Feder verloren) · 🔴 Bremsflanke prüfen |

### 6.3 ⚠️ Zwei Befunde an den Laufrädern

**Befund A – unterschiedliche Reifenbreiten vorne/hinten**

| | Reifen | Breite |
|---|---|---|
| vorne | Schwalbe Active Line K-Guard | **42 mm** |
| hinten | Schwalbe Marathon Plus | **47 mm** |

Nicht gefährlich, aber: unterschiedliches Abrollverhalten, und **das hintere Schutzblech
braucht mehr Freiraum** als das vordere. → **Freigängigkeit bei 47 mm hinten prüfen**
(mindestens 10 mm, besser 15 mm). Beide Felgen haben 19 mm Innenbreite → 42 und 47 mm sind
beide im passenden Bereich. ❓ Offen: Welcher Reifen ist original, welcher vom Spenderrad?
(„City-Profil-Reifen" vom Spenderrad → vermutlich der **Active Line** vorne.)

**Befund B – 🔴 Nabendynamo-Lager sind ab Werk fast immer zu fest**

Erfahrungswert aus der Schrauber-Praxis zu Shimano-Nabendynamos:

> Die Lager sind ab Werk praktisch immer **zu stramm** eingestellt. Man muss den linken Konus
> bei einem neuen Dynamo oft um bis zu **eine halbe Umdrehung** lösen, bevor es richtig läuft.
> **Und: Man kann es nicht erfühlen**, weil das magnetische Rasten des Dynamos die Wahrnehmung
> der Lager-Rauheit überdeckt.

**Richtige Einstellmethode für einen Nabendynamo** (anders als bei einer normalen Nabe!):

| Schritt | Detail |
|---|---|
| 1 | Schnellspanner **komplett entfernen** |
| 2 | **Nur links** arbeiten (Seite ohne Kabelanschluss). Rechts nicht öffnen |
| 3 | Kontermutter lösen, Konus gegenhalten |
| 4 | Konus lösen, bis **leichtes Spiel** spürbar ist |
| 5 | 🔴 **Ziel: minimales Spiel ohne Schnellspanner, das beim Spannen des Schnellspanners gerade verschwindet** |
| 6 | Kontermutter anziehen, Konus gegenhalten |
| 7 | Schnellspanner mit **Handkraft** spannen → jetzt muss das Spiel **gerade eben** weg sein |
| ⚠️ | **Nicht** versuchen, die Leichtgängigkeit zu erfühlen – das Magnet-Rasten täuscht. Nur nach **Spiel** gehen |
| 💡 | Fett nachfüllen: linken Konus lösen, Achse nach rechts drücken und mit einer Spritze Fett durch den Dichtungsspalt auf der Dynamo-Seite pressen |

→ Das bedeutet: „Vorderrad schwergängig" kann **doch** ein echtes (kleines) Problem sein –
nämlich **zu feste Lagervorspannung**, nicht Verschleiß. Prüfen mit der Methode oben.

### 6.4 🔴 Felgen-Bremsflanke prüfen (bleibt offen)

Die **Mach1 210** ist eine Alu-Hohlkammerfelge ohne bekanntermaßen besonders harte Flanke.
Bei ca. 20 Jahren Alter und V-Brakes ist Verschleiß wahrscheinlich.

| ☐ | Test | Gut | Schlecht → Felge/Laufrad tauschen |
|---|---|---|---|
| ☐ | **Verschleißindikator** | Mach1-Felgen haben oft eine **umlaufende Rille** oder kleine **Bohrungen** in der Bremsflanke | Rille/Bohrung verschwunden |
| ☐ | **Hohlkehl-Test** | Messschieber-Tiefenmaß oder eine gerade Kante quer auflegen: Flanke eben | Flanke konkav, Mulde messbar |
| ☐ | **Muldentiefe** | < 0,3 mm | ≥ 0,5 mm → 🔴 tauschen |
| ☐ | **Fingernagel-Test** | glatt | Stufe/Rille spürbar |

**Felgen-Ersatz-Spec** (falls nötig): **622 × 19** (ETRTO), **Alu-Hohlkammer**,
**mit Bremsflanke**, **Speichenzahl ❓ zählen** (32 oder 36), für **V-Brake**.
Die Mach1 210 gibt es weiterhin zu kaufen (💰 20–35 €) – oder ein komplettes Laufrad
mit Shimano-Nabe (💰 50–110 €).

---

## 7. Federgabel, Steuersatz, Vorbau, Lenker

| Feld | Wert |
|---|---|
| **Gabel** | ✅ **SR Suntour NEX** – Codes: **KB1E0817**, **SF14 NEX P**, **700C TS T63** |
| Interpretation der Codes | **SF14** = Suntour-Fork-Programm · **NEX** = Modell · **700C** = Laufradgröße 622 · **T63** = **63 mm Federweg** · **TS** = vermutlich **Threaded Steerer** (Gewindeschaft) · **KB1E0817** = Produktions-/Loscode |
| Schaft | **1⅛ Zoll (28,6 mm) Gewinde**, Stahl, **Gewindelänge ab Werk nur 55 mm** |
| Federung | Stahlfeder, **Vorspannung einstellbar** (Preload) |
| Gabelscheiden | **Aluminium** → Bremssockel vermutlich eingeschraubt |
| Standrohre | Stahl, Ø 28 mm |
| Achse | QR, Einbaubreite 100 mm |
| Offset | 42 mm |
| Achse bis Krone | ca. **445–477 mm** je nach Variante → ❓ **messen und mit der originalen Daytona-Gabel vergleichen** |
| Schutzblech-Öse | ✅ vorhanden (deshalb passte der Kotflügel vorne „easy") |
| **Steuersatz** | 1⅛ Zoll **Gewinde** · ⚠️ nur 1–2 Gewindegänge frei · Mutter mit Loctite gesichert |
| ❓ Steuerkopf-Typ | 🔴 **klären**: War der STAIGER-Rahmen ab Werk für **Ahead** ausgelegt? Dann sind die Rahmenschalen 34 mm (EC34) – bei 1⅛ Zoll **identisch für Gewinde und Ahead**. Prüfen: Konussitz an der Gabel **26,4 mm** (Gewinde) oder **30 mm** (Ahead)? |
| **Vorbau** | ⚠️ **Quill-Vorbau vom Spenderrad**, winkelverstellbar, Faceplate. Original war ein **XLC Comp Vorbau** (Daytona-Spec) |
| Vorbau-Einsteck-Ø | ❓ **25,4 mm** (für 1⅛ Zoll Gewindeschaft) – messen |
| 🔴 Mindesteinstecktiefe | ❓ **prüfen** – siehe Abschnitt 2 |
| **Lenker** | ⚠️ schwarzer Lenker vom Spenderrad. Original war ein **XLC Comp Alu Flatbar** |
| Lenker-Klemm-Ø | ❓ **22,2 mm im Griffbereich** (BL-M571 und SL-M580 sind für 22,2 mm) · Mitte ❓ 25,4 oder 31,8 mm |
| Lenkerbreite | ❓ ____ mm |

### 💡 Zum „ungewohnten Lenker-Gefühl"

Die Gabel-Geometrie ist **nicht** das Problem – die NEX T63 hat wie die originale Daytona-Gabel
**63 mm Federweg**. Bleiben als Ursachen:

| Ursache | Gegenmaßnahme |
|---|---|
| Breiterer + stärker gekröpfter Lenker (Original war ein **XLC Comp Alu Flatbar** = gerade, schmal) | Lenker kürzen (max. 20–30 mm pro Seite), oder den originalen Flatbar-Typ zurück |
| Anderer Vorbau (Original **XLC Comp**) | winkelverstellbaren Vorbau anders einstellen |
| **Federgabel-Vorspannung falsch** | 🔴 **Preload einstellen!** Bei zu weicher Feder sackt die Gabel weg → Geometrie ändert sich beim Fahren, Lenkung wird träge |
| Federgabel schwergängig/trocken (20 Jahre alt) | Standrohre reinigen + dünn ölen, auf Spiel prüfen |
| Sattelposition | waagerecht stellen, vor/zurück |

> 💡 **Neuer Punkt: die Federgabel selbst prüfen.** Eine 20 Jahre alte Stahlfedergabel ist oft
> trocken und schwergängig. Test: Vorderradbremse ziehen und das Rad nach vorne/unten drücken –
> die Gabel sollte **leicht einfedern und von selbst wieder ausfedern**. Klemmt sie, wirkt sich
> das direkt auf Lenkgefühl **und** auf die Bremspunkt-Position aus.
> **Standrohspflege:** mit einem fusselfreien Tuch reinigen, dünn mit Federgabel-Öl
> (z. B. Brunox Deo / R.S.P. Slick Kick) benetzen. **Nie** mit WD-40 oder Fett.

---

## 8. Weitere Bauteile

| Komponente | Verbaut | Daten |
|---|---|---|
| **Sattelstütze** | ✅ **XLC Comp** (Original-Daytona-Teil) | 🔴 **Durchmesser klären!** Original-Daytona-Spec: **XLC Comp 27,2 mm Alu**. Deine Messung „31,35 mm AD" passt **nicht** zu 27,2 mm – vermutlich hast du das **Sitzrohr außen** oder die **Sattelklemme** gemessen (31,35 mm Außendurchmesser ist plausibel für ein Sitzrohr, das eine 27,2-mm-Stütze aufnimmt). **→ Die Zahl unter der Stütze ablesen!** |
| **Schnellspanner** | ✅ **XLC Comp** | vorne 9 oder 10 mm, hinten ❓ – **Federn prüfen** (schmale Seite nach innen) |
| **Sattel** | ❓ Original Daytona: **Selle Italia X2** | ❓ prüfen |
| **Griffe** | ❓ Original Daytona: **XLC Neopren Schraubgriffe** | ❓ |
| **Pedale** | ❓ unbekannt (Original bei späteren Daytonas: Wellgo C-29) | Gewinde 9/16" × 20 tpi |
| **Licht** | ✅ Nabendynamo **DH-3N31** + Scheinwerfer + Rücklicht, Kabel neu gelötet | ✅ funktioniert |
| **Schutzbleche** | ⚠️ Metall mit V-Streben, vom Spenderrad | ❓ Freigängigkeit bei **47 mm** hinten prüfen |
| **Gepäckträger** | ❓ (Daytona wurde oft mit Träger gefahren) | ❓ |
| **Ständer** | ❓ nachgerüstet, ⚠️ Winkel zu schräg | ❓ Aufnahme messen |

---

## 9. 📐 Restliche Messliste (nur das, was noch offen ist)

| # | Messung | Wert |
|---|---|---|
| 1 | 🔴 Zähne der drei Kettenblätter (48-36-26 oder 44-32-22?) | ____/____/____ |
| 2 | 🔴 Kassette: Modellnummer + kleinstes/größtes Ritzel | ____-____ |
| 3 | 🔴 **Sattelstützen-Ø** – Zahl **unter** der Stütze (27,2 erwartet) | ____ mm |
| 4 | 🔴 **Quill-Vorbau**: liegt die MIN-INSERTION-Markierung **im** Schaftrohr? | ja/nein |
| 5 | 🔴 Liegt der Innenkeil des Vorbaus **unterhalb** des Gewindebereichs? | ja/nein |
| 6 | 🔴 Felgen-Bremsflanke v/h: Verschleißindikator + Muldentiefe | ____ / ____ mm |
| 7 | 🔴 Magnet-Test Gabelscheiden: Alu? Bremssockel mit zwei Abflachungen? | |
| 8 | Abstand Mitte Ausfallende → Mitte Bremssockel (Gabel / Hinterbau) | ____ / ____ mm |
| 9 | Länge Sockel-Bund vs. Tiefe Ausnehmung im Deore-Bremsarm | ____ / ____ mm |
| 10 | Konusschlüssel-Größen: Nabendynamo links, FH-M530 links | ____ / ____ mm |
| 11 | Kettenstrebenlänge (für die Kettenlängen-Rechnung) | ____ mm |
| 12 | Einbaubreite hinten (135 mm erwartet) | ____ mm |
| 13 | Speichenzahl v/h | ____ / ____ |
| 14 | Lenker-Klemm-Ø Mitte + Breite | ____ mm / ____ mm |
| 15 | Vorbau-Einsteck-Ø (25,4 mm erwartet) | ____ mm |
| 16 | Konussitz an der Gabel: 26,4 mm (Gewinde) oder 30 mm (Ahead)? | ____ mm |
| 17 | Achse bis Gabelkrone an der NEX (unbelastet) | ____ mm |
| 18 | Federgabel: federt sie leicht ein und aus? Preload-Einstellung? | |
| 19 | Innenlager-Abdruck (BB-ES25? Achslänge?) | |
| 20 | Nabendynamo: Spiel links bei entferntem Schnellspanner | |

## 10. 💰 Einkaufsbedarf – jetzt mit exakten Spezifikationen

| ☐ | Teil | **Exakte Spec** | Prio | ca. Preis |
|---|---|---|---|---|
| ☐ | **Kette** | **Shimano CN-HG53, 9-fach** (Original-Spec zum FC-M530), 116 Glieder | 🔴 | 12–18 € |
| ☐ | **Bremsbeläge hinten** | **Shimano V-Brake 70 mm** (M70T4 / S65T / M65T) mit Konvex-/Konkavsatz | 🔴 | 8–15 € |
| ☐ | **Bremsbeläge vorne** | dito 70 mm (für die Tektro-Zange, falls die 63er ersetzt werden sollen) | 🟡 | 8–15 € |
| ☐ | **Kontermutter 1⅛ Zoll × 24 tpi, flach** | ⚠️ **1⅛ Zoll, nicht 1 Zoll!** Zoll-Sondergewinde 1,058 mm Steigung | 🔴 | 3–10 € |
| ☐ | **Konusschlüssel** | ❓ Größen messen (Shimano typisch 15/17 mm hinten, 13/15 oder 15/17 mm vorne) | 🔴 | 8–20 € |
| ☐ | **Schnellspanner-Federn** | QR 9/10 mm, konisch | 🟡 | 1–3 € |
| ☐ | **Lagerfett** | Shimano Premium Grease | 🟡 | 6–10 € |
| ☐ | **Kettenpeitsche + Kassettenabzieher** | Shimano HG 12-Spline | 🟡 | 18–27 € |
| ☐ | **Federgabel-Öl** | Brunox Deo / R.S.P. Slick Kick (für Standrohre) | 🟡 | 8–12 € |
| ☐ | **SR Suntour NEX Threaded, Schaft 225 mm** | 700C, 63 mm, 1⅛ Zoll Gewinde, Cantilever/V-Brake-Sockel | 🟡 | 50–90 € |
| ☐ | **Oder: Ahead-Umbau** | NEX gewindelos (Schaft 255 mm) + Ahead-Steuersatz 1⅛ + Ahead-Vorbau 28,6/25,4 | 🟡 | 70–130 € |
| ☐ | **Cantisockel zum Einschrauben** | ❓ M8/M10 + Steigung, **kurzer Bund** | 🟡 | 5–15 € |
| ☐ | **Felge Mach1 210** (falls Bremsflanke durch) | **622 × 19**, Alu-Hohlkammer, ❓ Speichenzahl | 🔴 falls Verschleiß | 20–35 € |
| ☐ | **Reifen** | ❓ einheitliche Breite wählen: **47-622** Marathon Plus (v+h) oder 42-622 | 🟢 | 20–40 €/Stück |

---

## 11. Verknüpfungen

- [`../02-teile/20-steuersatz-gabel-vorbau-lenker.md`](../02-teile/20-steuersatz-gabel-vorbau-lenker.md) – Gabel, Steuersatz, Vorbau
- [`../02-teile/10-antrieb-schaltung-kette.md`](../02-teile/10-antrieb-schaltung-kette.md) – FC-M530, RD-M511, FD-C050, Kette
- [`../02-teile/30-laufrad-reifen-nabe.md`](../02-teile/30-laufrad-reifen-nabe.md) – DH-3N31, FH-M530, Mach1 210
- [`../02-teile/40-bremsen.md`](../02-teile/40-bremsen.md) – BL-M571, Bremsarme, Beläge
- [`../04-diagnose/vordere-bremsarme-sockel.md`](../04-diagnose/vordere-bremsarme-sockel.md) – Bremssockel-Problem
- [`../04-diagnose/hintere-bremse-kehrt-nicht-zurueck.md`](../04-diagnose/hintere-bremse-kehrt-nicht-zurueck.md) – Belag-Problem
- [`../04-diagnose/vorderrad-schwergaengig.md`](../04-diagnose/vorderrad-schwergaengig.md) – Nabendynamo-Lager
- [`../06-logbuch/2026-09-04-komponenten-entschluesselt.md`](../06-logbuch/2026-09-04-komponenten-entschluesselt.md) – wie die Daten entschlüsselt wurden
