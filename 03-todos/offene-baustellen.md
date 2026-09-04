# 📌 Offene Baustellen

Stand: **2026-09-05** · Quelle: zwei Zusammenfassungen + Rückfragen beim Besitzer +
**entschlüsselte Teilenummern** + **Korrektur-Runde 2026-09-05**
(siehe [`../06-logbuch/2026-09-03-rueckfrage-korrekturen.md`](../06-logbuch/2026-09-03-rueckfrage-korrekturen.md),
[`../06-logbuch/2026-09-04-komponenten-entschluesselt.md`](../06-logbuch/2026-09-04-komponenten-entschluesselt.md)
und [`../06-logbuch/2026-09-05-korrektur-runde.md`](../06-logbuch/2026-09-05-korrektur-runde.md))

---

## 🔴 Zuerst lesen: die Korrektur-Runde vom 2026-09-05

Vier bisherige Annahmen waren **falsch** und sind jetzt berichtigt. Das ändert die
Reihenfolge der Arbeiten erheblich.

| # | Was bisher in den Unterlagen stand | ⛔ Warum falsch | ✅ Was richtig ist |
|---|---|---|---|
| **1** | „Die schwarze Suntour-NEX-Gabel passt konstruktiv zum weißen Rad, das Staiger Daytona hatte ab Werk eine Suntour NCX-D LO 63 mm" | Die Prospekt-Ausstattung ist **nicht** die Ausstattung **dieses** Rads | 🔴 Die NEX ist das **Originalteil des Spenderrads**. Das Spenderrad ist ein **Bergamont Horizon 4.0** (Rahmenprägung `52 T4/T6 Heat Treated 6061 Lite Alloy` = Alu 6061 wärmebehandelt, **Größe 52 cm**). Die **Original-Gabel des weißen Rads ist eine RST Vogue TNL** – **und sie ist noch vorhanden** |
| **2** | „Hintere Bremse kehrt nicht zurück → die zu kurzen Tektro-Beläge sind der Hauptverdächtige" | Die Beläge haben mit der Rückstellkraft des **Hebels** nichts zu tun | ✅ **Ursache gefunden:** die **Bremshebel-Klemmschellen** waren am Lenker **zu nah/zusammen zu fest** angezogen → der **Angelpunkt (Pivot) des hinteren Bremshebels** wurde geklemmt → **behoben** |
| **3** | „Die Bremssockel-Stifte der Spenderrad-Gabel sind **länger** → Sockel **2–2,5 mm zurückdrehen**" | ⛔ **Richtung falsch.** Zurückdrehen würde das Problem **verschlimmern** | 🔴 Die Stifte sind **KÜRZER** → die **M6-Befestigungsschraube der Shimano-Arme findet keinen Gewindegriff** im Stift. Fix: **längere M8-Cantistifte** (brake-stuff.de **CS-M8-VA**, 14,90 €/Paar, listet **Staiger**), kürzere Armschraube oder Stifte der RST-Gabel |
| **4** | „Steuerrohr-Differenz ca. 23 mm" (geschätzt) | – | ✅ **von dir gemessen: 20–30 mm.** Der **Bergamont-Vorbau ist über dem Steuersatz länger und oben einstellbar** → die **Lenkerhöhe** stimmt, aber ⛔ **nicht die Schaftlänge** |

💡 **Die wichtigste neue Erkenntnis:**

> **Baustelle #14 (RST Vogue TNL retten) ist der Schlüssel zu Baustelle #1, #5 und #6.**
> Die Original-Gabel ist für **dieses** Steuerrohr gebaut → Schaftlänge stimmt,
> Bremssockel passen zu den weißen Shimano-Armen, Gewindelänge reicht.
> **Erster Arbeitsschritt überhaupt: der Fingernageltest an den Standrohren (5 min, 0 €).**

**Legende:** 🔴 hoch (Sicherheit/Funktion) · 🟡 mittel · 🟢 niedrig (Komfort/Optik)
Status: `🔴 offen` · `🟠 in Arbeit` · `🟡 Diagnose fehlt` · `✅ erledigt` · `🟢 entwarnt`

---

## Übersicht (Priorisierung Stand 2026-09-05)

