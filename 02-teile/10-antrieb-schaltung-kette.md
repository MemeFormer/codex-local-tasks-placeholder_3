# ⚙️ 10 – Antrieb & Schaltung

**Baugruppe:** Kurbelgarnitur · Innenlager · Kette · Kassette/Freilauf · Schalthebel ·
Umwerfer · Schaltwerk · Pedale
**Zustand:** ✅ funktioniert laut letztem Stand („Kette + Schaltung + Umwerfer laufen top“)
**Offen:** ⚠️ Kette ist zu kurz (Provisorium) → neue Kette 💰
**Baustellen:** 🟡 **#7** neue Kette (Spec steht: **Shimano CN-HG53**, 9-fach) · 🟢 **#11** Kassette
vom Spenderrad lösen (optional, **Kettenpeitsche** fehlt) →
[`../03-todos/offene-baustellen.md`](../03-todos/offene-baustellen.md)

> ✅ **GEKLÄRT (2026-09-04) – alle Antriebs-Teilenummern entschlüsselt:**
>
> | Teil | Stempelung | Identifikation |
> |---|---|---|
> | **Kurbelgarnitur** | **FC-M530/531 · 170** | ✅ **Shimano Deore FC-M530**, **Hollowtech** (hohlgeschmiedete Arme), **Octalink**-Verzahnung, Kurbelarmlänge **170 mm** |
> | **Innenlager** (gehört zum FC-M530) | ❓ Abdruck prüfen | ✅ **Shimano BB-ES25 Octalink**, **BSA 68 mm** (1,37″ × 24 tpi), Achslänge **113/118/121/126 mm**, Kettenlinie **47,5 / 50 mm** |
> | **Kette – NEUKAUF-SPEC** | – | 🔴 ✅ **Shimano CN-HG53** (oder CN-HG73), **9-fach** – das ist die **Original-Spec** zum FC-M530 |
> | **Schalthebel** | **SL-M580** | ✅ **Shimano Deore LX SL-M580**, **9-fach Rapidfire (Trigger)**, Lenkerklemmung **22,2 mm** |
> | **Umwerfer** (vorne) | **GD-C050 / OP Swing** | ✅ **Shimano FD-C050** – 🔴 **„GD" ist ein Lesefehler, es heißt FD** (F/G verwechselt). „OP Swing" = **Top Swing**. SIS, 3-fach, Klemmung **28,6 / 31,8 mm**, 5-mm-Inbus **5–7 Nm**, für Octalink/Spline-Kurbel, **max. 48 Zähne**, Kapazität **20 Zähne**, Kettenlinie **46–52,5 mm** |
> | **Schaltwerk** (hinten) | **RD-M511** | ✅ **Shimano Deore RD-M511** (M510-Familie), **9-fach, SGS-Langkäfig**: max. größtes Ritzel **34 Zähne**, max. Differenz vorne **22 Zähne**, Gesamtkapazität **45 Zähne** |
> | **Hinterradnabe** | **FH-M530 (VIAM)** | ✅ **Shimano Deore FH-M530**, Freilaufnabe, **9-fach HG-Spline** |
> | Pedale | ❓ unbekannt | Gewinde **9/16″ × 20 tpi** (über die Shimano-Doku zum FC-M530 bestätigt) |
>
> ⚠️ **Begriffskorrektur:** „Pedale … FC-M530" – **FC-M530 ist die KURBELGARNITUR**, nicht
> die Pedale. „FC" = Front Chainwheel. **170** = Kurbelarmlänge in mm.
> ⚠️ Und: „Schaltwerk vorne" heißt korrekt **UMWERFER**.

---

## 1. Begriffe in dieser Baugruppe