| # | Baustelle | Prio | Status | Nächster konkreter Schritt | Detail |
|---|---|---|---|---|---|
| **14** | 🆕 **RST Vogue TNL retten?** (Original-Gabel, noch vorhanden) | 🔴 | 🔴 **offen – hat Vorrang** | 🔴 **Fingernageltest** an den Standrohren + **Standrohr-Ø messen** (25,4 oder 28,6 mm?) + Schaftlänge messen | [`../04-diagnose/rst-vogue-tnl-federgabel.md`](../04-diagnose/rst-vogue-tnl-federgabel.md) |
| 1 | 🔴 **Quill-Vorbau-Mindesteinstecktiefe** | 🔴 | 🔴 offen | Markierung suchen, prüfen ob sie **im** Schaftrohr liegt. Vorbau-Einsteckteil muss **25,4 mm** haben (1⅛″-Schaft). 🔴 **durch die 20–30 mm Steuerrohr-Differenz kritischer geworden** | [`../02-teile/20-steuersatz-gabel-vorbau-lenker.md`](../02-teile/20-steuersatz-gabel-vorbau-lenker.md) Abs. 3b + 6 |
| 2 | 🔴 **Felgen-Bremsflanken** prüfen (v + h) | 🔴 | 🔴 offen | Verschleißindikator + Muldentiefe messen. 🔴 **Neues Indiz: die Original-Shimano-Beläge (ca. 72 mm) waren komplett durchgefahren** | [`../02-teile/30-laufrad-reifen-nabe.md`](../02-teile/30-laufrad-reifen-nabe.md) Abs. 2.3 |
| 6 | 🔴 **Steuersatz-Gewinde** – dauerhafte Lösung | 🔴 | 🔴 offen | 🔴 **Steuerrohrlänge + Schaftlänge messen** → dann **Variante A+ (RST zurück)**, **A0 (NEX 225 mm)** oder **D (Ahead)** | [`../02-teile/20-steuersatz-gabel-vorbau-lenker.md`](../02-teile/20-steuersatz-gabel-vorbau-lenker.md) Abs. 3a/3b/4 |
| 5 | 🔴 **Vordere Bremssockel-Stifte zu kurz** | 🔴 | 🔴 **Ursache korrigiert** | 🔴 **Stift-Überstand messen** + Gewinde M8 prüfen → **längere M8-Cantistifte** (CS-M8-VA, 14,90 €/Paar). ⛔ **Nicht zurückdrehen!** Wird mit #14 ggf. überflüssig | [`../04-diagnose/vordere-bremsarme-sockel.md`](../04-diagnose/vordere-bremsarme-sockel.md) |
| 7 | Neue Kette (Kette zu kurz) | 🟡 | 🔴 offen | Big-Big-Test, Kettenstrebenlänge messen, **Shimano CN-HG53 9-fach** bestellen | [`../02-teile/10-antrieb-schaltung-kette.md`](../02-teile/10-antrieb-schaltung-kette.md) |
| 3a | 🟡 **Hintere Beläge zu kurz** (63 mm statt 72 mm) | 🟡 | 🟠 offen, **kein Sicherheitsproblem** | Beim nächsten Belagwechsel: **Shimano M70T4 = 72 mm** mit korrektem Scheibensatz | [`../04-diagnose/hintere-bremse-kehrt-nicht-zurueck.md`](../04-diagnose/hintere-bremse-kehrt-nicht-zurueck.md) Abs. 0a |
| 4a | 🟡 **Verlorene Feder am Hinterrad** | 🟡 | 🟠 offen | Feder identifizieren (**Wellenscheibe** oder **QR-Feder**?) → bei Bedarf ersetzen | [`../04-diagnose/hinterrad-lager-feder.md`](../04-diagnose/hinterrad-lager-feder.md) Teil 2 |
| 12 | Testfahrt + Gesamtcheck | 🟡 | 🔴 offen | [`sicherheitscheck.md`](sicherheitscheck.md) | |
| 10 | Teile identifizieren + Stammdaten ausfüllen | 🟢 | ✅ **~95 % erledigt** | 🔴 Nur noch offen: **Kassette**, **Kettenblatt-Zähne**, **RST-Standrohr-Ø**, **Schaftlängen**, **Sattelstützen-Ø** | [`../04-messdaten/messdatenblatt.md`](../04-messdaten/messdatenblatt.md) |
| 11 | Kassette vom Spenderrad lösen (optional) | 🟢 | 🔴 offen | **Kettenpeitsche** besorgen – ohne die dreht sich das Paket mit | [`../02-teile/10-antrieb-schaltung-kette.md`](../02-teile/10-antrieb-schaltung-kette.md) Abs. 4 |
| 8 | Ständer-Winkel zu schräg | 🟢 | 🔴 offen | Kipprichtung klären, Lochabstand messen, Distanzscheiben | [`../02-teile/70-staender-gepaecktraeger.md`](../02-teile/70-staender-gepaecktraeger.md) |
| 9 | Lenker-Ergonomie / Sitzposition | 🟢 | 🟢 niedrig | Erst nach 3–5 Fahrten bewerten. ⚠️ **Begründung korrigiert** (siehe Detail) | [`../02-teile/20-steuersatz-gabel-vorbau-lenker.md`](../02-teile/20-steuersatz-gabel-vorbau-lenker.md) Abs. 7 |
| **3** | ~~Hintere Bremse kehrt nicht zurück~~ | – | ✅ **ERLEDIGT** | Ursache: **Bremshebel-Klemmung am Lenker** – behoben | Archiv unten |
| **4** | ~~Hinterrad läuft schwer~~ | – | ✅ **ERLEDIGT** | *„läuft normal, hat sich wohl eingespielt"* | Archiv unten |
| **13** | ~~Nabendynamo-Lagervorspannung~~ | – | ✅ **ERLEDIGT** | Rad läuft **mehrere Umdrehungen** nach = Sollbereich | Archiv unten |

---

## 💡 Der Synergie-Effekt: eine Maßnahme, vier Baustellen

Baustelle **14** (RST Vogue TNL retten) ist der Hebel für **1, 5 und 6** – alle drei haben
dieselbe Wurzel: **die fremde Bergamont-Gabel in einem Staiger-Rahmen mit längerem Steuerrohr.**

| Baustelle | Problem | 🔴 Genaue Wurzel |
|---|---|---|
| **1** | Quill-Vorbau erreicht die Mindesteinstecktiefe evtl. nicht | NEX-Schaft ist für ein **20–30 mm kürzeres** Steuerrohr gekürzt; der lange Bergamont-Vorbau **braucht mehr** Schaft, nicht weniger |
| **5** | Die guten weißen **Deore**-Bremsarme lassen sich nicht sicher befestigen | Die **Cantistifte der Bergamont-Gabel sind kürzer** → die M6-Armschraube findet **keinen Gewindegriff** im Stift |
| **6** | Zu wenig Gewinde für die Kontermutter | NEX-Gewindeschäfte haben ab Werk nur **ca. 55 mm Gewinde oben**; gekürzt für das **kürzere Bergamont-Steuerrohr** → STAIGER-Steuerrohr ist **20–30 mm länger** |
| **14** | Original-Gabel defekt (Öl raus, Dichtungen hin, leichter Rost) | Staubschabring/Spiralfeder ausgefallen → Öl aus dem **Öldämpfungsbein** → nur die **Coil-Feder** arbeitet |

### Vier Wege – Bewertung

| Weg | Was | Aufwand | 💰 | Bewertung |
|---|---|---|---|---|
| **A+** ⭐ | 🔴 **RST Vogue TNL zurückbauen** (Dichtungen + Öl + Standrohre polieren) | ca. 1–1,5 h | **25–50 €** | 💡 **Beste Lösung** – löst **1 + 5 + 6 + Höhenproblem** auf einmal. **Bedingung: Standrohre bestehen den Fingernageltest** |
| **A0** | Neue NEX-Gabel mit **225-mm-Schaft** + **längere M8-Cantistifte** | ca. 2 h | **65–105 €** | ✅ Gut, behält Schutzblech-Ösen + 63-mm-Geometrie. ⚠️ +15 mm Schaft reicht bei 20–30 mm Differenz **allein nicht** |
| **C** | 🔴 **Ahead-Umbau** (NEX Ahead 255 mm + Ahead-Steuersatz + Ahead-Vorbau) | ca. 2 h | 70–130 € | ✅ **Dauerhafteste Lösung** – **EC34-Lagerschalen bleiben im Rahmen!** |
| **E** | 🟢 **Riser-Lenker** mit mehr Rise + Staiger-Originalvorbau | ca. 30 min | **20–40 €** | ✅ Billigste Höhenlösung – löst aber **nicht** #5 und #6 |

⛔ **Was nicht geht:** Quill-Vorbau kürzen (schwächt den Schaft, Bruchgefahr).

**Falls Weg A+ (RST zurück):** Neu lösen müsstest du nur
- **Schutzblech-Befestigung vorne** (die NEX hatte die passenden Ösen) →
  **Universal-Schellen / P-Schellen**, 💰 3–8 €
- **Geometrie prüfen**: RST Vogue ≈ **50 mm** Federweg (axle-to-crown ca. **455–465 mm**) vs.
  NEX **63 mm** (ca. **445–469 mm**) → die Differenz ist **klein**, aber bitte messen