| Deutsch | Englisch | bei mir verbaut? |
|---|---|---|
| Kurbelgarnitur (3-fach) | crankset (triple) | ✅ **Shimano Deore FC-M530**, Hollowtech, **Octalink**, **170 mm** |
| Kettenblätter | chainrings | ❓ Zähne ____/____/____ – FC-M530 gab es als **44-32-22** (MTB) und **48-36-26** (Trekking). Wegen FD-C050 (max. 48 Z.) und Trekking-Einsatz: **vermutlich 48-36-26** |
| Innenlager | bottom bracket | ✅ **Shimano BB-ES25 Octalink**, BSA 68 mm – ❓ Achslänge (113/118/121/126 mm) und Abdruck prüfen |
| Kette (9-fach) | chain | ✅ repariert, ⚠️ zu kurz → Neukauf: **Shimano CN-HG53** |
| Kettenschloss | master link | ✅ vom alten Bike übernommen, ❓ Hersteller |
| Kassette (9-fach) | cassette | ✅ vom weißen Rad behalten, ❓ Modell + Abstufung (Deore-Ära: **CS-HG50-9 11-32**) |
| Freilaufkörper | freehub body | ✅ **HG-Spline** auf **Shimano Deore FH-M530** – 8/9-fach kompatibel |
| Schaltwerk | rear derailleur | ✅ **Shimano Deore RD-M511**, 9-fach, **SGS-Langkäfig** |
| Umwerfer | front derailleur | ✅ **Shimano FD-C050**, **Top Swing** („OP Swing"), 3-fach, Schelle 28,6/31,8 mm |
| Schalthebel (3×9) | shifters | ✅ **Shimano Deore LX SL-M580** – **Triggerhebel (Rapidfire)**, 9-fach, Klemmung 22,2 mm |
| Schaltzüge + Hüllen | cables + housing | ❓ Zustand |
| Schaltauge | derailleur hanger | ❓ vorhanden/gerichtet? |

---

## 2. Ist-Zustand (bitte prüfen und eintragen)

### 2.1 Übersetzung

```
Kurbel vorne:      ____ / ____ / ____ Zähne   (FC-M530: 48-36-26 Trekking ODER 44-32-22 MTB)
Kassette hinten:   ____ - ____ Zähne (9 Ritzel)  (RD-M511: max. 34 Zähne!)
                   Abstufung eintragen:  __ __ __ __ __ __ __ __ __
```

### 🔴 Rechnerische Prüfung der Schaltkapazität (mit den echten Werten)

```
RD-M511 (9-fach, SGS-Langkäfig):
          max. größtes Ritzel    34 Zähne
          max. Differenz vorne   22 Zähne
          Gesamtkapazität        45 Zähne

Fall A  Kurbel 48-36-26 + Kassette 11-32:
        Differenz vorne  = 48 − 26 = 22   ✅ exakt am Limit
        Differenz hinten = 32 − 11 = 21
        Gesamtbedarf     = 22 + 21 = 43   ✅ ≤ 45
        Größtes Ritzel   = 32             ✅ ≤ 34

Fall B  Kurbel 44-32-22 + Kassette 11-34:
        Differenz vorne  = 44 − 22 = 22   ✅ exakt am Limit
        Differenz hinten = 34 − 11 = 23
        Gesamtbedarf     = 22 + 23 = 45   ✅ = exakt an der Grenze
        Größtes Ritzel   = 34             ✅ = exakt am Limit

→ Beide Fälle passen, aber es ist KEIN Spielraum mehr.
→ 🔴 Eine Kassette mit 36 Zähnen oder eine Kurbel mit mehr als 22 Zähnen Differenz
  würde NICHT mehr passen. Beim Neukauf also bei 9-fach, max. 34 Zähne bleiben!
→ Big-Big ist konstruktiv gerade noch erlaubt, wegen der ZU KURZEN Kette trotzdem meiden.
```

### FD-C050 (Umwerfer) – worauf es ankommt

| Eigenschaft | Wert |
|---|---|
| Modell | **Shimano FD-C050** (City/Trekking, Nachfolger FD-C051) |
| Bauart | **Top Swing** („OP Swing"), **SIS**-indexiert |
| Befestigung | **Schelle** (clamp mount), ❓ **28,6 mm oder 31,8 mm** – 🔴 **messen!** |
| Gänge | 3-fach |
| Max. großes Kettenblatt | **48 Zähne** |
| Gesamtkapazität | **ca. 20 Zähne** → ⚠️ bei 48-36-26 = 22 Zähne Differenz **knapp über** Spec. Prüfen, ob es in der Praxis trotzdem sauber schaltet |
| Passende Kurbel | Octalink / Spline |
| Kettenlinie | **46–52,5 mm** |
| Anzugsmoment Schelle | **5–7 Nm**, **5-mm-Inbus** |
| Zugansteuerung | ❓ Top Pull / Bottom Pull prüfen (C050 meist **Dual Pull**) |

> 💡 **Praxis-Hinweis:** Der FD-C050 stammt aus der City/Trekking-Linie und ist laut
> Shimano-Angaben eher für 6/7-fach-Systeme freigegeben. Dass er mit deiner 9-fach-Kette
> „top läuft", ist ein gutes Zeichen – **aber:** Falls er irgendwann unpräzise schaltet,
> ist ein **Shimano Deore FD-M530 / FD-M591** (9-fach, **Top Swing**, Schelle) der
> sauberere Ersatz (💰 20–35 €).

Die Abstufung steht meist **auf jedem Ritzel eingeprägt** (klein, an der Innenseite) oder
auf dem größten Ritzel als Gesamtangabe (z. B. „11-32“).

### 2.2 Kette

| Feld | Wert |
|---|---|
| Hersteller / Modell | ✅ Neukauf-Spec: **Shimano CN-HG53** (Original-Spec zum FC-M530) · ❓ Aufdruck der **aktuellen** Kette noch ablesen |
| Geschwindigkeitsklasse | ✅ **9-fach** (muss zur Kassette passen) |
| Aktuelle Gliederzahl (Außenglieder zählen) | ❓ TODO ____ Glieder |
| Soll-Gliederzahl | ❓ TODO (siehe Rechnung unten) |
| Kettenschloss-Typ | ❓ Shimano-Nietstift (einmalig!) / SRAM PowerLock / KMC MissingLink (wiederverwendbar) |
| Verschleiß (Kettenlehre) | ❓ TODO ____ % (Neukauf ab 0,75 %) |
| Position der Reparaturstelle | ❓ markieren (z. B. mit Edding oder Foto) |

### ⚠️ Was bei der Kettenreparatur passiert ist

Die Kette ist **nicht am Schloss** gerissen, sondern an einer normalen Nietstelle. Zum Einbau
des Fremdschlosses musste ein **Stift aus einer Außenlasche** herausgedrückt werden. Damit
verliert die Kette **ein Außenglied-Paar** → Länge reduziert sich um ca. **½ bis 1 Teilung**
(Teilung = 12,7 mm pro Glied).

**Konsequenzen:**

| Effekt | Bewertung |
|---|---|
| Kettenspannung im größten Gang (Big-Big: großes Kettenblatt + größtes Ritzel) | ⚠️ Schaltwerk wird weiter nach vorne gezogen, Käfig fast waagerecht |
| Gefahr: Schaltwerk überstreckt → Käfig/Schaltauge/Rahmen beschädigt | 🔴 **Big-Big vermeiden**, bis neue Kette montiert ist |
| Kleiner Gang (Small-Small) | ✅ unkritisch, Spannung nur geringer |
| Schaltpräzision | meist noch okay |
| Dauerlösung | ❌ nein – neue Kette kaufen |

**Prüfung am Rad (2 Minuten):**

1. Schalte auf **großes Kettenblatt + größtes Ritzel** (nur im Stand, vorsichtig, nicht fahren)
2. Schau auf den Schaltwerkskäfig: Ist der Abstand **Leitrolle → Ritzel** noch ≥ 5 mm?
   Bleibt der Käfig in einem Winkel **unter 90°** zur Kettenstrebe (nicht komplett gestreckt)?
3. Lässt sich die Kette **ohne Kraft** in diese Position schalten? Geht sie rein/schwer?
4. Prüfe **Small-Small**: hängt die Kette durch und schleift an der Leitrolle?

**Ergebnis eintragen:**

| Test | Ergebnis |
|---|---|
| Big-Big schaltbar ohne Blockieren? | ❓ ja / nein |
| Käfig gestreckt (fast waagerecht)? | ❓ ja / nein |
| Abstand Leitrolle → größtes Ritzel | ❓ ____ mm (Soll ≥ 5 mm) |
| Small-Small: Kette schleift? | ❓ ja / nein |

---

## 3. Kettenlänge richtig bestimmen (für die neue Kette)

**Methode A – ohne durchs Schaltwerk zu führen (empfohlen, sicherste Methode):**

1. Neue Kette auf **großes Kettenblatt + größtes Ritzel** legen (**nicht** durchs Schaltwerk!)
2. Kette schließen, sodass sie stramm anliegt
3. **2 Glieder (= 1 Innenglied + 1 Außenglied ≈ 25,4 mm) dazugeben**
4. Das ist die Soll-Länge

**Methode B – Rechnung:**

```
L (Glieder) = (2 × Kettenstrebenlänge in mm) / 12,7
            + (Zähne großes Kettenblatt + Zähne größtes Ritzel) / 2
            + 2   … aufrunden auf ganze Glieder, bei 3-fach eher +0,5 extra

Kettenstrebenlänge (center of BB → rear axle):  ❓ TODO ____ mm
```

**Methode C – alte Kette als Maß (funktioniert hier NICHT, weil die alte gekürzt wurde)** ⚠️

```
Soll-Gliederzahl: ❓ TODO ____ Glieder
Bestellt wird:    Kette 9-fach mit ____ Gliedern (Standard: 114 oder 116, wird gekürzt)
```

### 💰 Was ich brauche

| Teil | Spezifikation | Prio | ca. Preis | Notiz |
|---|---|---|---|---|
| **Kette** | 🔴 **Shimano CN-HG53, 9-fach**, 116 Glieder (**Original-Spec** zum FC-M530) · Alternativ KMC X9 9-fach | 🔴 hoch | 12–18 € | Länge selbst kürzen; 🔴 **NICHT** die reparierte alte Kette als Maß nehmen |
| Kettenschloss | **KMC MissingLink 9-fach** (wiederverwendbar) | 🟡 | 4 € | Shimano-Ketten kommen mit **einmaligem Nietstift** |
| Kettenlehre | Verschleißmesslehre 0,5/0,75/1,0 | 🟢 | 8 € | Neukauf ab 0,75 % |

---

## 4. Kassette & Freilauf – warum sich die Kassette „nicht lösen ließ“

> Das war der Grund, warum das Original-Hinterrad wieder eingebaut wurde.
> **Sehr wahrscheinlich lag es am Werkzeug, nicht am Teil.**

### 4.1 Erstmal klären: Kassette oder Schraubkranz?

| Merkmal | **Kassette** (cassette) | **Schraubkranz** (freewheel) |
|---|---|---|
| Befestigung | dünner **Verschlussring** (lockring) in der Mitte | der ganze Kranz ist **aufgeschraubt** |
| Kleinster Zahnkranz | meist ≥ 11 Zähne, glatter Abschluss | meist 13–14 Zähne, mit Einschnitten |
| Werkzeug | Kassettenabzieher (12-Spline) + **Kettenpeitsche** | Schraubkranzabzieher + Kettenpeitsche |
| Freilauf | separat, bleibt auf der Nabe | **im Kranz integriert** |
| Bei 9-fach | ✅ fast immer Kassette | ❌ 9-fach-Freewheels sind selten |

### 4.2 Kassetten-Demontage – korrekter Ablauf

1. Schnellspanner **komplett rausdrehen und entfernen** (nicht nur öffnen!)
2. **Kettenpeitsche** auf ein mittleres/großes Ritzel legen, gegen Uhrzeigersinn auf Zug
3. **Kassettenabzieher** (12-Spline, z. B. Shimano HG) in den Lockring stecken,
   mit **Maulschlüssel/Ratsche** oder Drehmomentschlüssel
4. Abzieher **gegen den Uhrzeigersinn** drehen (= Lockring lösen, Rechtsgewinde),
   Kettenpeitsche hält **im Uhrzeigersinn** dagegen
5. Benötigtes Drehmoment: oft **30–50 Nm** – der Lockring sitzt wirklich fest, und
   zusätzlich verbacken ihn Rost und Fett

**💡 Der wahrscheinlichste Fehler:** Lockring-Werkzeug allein dreht die ganze Kassette mit,
wenn **keine Kettenpeitsche** das Paket festhält. Dann „bewegt sich kein Ritzel“ – exakt die
Beobachtung aus deinem Bericht. Ohne Kettenpeitsche geht es fast nie.

**Notlösung ohne Kettenpeitsche:** alte Kette um ein großes Ritzel wickeln, mit einem
Schraubendreher/Knebel als Hebel festhalten. Oder: **Zweimann-Methode** – eine Person hält die
Felge mit einem Holzklotz/Lappen gegen die Speichen (vorsichtig, keine Speichen verbiegen).

**Wenn der Lockring wirklich festsitzt:**
- Rostlöser (WD-40 / Caramba) an die Lockring-Gewindestelle, 20 min einwirken lassen
- **Hitze**: Lockring mit Heißluftpistole erwärmen (nicht die Nabe/das Lager!), dann lösen
- Langer Hebel am Werkzeug (Rohr als Verlängerung)
- Achtung: **Keramik-/Industrielager** und Fett nicht überhitzen

### 4.3 8-fach ↔ 9-fach Kompatibilität (deine ursprüngliche Frage)

| Kombination | Passt? | Hinweis |
|---|---|---|
| 9-fach-Kassette auf HG-Freilaufkörper | ✅ | HG-Spline ist bei 8/9/10-fach identisch |
| 8-fach-Kassette auf 8/9/10-fach-Freilaufkörper | ✅ ggf. mit **4,5-mm-Distanzscheibe** bei 10-fach-Körper | |
| 9-fach-Kassette auf 7-fach-Freilaufkörper | ❌ | 7-fach-Körper ist kürzer |
| 9-fach-Kette auf 8-fach-Kassette | ✅ (geht, minimal unpräzise) | |
| 8-fach-Kette auf 9-fach-Kassette | ⚠️ funktioniert, aber zu breit → schlechtere Schaltpräzision, mehr Verschleiß | nicht empfohlen |
| 9-fach-Schalthebel + 9-fach-Kassette | ✅ | Ritzelabstand 9-fach = **4,34 mm** (8-fach = 4,8 mm) |

**Wichtige Ritzelabstände (Shimano HG):**

| Anzahl Ritzel | Ritzelabstand (pitch) | Ketten-Außenbreite |
|---|---|---|
| 7-fach | 5,0 mm | 7,3 mm |
| 8-fach | 4,8 mm | 7,1 mm |
| 9-fach | **4,34 mm** | **6,6–6,8 mm** |
| 10-fach | 3,95 mm | 5,9 mm |

→ Deshalb: **9-fach-Kassette verlangt eine 9-fach-Kette.** Eine 8-fach-Kette passt
mechanisch auf die Verzahnung, ist aber zu breit und schaltet schlechter.

### 4.4 Freilaufkörper tauschen (nur falls wirklich nötig)

Der Freilaufkörper des weißen Rads klingt feiner – das ist ein **Qualitäts-/Klinkenanzahl**-
Unterschied (mehr Klinken = kürzerer Leerweg = „feineres“ Klicken). Ein Tausch ist möglich, aber:

| Schritt | Werkzeug |
|---|---|
| Schnellspanner raus | – |
| Kontermutter + Konus der Nabe lösen (auf der **Antriebsseite** ist der Freilauf aufgeschraubt) | Konusschlüssel ❓ Größe (oft 15 mm), evtl. **10-mm-Inbus** |
| Freilaufkörper abziehen | evtl. große Innensechskant-Nuss (**10 mm Inbus**, z. B. Shimano FH-RM/Nabe) |
| Kugeln/Fett nicht verlieren | Lappen |
| Neuen Freilaufkörper aufstecken, **Freilauf-Fett** verwenden | |
| Lager neu einstellen | Konusschlüssel |

**Kompatibilitätsprüfung vor dem Kauf:** Freilaufkörper sind **naben­modell­spezifisch**
(unterschiedliche Länge, Verzahnung, Achsdurchmesser). Also: **Nabenmodell ablesen** und den
Original-Ersatzteil-Katalog (Shimano SI / EV-Dokument) suchen.

**Bewertung:** 🔻 **Nicht nötig**, solange der vorhandene Freilauf sauber läuft. Lieber die
anderen Baustellen zuerst.

---

## 5. Schaltwerk & Umwerfer – Einstellreferenz

| Schraube | Funktion | Einstellung |
|---|---|---|
| **L** (low) | Begrenzung zum größten Ritzel hin | Leitrolle fluchtet exakt unter dem größten Ritzel, Kette fällt nicht in die Speichen |
| **H** (high) | Begrenzung zum kleinsten Ritzel hin | Leitrolle fluchtet unter dem kleinsten Ritzel, Kette fällt nicht nach außen ab |
| **B-Tension** | Abstand Leitrolle → Ritzel | 5–6 mm bei größtem Ritzel (Shimano-Angabe oft 5–6 mm) |
| Zugspannung (Barrel Adjuster) | Indexierung | Schaltet schlecht auf größere Ritzel → **mehr** Spannung (rausdrehen). Schaltet schlecht auf kleinere → weniger |
| Umwerfer-Höhe | Kettenblatt-Abstand | Außenleitblech 1–3 mm über den Zähnen des großen Blatts |
| Umwerfer-Winkel | Parallelität | Leitblech parallel zu den Kettenblättern |
| Umwerfer L/H | Begrenzung | Kette schleift nicht am Leitblech |

**Zughüllen-Längen:** nicht zu kurz (Knick → Reibung → schlechtes Schalten), nicht zu lang
(Schleife streift am Reifen/Schutzblech).

---

## 6. Pedale

| Feld | Wert |
|---|---|
| Typ | ❓ Plattform / SPD-Klick |
| Gewinde | 9/16" × 20 tpi (Standard) – ⚠️ **linkes Pedal hat Linksgewinde!** |
| Zustand | ❓ Lager, Gewinde |
| Schlüsselweite | 15 mm Pedalschlüssel oder 6/8-mm-Inbus von der Kurbelinnenseite |

⚠️ **Montage-Regel:** rechtes Pedal = Rechtsgewinde (normal), linkes Pedal = Linksgewinde
(löst sich beim Rückwärtstreten nicht). Gewinde leicht fetten.

---

## 7. 📐 Messliste für den nächsten Werkstattbesuch

| # | Messung | Wert |
|---|---|---|
| 1 | 🔴 Zähnezahl der drei Kettenblätter (48-36-26 oder 44-32-22?) | ____ / ____ / ____ |
| 2 | ~~Kurbelarmlänge~~ | ✅ **170 mm** |
| 3 | 🔴 Kassette: Modellnummer + Abstufung (**max. 34 Zähne** wg. RD-M511!) | |
| 4 | Kette: Modellnummer der **aktuellen** Kette + Gliederzahl | |
| 5 | 🔴 Kettenstrebenlänge (Mitte Tretlager → Mitte Achse) – für die Kettenlängenrechnung | ____ mm |
| 6 | ~~Schaltwerk: Modellnummer~~ · Käfiglänge bestätigen (SGS?) | ✅ **RD-M511** · ❓ SGS |
| 7 | ~~Umwerfer: Modellnummer~~ · **Schellen-Ø messen** (28,6 oder 31,8 mm!) | ✅ **FD-C050** · ____ mm |
| 8 | ~~Schalthebel: Modellnummer~~ | ✅ **SL-M580**, Trigger |
| 9 | Big-Big-Test (Abschnitt 2.2) | |
| 10 | Kette: Verschleiß mit Lehre gemessen? | ____ % |
| 11 | Ist das Schaltauge original / gerichtet? | |
| 12 | ~~Hinterrad-Nabenmodellnummer~~ | ✅ **FH-M530 (VIAM)** |
| 13 | 🔴 **Innenlager-Abdruck**: BB-ES25? Achslänge (113/118/121/126 mm)? Kettenlinie? | |
| 14 | Umwerfer: Zugansteuerung **Top Pull** oder **Bottom Pull**? | |
| 15 | Kettenlinie messen (Mitte Kettenblatt → Mitte Tretlagergehäuse) – Soll 47,5/50 mm | ____ mm |

## 8. 💰 Einkaufsbedarf

| Teil | Spec | Prio | ca. Preis | bestellt? |
|---|---|---|---|---|
| **Kette 9-fach** | 🔴 **Shimano CN-HG53**, 116 Glieder (**Original-Spec** FC-M530) · alternativ KMC X9 | 🔴 | 12–18 € | ☐ |
| KMC MissingLink 9-fach | wiederverwendbares Kettenschloss | 🟡 | 4 € | ☐ |
| Kettennieter | falls nicht vorhanden | 🔴 | 8–15 € | ☐ |
| Kettenpeitsche | für Kassette (später) | 🟡 | 10–15 € | ☐ |
| Kassettenabzieher Shimano HG | 12-Spline – 💡 **passt oft auch auf die Nabendynamo-Rotormutter!** | 🟡 | 8–12 € | ☐ |
| Kettenlehre | 0,5/0,75/1,0 | 🟢 | 8 € | ☐ |
| Schaltzug-Set | Edelstahl **1,2 mm** + Hüllen **4 mm** (SL-M580 Rapidfire) | 🟢 | 10–20 € | ☐ |
| 🔴 Nur falls nötig: **Umwerfer** | **Shimano Deore FD-M530 / FD-M591**, 9-fach, **Top Swing**, Schelle ❓ mm – Ersatz für den FD-C050 | 🟢 | 20–35 € | ☐ |
| 🔴 Nur falls nötig: **Innenlager** | **Shimano BB-ES25 Octalink**, **BSA 68 mm**, Achslänge ❓ mm (113/118/121/126) | 🟢 | 25–40 € | ☐ |