**⚠️ Baustelle 9 – Begründung korrigiert:** Die alte Entwarnung („das Staiger Daytona hatte
ab Werk eine Suntour 63 mm, also passt die NEX") ist **hinfällig**, weil **dein** weißes Rad
eine **RST Vogue TNL mit ca. 50 mm** hatte. Die NEX ist damit **ca. 0–20 mm höher** in der
Einbauhöhe → Lenkwinkel minimal flacher, Tretlager minimal höher. **Praktisch kaum spürbar**,
aber das „ungewohnte Lenker-Gefühl" kommt wahrscheinlicher vom **breiteren Bergamont-Riser**
(typisch **30–33° Backsweep**) und dem **anderen Vorbau**. ❓ Trotzdem messen:
**axle-to-crown** beider Gabeln.

---

## Empfohlene Reihenfolge der Werkstatt-Sessions

Nicht alles auf einmal. Diese Reihenfolge minimiert Umbauten und Kosten.

### Session 1 – Diagnose & Messen (60–90 min, kaum Werkzeug, 0 €)

**Ziel: nichts reparieren, nur herausfinden.** Danach weißt du, was du bestellen musst.

1. 🔴 **Fingernageltest an der RST Vogue TNL** – Grübchen (Pitting) an den Standrohren?
   → **entscheidet über Weg A+ oder A0/C** → Baustelle **14**
2. 🔴 **RST-Standrohr-Ø messen** (25,4 oder 28,6 mm?) → bestimmt den Dichtungssatz → **#14**
3. 🔴 **RST-Schaftlänge messen** (Krone → Schaftspitze) + Gewindelänge → **#14 / #6**
4. 🔴 **Steuerrohrlänge STAIGER** + **Steuerrohrlänge Bergamont** (A und B, Soll Δ 20–30 mm) → **#1 / #6**
5. 🔴 **Quill-Vorbau-Einstecktiefe** prüfen + **Vorbau-Einsteck-Ø** (muss **25,4 mm** sein!) → **#1**
6. 🔴 **Bremssockel vorne messen**: **Stift-Überstand** über die Gabelscheide, Gewinde **M8**,
   Gesamtlänge, Einschraublänge → **#5**
7. 🔴 **Felgen-Bremsflanken** prüfen (v + h): Verschleißindikator, Muldentiefe, scharfe Kante → **#2**
8. 💡 **Federraste vorne** in ein anderes der 3 Löcher setzen → **#5** (0 €)
9. Hinterrad: **verlorene Feder identifizieren** (Wellenscheibe? QR-Feder?) → **#4a**
10. Restliche Modellnummern fotografieren: **Kassette**, **Kettenblatt-Zähne**,
    **Pedale**, **Sattelstütze unter der Klemme**, **RST-Gabel-Aufkleber** → **#10**
11. Konusschlüssel-Größen messen (Nabendynamo links, FH-M530 links)
12. **Axle-to-crown** beider Gabeln messen → **#9**

**Output:** ausgefülltes Messdatenblatt + [`Einkaufsliste`](einkaufsliste.md)

### Session 2 – Bestellen (0 min Werkstatt)

Aus der [`Einkaufsliste`](einkaufsliste.md) bestellen. Wartezeit für Session 3 nutzen.
🔴 **Erst bestellen, wenn Session 1 die Maße geliefert hat** – sonst passt der Dichtungssatz
oder die Cantistifte nicht.

### Session 3 – Gabel (60–120 min) – **der entscheidende Schritt**

1. 🔴 **RST Vogue TNL zerlegen, reinigen, Standrohre polieren, Dichtungen + Öl neu** → **#14**
2. Gabel zurückbauen, **crown race** umsetzen, **Steuersatz neu einstellen** → **#6 erledigt**
3. **Weiße Shimano-Deore-Bremsarme vorne montieren** → **#5 erledigt**
4. **Vorbau-Einstecktiefe** kontrollieren (MIN-INSERTION-Marke **im** Rohr) → **#1 erledigt**
5. Schutzblech vorne neu befestigen (Universal-/P-Schellen)
6. **Falls die RST unrettbar ist:** Weg **A0** (NEX 225 mm) oder **C** (Ahead) + **längere
   M8-Cantistifte** für die weißen Arme

### Session 4 – Bremsen feinjustieren (30–45 min)

1. **Bremshebel-Position + Klemmmoment** am Lenker kontrollieren (4–6 Nm, Abstand zwischen
   den Klemmungen) → **Wiederholung von #3 vermeiden**
2. Vorne/hinten zentrieren, Federspannung, Zugspiel → [`../05-anleitungen/bremsen-einstellen.md`](../05-anleitungen/bremsen-einstellen.md)
3. 🟡 **Hintere Beläge** bei Bedarf auf **Shimano M70T4 = 72 mm** wechseln → **#3a**

### Session 5 – Neue Kette (45 min)

1. Länge **neu berechnen** (⚠️ nicht die alte Kette als Maß nehmen!), kürzen, montieren → **#7**
2. Big-Big-Test wiederholen, Schaltung neu justieren

### Session 6 – Kleinkram (30 min)

1. Ständer-Winkel → **#8** · 2. Lenker-Ergonomie bewerten → **#9** · 3. Schutzbleche final

### Session 7 – Testfahrt

[`Sicherheitscheck`](sicherheitscheck.md) durchgehen, dann längere Probefahrt. → **#12**

---

## Baustellen-Detail (Arbeitskopie)

### 14. 🆕🔴 RST Vogue TNL – retten oder verschrotten?

| Feld | Wert |
|---|---|
| Was ist das | **Original-Federgabel des weißen Staiger-Rads** – **RST Vogue TNL**, Coil/Öl |
| Warum wichtig | 🔴 **Löst Baustelle 1, 5 und 6 gleichzeitig**, wenn sie wieder funktioniert |
| Aufbau | **Öldämpfung rechts** / **Stahlfeder + MCU links**, **hydraulischer Lockout**, Vorspannung einstellbar |
| Schaft | **28,6 mm (1⅛″)** oder 25,4 mm (1″) **CroMo** – ❓ messen |
| Standrohre | **25,4 mm Stahl, Ti-Farbe** (Katalog 2008) – 🔴 **Ø messen** für den Dichtungssatz |
| Tauchrohre | **Aluminium** |
| Federweg | ca. **50 mm** (RST-Vogue-Baureihe), axle-to-crown ca. **455–465 mm** |
| Symptom | Gabel **gibt nach, aber nur die Feder** – keine Dämpfung mehr |
| 🔴 Ursache | **Staubschabring / Spiralfeder ausgefallen** → **Öl aus dem Dämpfungsbein ausgetreten** → nur die Coil-Feder arbeitet. Dazu **leichter Rost** an den Standrohren |
| 🔴 **Entscheidungskriterium** | **Fingernageltest:** Fängt der Fingernagel an einer Roststelle → **Grübchen (Pitting)** = ⛔ **unrettbar** (neue Dichtungen laufen auf rauher Fläche sofort wieder aus). Bleibt der Nagel nicht hängen → ✅ **rettbar** |
| 💰 Teile (falls rettbar) | **RST Dust Seal Kit – Paar, 14,28 €** (bike24) · **Gabelöl 5W–10W**, 8–12 € · **Chrompolitur / Stahlwolle 0000**, ca. 5 € → **gesamt 25–50 €** |
| Vertrieb | **Paul Lange & Co.** = RST-Vertrieb Deutschland (führt Vogue-Ersatzteile inkl. TNL-Lockout-Kappen) |
| ⚠️ Falle | 🔴 **Nicht die moderne „RST Vogue Air" bestellen** – anderes Produkt. Und: **erst Ø messen**, die 28,6-mm-Variante des Dichtungssatzes ist für Vogue/VIVair/F1RST, die 30-mm-Variante für Omega/Blaze |
| Fallback (falls unrettbar) | NEX mit **225-mm-Schaft** (Weg A0) oder **Ahead-Umbau** (Weg C) oder **gebrauchte 1⅛″-Gewindegabel** mit ≥ Steuerrohr + 30 mm + Einstecktiefe |
| Detail | [`../04-diagnose/rst-vogue-tnl-federgabel.md`](../04-diagnose/rst-vogue-tnl-federgabel.md) |
| Ergebnis | ❓ |

### 1. 🔴 Quill-Vorbau-Mindesteinstecktiefe

| Feld | Wert |
|---|---|
| Symptom | Gabelschaft steht nur **1–2 Gewindegänge** über → Schaft ist sehr kurz |
| 🔴 Verschärft durch | **Steuerrohr des Staiger-Rahmens ist 20–30 mm länger** als das des Bergamont-Rahmens; der **Bergamont-Vorbau ist über dem Steuersatz länger** → braucht **mehr** Schaft |
| Risiko | Steht die „MIN INSERTION"-Markierung **über** der Schaftoberkante, wirkt eine große Hebelkraft an der Schaftkante → 🔴 **Gabelschaft-Bruch, schwerer Unfall** |
| Prüfung | Markierung am Vorbau suchen → messen, wie tief das Einsteckteil im Schaftrohr sitzt. **Einsteck-Ø muss 25,4 mm sein** (1⅛″-Schaft!) |
| Falls zu flach | 🔴 **nicht fahren.** Lösung: **RST Vogue TNL zurück** (Weg A+), Gabel mit längerem Schaft, oder Ahead-Vorbau (klemmt außen) |
| Detail | [`../02-teile/20-steuersatz-gabel-vorbau-lenker.md`](../02-teile/20-steuersatz-gabel-vorbau-lenker.md) Abs. 3b + 6 |
| Ergebnis | ❓ |

### 2. 🔴 Felgen-Bremsflanken

| Feld | Wert |
|---|---|
| Symptom | Bremsflanken am weißen Rad waren abgefahren; Original-Hinterrad ist wieder eingebaut |
| 🔴 **Neues Indiz (2026-09-05)** | Die **Original-Shimano-Beläge (ca. 72 mm) waren komplett durchgefahren** – *„mehr als nur abgefahren, die waren durch"*. Wer Beläge durchfährt, fährt meist auch die **Felgenflanke** an |
| Risiko | **Felgendurchbruch** unter Bremsdruck (Felgenplatzer) – 🔴 sicherheitsrelevant |
| Felgen | hinten **Mach1 210** (622 × 19c, Alloy 6060, original Daytona) · vorne **Shining Double Wall A-M4** (622 × 19, vom Bergamont-Spenderrad) |
| Prüfung | Verschleißindikator sichtbar? Muldentiefe messen (Tiefe mit Haarlineal/Münze)? Kante mit dem Fingernagel prüfen? Felge **konkav** (eingedellt)? |
| Ersatz | Mach1 210 weiterhin lieferbar (💰 20–35 €) – oder **Felge neu einspeichen** lassen (💰 60–110 €) |
| Detail | [`../02-teile/30-laufrad-reifen-nabe.md`](../02-teile/30-laufrad-reifen-nabe.md) Abs. 2.3 |
| Ergebnis | ❓ |

### 5. 🔴 Vordere Bremsarme passen nicht auf den Bremssockel – **Ursache korrigiert**

| Feld | Wert |
|---|---|
| Symptom | Die weißen **Shimano Deore**-Bremsarme lassen sich nicht richtig auf dem Sockel der Bergamont-Gabel befestigen |
| ❌ **Nicht** das Problem | Die Bremshebel am Lenker – die sind die **originalen weißen BL-M571** und in Ordnung |
| ⛔ **Zurückgezogen** | „Sockel-Bund **länger** → Sockel **2–2,5 mm zurückdrehen**." **Falsch – das verschlimmert es.** |
| 🔴 **KORRIGIERTE URSACHE** | Die **Cantistifte der Bergamont-Gabel sind KÜRZER** als die der Staiger-Originalgabel → die **M6-Befestigungsschraube** greift **nicht tief genug ins Innengewinde des Stifts** → Arm hat Spiel / lässt sich nicht festziehen |
| Befund zusätzlich | 🔴 **Beide Gabeln sind Alu** (Bergamont: Suntour NEX · Staiger: RST Vogue) → die Stifte sind **eingeschraubt** (M8), also **tauschbar** ✅ |
| Stift-Ø | **7,95 mm gemessen = M8** → **M8-Cantistifte** bestellen (nicht M10!) |
| 🎯 **Lösung A (empfohlen)** | 🔴 **Längere M8-Cantistifte einschrauben** – **brake-stuff.de CS-M8-VA**, **14,90 €/Paar** (M8, Ø8, **M6-Innengewinde**, Einschraublänge **10 mm**, **5–6 Nm**, **listet ausdrücklich Staiger**). Alternative: **CS-M8-RST** 16 € (verlängertes Gewinde + Zusatzflansch) – 🔴 **für RST-Gabeln entwickelt** |
| 🎯 Lösung B | **Kürzere M6-Armschraube** verwenden, falls der Stift genug Innengewinde hat (💰 1–3 €) |
| 🎯 Lösung C | **Cantistifte der RST Vogue TNL übernehmen** – wenn die RST verschrottet wird, sind ihre Stifte **die passenden** (💰 0 €) |
| 💡 Lösung D | **Federraste**: Federstift in ein **anderes der 3 Löcher** im Bremssockel (beide Arme ins gleiche Loch) – verbessert die **Rückstellkraft**, nicht den Gewindegriff |
| ✅ **Lösung E (0 €)** | 🔴 **Weg A+: RST Vogue TNL zurückbauen** – dann passen die weißen Arme **ohne jede Änderung** |
| 🔴 Montage der Stifte | Loch reinigen/entfetten, **Loctite 243**, **5–6 Nm**, **2–3 h warten**. Datenblatt-PDF von brake-stuff.de nennt **Gesamtlänge + Einschraublänge** → **Gesamtlänge vergleichen!** |
| Detail | [`../04-diagnose/vordere-bremsarme-sockel.md`](../04-diagnose/vordere-bremsarme-sockel.md) |
| Ergebnis | ❓ |

### 6. 🔴 Steuersatz-Gewinde – dauerhafte Lösung (sicherheitsrelevant)

| Feld | Wert |
|---|---|
| Symptom | nur **1–2 Gewindegänge** frei → keine Kontermutter möglich |
| 🔴 **URSACHE (bestätigt durch Messung)** | Gabel = **SR Suntour NEX SF14 NEX P 700C TS T63** vom **Bergamont Horizon 4.0**. NEX-Gewindeschäfte (210/225 mm) haben ab Werk **nur ca. 55 mm Gewinde – am oberen Ende**. Der Schaft wurde für das **kürzere Bergamont-Steuerrohr oben gekürzt** → Gewinde weg. Das **STAIGER-Steuerrohr ist 20–30 mm länger** → nur noch 1–2 Gänge übrig |
| Daten | Schaft **1⅛″ = 28,6 mm**, **24 tpi** (1,058 mm Steigung), Schaftlängen ab Werk **210 / 225 mm**, axle-to-crown **445–469 mm** |
| Aktuell | Mutter + **Loctite 243**, regelmäßige Kontrolle – ⚠️ **Provisorium** |
| ⚠️ Hinweis | Loctite wirkt **nicht auf fettigem Gewinde** → vorher entfetten, 24 h aushärten |
| 🎯 Dauerhaft (empfohlen) | 🔴 **Weg A+: RST Vogue TNL zurückbauen** – Schaft passt garantiert (war original in diesem Rahmen) |
| Dauerhaft (Plan B) | **NEX-Gabel mit 225-mm-Schaft** (+15 mm, 💰 50–90 €) – ⚠️ bei 20–30 mm Differenz **allein nicht genug** |
| Dauerhaft (modern) | **Ahead-Umbau**: NEX Ahead **255 mm** + Ahead-Steuersatz **EC34/28,6 – EC34/30** + Ahead-Vorbau (💰 70–130 €). 💡 **Die EC34-Lagerschalen sind bei 1⅛″-Gewinde- und Ahead-Steuersatz identisch → bleiben im Rahmen!** |
| Billig, aber unzureichend | **flache Steuersatz-Mutter 1⅛″ × 24 tpi** – bringt ca. 5 mm. ⚠️ Kein Metrik-Gewinde, nicht aus dem Baumarkt! |
| 🔴 Vorher messen | **Steuerrohrlänge STAIGER** + **Schaftlänge NEX** + **Schaftlänge RST** + freies Gewinde |
| Detail | [`../02-teile/20-steuersatz-gabel-vorbau-lenker.md`](../02-teile/20-steuersatz-gabel-vorbau-lenker.md) Abs. 3a, 3b, 4 |
| Ergebnis | ❓ |

### 7. Neue Kette 🟡

| Feld | Wert |
|---|---|
| Symptom | Kette durch Reparatur ~½–1 Glied zu kurz |
| Risiko | Big-Big überstreckt das Schaltwerk → Schaltauge/Käfig-Schaden |
| 🔴 **Exakte Spec** | ✅ **Shimano CN-HG53, 9-fach** – Original-Kette zur **Kurbelgarnitur FC-M530** (alternativ CN-HG73 oder KMC X9). 116 Glieder, selbst kürzen. 💰 12–18 € |
| ⚠️ Begriff | **FC-M530 = Kurbelgarnitur** (crankset), **nicht** Pedale |
| Lösung | Länge **neu berechnen** (⚠️ **nicht** die alte Kette als Maß nehmen!). Dazu: Kettenstrebenlänge + Zähne großes Kettenblatt + Zähne größtes Ritzel |
| ⚠️ Grenze | Schaltwerk **RD-M511**: max. größtes Ritzel **34 Zähne**, Gesamtkapazität **45 Zähne** → bei 48-36-26 + 11-32 = 43 ✅, **kein Spielraum für größere Kassetten** |
| Innenlager | **BB-ES25**, BSA **68 mm**, **Octalink** (passt zur FC-M530) |
| Detail | [`../02-teile/10-antrieb-schaltung-kette.md`](../02-teile/10-antrieb-schaltung-kette.md) Abs. 3 |
| Ergebnis | ❓ |

### 3a. 🟡 Hintere Bremsbeläge zu kurz (Restthema aus Baustelle 3)

| Feld | Wert |
|---|---|
| Befund | Verbaut: **Tektro 836**, gemessen **62 mm** (Nennlänge 63 mm) in einer **Shimano-Deore-Zange** |
| 🔴 Neu bekannt | Die **ursprünglichen Shimano-Beläge** waren **ca. 72 mm** und **komplett durchgefahren** |
| Codes | **B1** (links) / **B44** (rechts) → ✅ **aufgeklärt**: sehr kleine, schwer lesbare Prägung, **vermutlich Chargennummer**. Alle vier Beläge sehen **absolut identisch** aus → **keine** unterschiedlichen Mischungen, **kein** Reibwert-Problem |
| Bewertung | 🟡 **Kein Sicherheitsproblem.** Ca. **12–14 % weniger Auflagefläche** → etwas weniger Bremsleistung + ungleichmäßigerer Felgenverschleiß |
| Empfehlung | Beim nächsten Belagwechsel: **Shimano V-Brake-Beläge M70T4 = 72 mm** (💰 8–15 €/Paar) **mit korrektem Shimano-Scheibensatz** |
| Detail | [`../04-diagnose/hintere-bremse-kehrt-nicht-zurueck.md`](../04-diagnose/hintere-bremse-kehrt-nicht-zurueck.md) Abs. 0a · [`../02-teile/40-bremsen.md`](../02-teile/40-bremsen.md) Abs. 3 |
| Ergebnis | ❓ |

### 4a. 🟡 Verlorene Feder am Hinterrad (Restthema aus Baustelle 4)

| Feld | Wert |
|---|---|
| Befund | Beim Achsausbau ging **eine kleine Feder verloren** – jetzt ist nur noch **eine Seite** vorhanden |
| ✅ Erledigt | Das **Laufverhalten** – *„mein Hinterrad läuft normal, hat sich wohl eingespielt"* |
| 💡 Kandidaten | **Wellenscheibe (wave washer)** oder **Schnellspanner-Feder (QR spring)** – Nabe ist **Shimano Deore FH-M530 (VIAM)** → Explosionszeichnung recherchierbar |
| 💡 These | Wenn die **QR-Feder** fehlt, verkantet der Schnellspanner beim Spannen und **drückt das Lager zusammen** → kann bei Belastung wiederkommen |
| Vorgehen | **QR komplett entfernen** und Rad drehen → läuft es frei? Dann liegt es am QR. Feder über Explosionszeichnung identifizieren |
| Nachkontrolle | 🟢 nach ca. **100 km**: Spiel + Leichtgängigkeit prüfen |
| Detail | [`../04-diagnose/hinterrad-lager-feder.md`](../04-diagnose/hinterrad-lager-feder.md) |
| Ergebnis | ❓ |

### 8. Ständer zu stark geneigt 🟢

| Feld | Wert |
|---|---|
| Symptom | Rad kippt fast von selbst |
| Vergleich | alter Ständer war zu aufrecht |
| Lösung | Distanzscheiben unter eine Seite (1 mm ≈ 1,4° bei 40 mm Lochabstand), Längenverstellung, oder KSA-40-Montage |
| Offene Frage | **In welche Richtung kippt das Rad?** (zum Ständer hin / weg) |
| Detail | [`../02-teile/70-staender-gepaecktraeger.md`](../02-teile/70-staender-gepaecktraeger.md) |
| Ergebnis | ❓ |

### 9. Lenker-Gefühl ungewohnt 🟢

| Feld | Wert |
|---|---|
| Symptom | breiterer, geschwungener Lenker → andere Sitzposition/Hebelwege |
| ⚠️ Korrektur | Die alte Entwarnung („Daytona hatte ab Werk Suntour 63 mm") gilt **nicht** – dein Rad hatte eine **RST Vogue TNL mit ca. 50 mm** |
| Bewertung | Die NEX ist ca. **0–20 mm höher** (axle-to-crown 445–469 mm vs. RST ca. 455–465 mm) → **praktisch kaum spürbar**. Wahrscheinlichere Ursache: der **Bergamont-Riser** (typisch **30–33° Backsweep**, breiter) + **anderer Vorbau** |
| Plan | 3–5 Fahrten, dann bewerten. Einstellmöglichkeiten ohne Teiletausch: Vorbauwinkel/-höhe, Lenker drehen, Hebelposition, Sattelposition |
| Detail | [`../02-teile/20-steuersatz-gabel-vorbau-lenker.md`](../02-teile/20-steuersatz-gabel-vorbau-lenker.md) Abs. 7 |
| Ergebnis | ❓ |

### 10. Teile identifizieren & dokumentieren 🟢 (~95 % erledigt)

| Teilschritt | Erledigt |
|---|---|
| ✅ Hersteller weißes Rad: **STAIGER** (Daytona Sportline, 3×9, Alu 6061) | ☑ |
| ✅ Spenderrad: **Bergamont Horizon 4.0** – Prägung `52 T4/T6 Heat Treated 6061 Lite Alloy` (Alu 6061 T4/T6, Größe 52 cm) | ☑ |
| ✅ Original-Gabel weißes Rad: **RST Vogue TNL** | ☑ |
| ✅ Gabel jetzt: **SR Suntour NEX SF14 NEX P 700C TS T63** | ☑ |
| ✅ Naben: **DH-3N31-NT** (vorne) / **Deore FH-M530 VIAM** (hinten) | ☑ |
| ✅ Felgen: **Shining A-M4** (vorne) / **Mach1 210** (hinten) | ☑ |
| ✅ Bremshebel: **BL-M571** · Schalthebel **SL-M580** · Kurbel **FC-M530** · Schaltwerk **RD-M511** | ☑ |
| ✅ Beläge hinten: **Tektro 836**, 62 mm; Codes **B1/B44** = Chargennummer | ☑ |
| ❓ **Kassette** – Modell + Abstufung | ☐ |
| ❓ **Kettenblatt-Zähne** (vorne) | ☐ |
| ❓ **RST-Standrohr-Ø** (25,4 / 28,6 mm) + **Schaftlänge** | ☐ |
| ❓ **Sattelstützen-Ø** (Bergamont-Serie: 27,2 mm) | ☐ |
| ❓ **Baujahr** Bergamont (V-brake-Version, 3×8 → ca. 2012–2016) | ☐ |
| ❓ **Speichenzahlen** (beide Räder) | ☐ |
| [`Messdatenblatt`](../04-messdaten/messdatenblatt.md) ausfüllen | ☐ |

### 11. Kassette vom Spenderrad lösen (optional) 🟢

| Feld | Wert |
|---|---|
| Symptom | „Lockring hat nichts gebracht, Ritzel haben sich nicht bewegt" |
| 💡 **Erklärung** | Ohne **Kettenpeitsche** dreht sich das Ritzelpaket einfach mit – exakt dieses Symptom. Der Lockring braucht **30–50 Nm** |
| Vorher klären | Ist es eine **Kassette** (Lockring, 12-Spline) oder ein **Schraubkranz** (freewheel, aufgeschraubt)? Anderes Werkzeug! ⚠️ Das Bergamont Horizon 4.0 ist **3×8** → wahrscheinlich **8-fach-Kassette** |
| Notlösung | alte Kette um ein großes Ritzel wickeln + Knebel als Hebel |
| Bewertung | 🟢 **Nicht dringend.** Das Original-Hinterrad läuft, die 9-fach-Kassette passt zur Schaltung |
| Detail | [`../02-teile/10-antrieb-schaltung-kette.md`](../02-teile/10-antrieb-schaltung-kette.md) Abs. 4 |
| Ergebnis | ❓ |

### 12. Testfahrt + Gesamtcheck 🟡

| Feld | Wert |
|---|---|
| Voraussetzung | 🔴 Baustelle **1, 2, 5, 6** müssen erledigt oder bewusst abgenommen sein – **das sind Sicherheitsbaustellen** |
| Ablauf | [`sicherheitscheck.md`](sicherheitscheck.md) |
| Ergebnis | ❓ |

---

## ✅ Erledigt (Archiv)

### Erledigt am 2026-09-04 / 09-05 (durch Rückfrage geklärt)

| # | Baustelle | ✅ Ursache / Lösung |
|---|---|---|
| **3** | Hintere Bremse kehrt nicht zurück | 🔴 **Bremshebel-Klemmschellen am Lenker zu nah/fest** → **Angelpunkt (Pivot) des hinteren Bremshebels geklemmt**. ⛔ **Nicht** die Beläge. **Behoben.** → Restthema **#3a** |
| **4** | Hinterrad läuft schwerer | Lager hat sich **gesetzt/eingespielt** – *„läuft normal"*. **Nachkontrolle nach ca. 100 km.** → Restthema **#4a** (verlorene Feder) |
| **13** | Vorderrad / Nabendynamo schwergängig | Rad läuft frei hängend **mehrere Umdrehungen** nach = **Sollbereich** für ein Nabendynamo-Rad. Lagervorspannung passt |
| – | Vordere Bremszange zentriert | ✅ erledigt |
| – | Hinterrad-Einlauf | ✅ erledigt |
| – | Teileidentifikation | ✅ ~95 % → Baustelle **10** |

### Bereits früher erledigt (aus der Umbauphase)

| Datum | Was | Notiz |
|---|---|---|
| ❓ | Kettenreparatur mit Fremdschloss | Kette dadurch kürzer → Baustelle 7 |
| ❓ | Gabel- und Steuersatztausch (Bergamont-NEX statt RST Vogue) | → Baustelle 1 + 6 + 14 |
| ❓ | Vorbau/Lenker montiert (Bergamont, winkelverstellbar, Faceplate) | → Baustelle 1 + 9 |
| ❓ | Bremsarme vorne vom Spenderrad montiert (Tektro) | weil die weißen nicht auf den Sockel passten → Baustelle 5 |
| ❓ | Bremsbeläge hinten vom Spenderrad montiert (Tektro 836) | weiße waren **durchgefahren** → Baustelle 2 + 3a |
| ❓ | Vorderrad komplett vom Spenderrad übernommen (Shining A-M4 + DH-3N31) | → Baustelle 2 + 13 |
| ❓ | Schutzbleche montiert (vorne über Originalpunkte der NEX-Gabel) | streifenfrei – ⚠️ bei Weg A+ neu lösen |
| ❓ | Rücklicht-Kabel neu gelötet + verlegt | Flachstecker entfernt |
| ❓ | Licht getestet: Nabendynamo + vorne/hinten funktionieren | ✅ |
| ❓ | Original-Hinterrad wieder eingebaut | Kassette ließ sich nicht lösen → Baustelle 11 |
| ❓ | Steuersatz eingestellt | freigängig, kein Spiel – aber ⚠️ nur Provisorium (Baustelle 6) |
| ❓ | Kette/Schaltung/**Umwerfer** funktionieren | ✅ (⚠️ „Schaltwerk Vo." = **Umwerfer**) |

> Bitte Datumsangaben ergänzen und neue Einträge in [`../06-logbuch/`](../06-logbuch/) anlegen.
