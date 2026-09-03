# 🛑 40 – Bremsen

**System:** ✅ **V-Brake** (Linearpullzug) – bestätigt
**Baugruppe:** Bremshebel (Lenker) · Bremsarme (Zange) · Bremssockel · Federspannschrauben ·
Federraste · Bremszüge · Zughüllen · Bremsbeläge · Felge (Bremsflanke)
**Zustand:** ✅ Hebel original weiß (gut) · ⚠️ Bremsarme vorne vom Spenderrad (zu weich) ·
🔴 hintere Bremse kehrt nicht zurück · ⚠️ Beläge hinten vom Spenderrad · ⚠️ Felgenflanken?

---

## 0. ⚠️ Begriffe: zwei verschiedene „Hebel“

Am Fahrrad mit Felgenbremse gibt es zwei Dinge, die man umgangssprachlich „Hebel“ nennt.
**Das muss getrennt werden**, sonst sucht man an der falschen Stelle:

| Umgangssprachlich | **Korrekt** | Englisch | Wo | Zustand bei mir |
|---|---|---|---|---|
| „Bremshebel“, „Armatur“ | **Bremshebel** | brake lever | am Lenker | ✅ **beide weiß, original, gut** |
| „die zwei Hebel unten an der Bremse“ | **Bremsarme** / Bremsschenkel | brake arms | an Gabel / Hinterbau | ⚠️ vorne schwarz · ✅ hinten weiß |
| „die Bremse“ als Ganzes | **Bremszange** / Bremskörper | brake caliper | – | – |
| „der Stahlstift, auf den man das aufsteckt“ | **Bremssockel** / Cantisockel | brake boss / canti stud | an Gabel / Hinterbau | ⚠️ vorne passt der weiße Arm nicht |
| „die kleine Stellschraube“ | **Federspannschraube** | spring tension screw | am Bremsarm | ⚠️ ändert „wirklich nur wenig“ |
| „der kleine Stift hinten am Arm“ | **Federraste / Federstift** | spring retainer pin | Bremsarm → Sockel | 💡 **hier liegt die Lösung!** |
| „die Löcher im Sockel“ | **Federrasten-Bohrungen** | spring tension holes | Bremssockel, **3 Stück** | 💡 |
| „die Schraube zum Festmachen“ | **Bremsbefestigungsschraube** | brake mounting bolt | M6 ins Innengewinde des Sockels | |
| „das gebogene Röhrchen“ | **Zugführungs-Röhrchen / Nudel** | cable noodle | zwischen den Bremsarmen | |
| „der Balg“ | **Faltenbalg** | bellows / boot | über der Nudel | |

### Aktuelle Aufteilung (bitte ergänzen)

| Position | Bremshebel (Lenker) | Bremsarme (Zange) | Beläge | Bemerkung |
|---|---|---|---|---|
| **vorne** | ✅ weiß, original | ⚠️ **schwarz** (Spenderrad) | ❓ welche? | weiße Arme passten nicht auf den Sockel |
| **hinten** | ✅ weiß, original | ✅ **weiß**, original | ⚠️ **schwarz** (Spenderrad) | weiße Beläge waren „ziemlich runter“ |

> 💡 **Wichtige Konsequenz für Baustelle #3:** Hinten sind Zange, Federn **und** Zug original –
> **nur die Beläge wurden getauscht**. Wenn die Bremse seitdem nicht zurückkehrt, sind die
> **neuen (gebrauchten) Beläge der Hauptverdächtige**. Siehe
> [`../04-diagnose/hintere-bremse-kehrt-nicht-zurueck.md`](../04-diagnose/hintere-bremse-kehrt-nicht-zurueck.md) Abschnitt 0.

---

## 1. System: V-Brake – was das bedeutet

| Eigenschaft | Wert |
|---|---|
| Zugweg | **long pull** (lang) |
| Passende Bremshebel | **V-Brake-Hebel** (long pull) – ✅ die weißen Originale sollten das sein |
| Innenzug-Ø | **1,5 mm** (MTB/V-Brake-Standard) |
| Hülle-Ø außen | **5 mm**, **spiralgewickelt** |
| Belagabstand | **1 mm** pro Seite |
| Toe-in | 0,5–1 mm |
| Bremssockel-Gewinde | **M6** Innengewinde |
| Bremssockel-Höhe | abhängig von der Laufradgröße (siehe unten) |

**Prüfen (Modellnummern ablesen):**

| Frage | Antwort |
|---|---|
| Modellnummer Bremshebel links/rechts | ❓ |
| Modellnummer Bremsarme vorne (schwarz) | ❓ |
| Modellnummer Bremsarme hinten (weiß) | ❓ |
| Zugführungs-Röhrchen (Nudel): Länge? | ❓ ____ mm (Standard 92 mm; kurze Nudel = mehr Kraft, weniger Weg) |
| Innenzug-Ø gemessen | ❓ ____ mm |

### Bremssockel-Höhe nach Laufradgröße (Shimano-Referenz)

Abstand **Mitte Ausfallende → Mitte Bremssockel**:

| Laufradgröße | Felgen-Ø | Soll-Abstand |
|---|---|---|
| 26" | 559 mm | ca. **253,5 mm** |
| 27,5" | 584 mm | ca. 266 mm |
| **28" / 29"** | **622 mm** | ca. **283 mm** |
| Abstand Sockel zueinander | – | 77–85 mm |

> ⚠️ Falls die schwarze Gabel für 26" gebaut ist und das weiße Rad 28" hat, sitzen die
> Bremsarme ca. **30 mm zu tief** → das könnte erklären, warum die weißen Bremsarme
> „nicht passten“. **Messen!**

---

## 2. Baustelle #4: Vordere Bremsarme zu weich / Federn zu schwach

### 🔴 Die wichtigste Erkenntnis

> **Die Federspannschraube ist das falsche Werkzeug für „Federn zu schwach“.**

Die „kleine Stellschraube“ hat nur ca. **±2–3 Umdrehungen** Verstellweg und dient vor allem
der **Zentrierung** (beide Arme gleich weit von der Felge), nicht der Erhöhung der
Rückstellkraft. Dass sie „wirklich nur wenig ändert“, ist **konstruktiv normal** und kein Defekt.

### ✅ Die echte Stellgröße: Federraste (3 Löcher im Bremssockel)

Der kleine **Federstift** auf der Rückseite jedes Bremsarms greift in **eine von drei
Bohrungen** im Bremssockel. Anderes Loch = deutlich andere Federvorspannung.

**Ablauf (10 min, 0 €):**

1. Bremsbefestigungsschraube (M6-Inbus) lösen, Bremsarm abziehen
2. Federspannschraube ganz herausdrehen
3. Bremsarm wieder aufsetzen, **Federstift in ein anderes Loch** setzen
4. **Beide Arme in dasselbe Loch** (sonst zieht die Bremse einseitig)
5. Federspannschraube wieder mittel positionieren, dann fein zentrieren
6. Test: Arme von Hand zusammendrücken → müssen **kräftig und komplett** zurückschnappen

### Maßnahmen-Ranking

| # | Maßnahme | Aufwand | Kosten | Bewertung |
|---|---|---|---|---|
| 1 | **Federraste: anderes Loch** | 10 min | 0 € | ✅ **zuerst machen** |
| 2 | Bremssockel + Bolzen **reinigen und dünn fetten** | 10 min | 0 € | ✅ immer – trockene Sockel sind eine Hauptursache |
| 3 | **Federn der weißen Bremsarme** in die schwarzen umsetzen | 30 min | 0 € | ✅ V-Brake-Federn sind meist baugleich; vorher Drahtstärke/Windungen/Haken vergleichen |
| 4 | Sockel von Lack/Rost befreien (400er Schleifleinen) → weiße Arme passen evtl. doch | 20 min | 3 € | 💡 **häufigste Ursache für „passt nicht“** |
| 5 | Feder leicht nachbiegen (nur am Hakenende, max. 10–15°) | 10 min | 0 € | ⚠️ Notlösung |
| 6 | Neue V-Brake vorne | 30 min | 💰 15–30 € | ✅ günstig und zuverlässig |
| 7 | **Weiße Original-Gabel zurückbauen** | hoch | 💰 3–10 € | 💡💡 **löst #4 UND #5 auf einmal** |

→ Vollständige Diagnose inkl. Bremssockel-Tausch:
[`../04-diagnose/vordere-bremsarme-sockel.md`](../04-diagnose/vordere-bremsarme-sockel.md)

### ⚠️ Ist der Bremssockel tauschbar?

| Gabelmaterial | Sockel-Befestigung | Tauschbar? |
|---|---|---|
| **Stahl** | angeschweißt / aufgelötet | ❌ **nein** – nur Werkstatt mit Lötbrenner. 🔴 Gabel ist Sicherheitsbauteil, nicht selbst schweißen/bohren |
| **Alu** | oft **eingeschraubt** (Stahlbolzen mit 2 Abflachungen für Gabelschlüssel, M8 oder M10) | ✅ ja, mit Schraubensicherung |

→ **Magnet-Test an der Gabel machen** und eintragen: ❓ Stahl / Alu

---

## 3. Baustelle #3: Hintere Bremse kehrt nicht zurück

**Ausgangslage:** Zange ✅ original weiß · Federn ✅ original · Zug ✅ original ·
**Beläge ⚠️ neu (gebraucht vom Spenderrad)**

→ **Die Beläge sind der Hauptverdächtige**, weil sie das Einzige sind, was sich geändert hat.

### Ursachen-Ranking (korrigiert)

| # | Ursache | Wahrscheinlichkeit | Test |
|---|---|---|---|
| 1 | **Fremde Beläge passen nicht**: zu lang, zu dick, falsche Form → haken an Felgenkante/Reifen | 🔴 **hoch** | Beläge ansehen: ragen sie über die Bremsflanke hinaus? Berühren sie den Reifen? |
| 2 | **Konvex-/Konkavscheiben** vertauscht oder falsch herum → Belag steht schräg und verkantet | 🔴 hoch | Belagträger zerlegen, Scheibenreihenfolge prüfen |
| 3 | **Scharfe Kante an der abgefahrenen Bremsflanke** → Belag bleibt hängen | 🔴 hoch | mit dem Fingernagel über die Felgenkante fahren |
| 4 | Zug/Hüll-Reibung (neue Verlegung) | mittel | Binärsuche: Zug aushängen |
| 5 | Belag verhärtet/verglast (lange Standzeit am Spenderrad) | mittel | Belag ansehen: glänzend/hart? |
| 6 | Rückholfeder falsch eingehängt / Pivot trocken | niedrig | Zange ausgehängt testen |

→ Volle Diagnose mit Binärsuche und Testprotokoll:
[`../04-diagnose/hintere-bremse-kehrt-nicht-zurueck.md`](../04-diagnose/hintere-bremse-kehrt-nicht-zurueck.md)

### V-Brake-Beläge: worauf es ankommt

| Größe | V-Brake | Cantilever | Rennrad-Seitenzug |
|---|---|---|---|
| Belaglänge | **ca. 70 mm** | ca. 55–65 mm | ca. 50 mm |
| Befestigung | Gewindebolzen M6 mit Konvex/Konkav-Scheiben | dito (kürzer) | Steck- oder Schraubbelag |
| Kompatibilität | ⚠️ **Canti-Beläge sind zu kurz für V-Brakes** – sie liegen nicht voll auf der Felge | | |

**Scheiben-Reihenfolge am Belagbolzen (Standard V-Brake):**

```
Bremsarm
  │  Konkavscheibe (nach außen gewölbt)
  │  Konvexscheibe (nach innen gewölbt, dünn)
  │  ── Belagträger mit Belag ──
  │  Konvexscheibe (dick)
  │  Konkavscheibe
  │  Unterlegscheibe
  └─ Mutter
```

⚠️ Die **dünne Konvexscheibe** gehört auf die Seite zum Bremsarm, die **dicke** nach außen.
Falsch herum = der Belag lässt sich nicht richtig schwenken und steht schräg → verkantet →
**Bremse kehrt nicht zurück**. Das ist ein sehr häufiger Fehler nach einem Belagwechsel!

**Prüfen:**

| ☐ | Frage | Antwort |
|---|---|---|
| ☐ | Belaglänge der Spenderrad-Beläge | ❓ ____ mm |
| ☐ | Sind es V-Brake-Beläge (ca. 70 mm) oder kürzere? | ❓ |
| ☐ | Konvex/Konkav-Scheiben in der richtigen Reihenfolge? | ❓ |
| ☐ | Steht der Belag senkrecht zur Felge (nicht verdreht)? | ❓ |
| ☐ | Liegt der Belag **komplett** auf der Bremsflanke? | ❓ |
| ☐ | Berührt er den Reifen? | ❓ 🔴 |
| ☐ | Belag-Material: noch weich/griffig oder hart/verglaset? | ❓ |

---

## 4. Grundeinstellung V-Brake (Sollwerte)

| Größe | Sollwert |
|---|---|
| Abstand Belag → Felge | **1 mm** pro Seite |
| Belagposition | **komplett auf der Bremsflanke**, nicht am Reifen, nicht unter der Felgenkante |
| Toe-in | vorderer Belagsrand **0,5–1 mm** näher an der Felge |
| Zentrierung | beide Arme gleich weit von der Felge |
| Hebelweg bis Druckpunkt | max. **1/3–1/2** |
| Anzugsmoment Bremsbefestigungsschraube | 6–8 Nm |
| Anzugsmoment Zugklemmschraube | 5–7 Nm |
| Federspannschrauben | mittig, dann fein justieren |
| Federraste | **beide Arme im selben Loch** |

**Reihenfolge beim Einstellen (einhalten, sonst doppelte Arbeit):**
Zange montieren → Federraste wählen → Federspannschrauben grob zentrieren →
Zug einhängen und spannen → Beläge positionieren (Höhe, Toe-in) → Feinjustage über
Barrel Adjuster → Endtest.

→ [`../05-anleitungen/bremsen-einstellen.md`](../05-anleitungen/bremsen-einstellen.md)

---

## 5. Ist-Zustand – Tabelle zum Ausfüllen

| Komponente | Verbaut | Hersteller + Modell | Zustand | Notiz |
|---|---|---|---|---|
| Bremshebel links | ✅ weiß, original | ❓ | ✅ gut | |
| Bremshebel rechts | ✅ weiß, original | ❓ | ✅ gut | |
| Bremszug vorne | ❓ | ❓ | ❓ | |
| Bremszughülle vorne | ❓ | ❓ | ❓ | Länge ❓ mm |
| Zugführungs-Röhrchen (Nudel) vorne | ❓ | – | ❓ | Länge ❓ mm |
| **Bremsarme vorne** | ⚠️ **schwarz** (Spenderrad) | ❓ | ⚠️ zu weich, Federn schwach | weiße passten nicht auf den Sockel |
| Bremssockel Gabel | ❓ Stahl (geschweißt) / Alu (geschraubt) | – | ⚠️ Lack/Rost? | Magnet-Test! |
| Bremsbeläge vorne | ❓ welche? | ❓ | ❓ | |
| Bremszug hinten | ✅ original | ❓ | ❓ | |
| Bremszughülle hinten | ✅ original | ❓ | ⚠️ Verdacht Reibung | Länge ❓ mm |
| **Bremsarme hinten** | ✅ **weiß**, original | ❓ | ✅ gut | |
| Bremssockel Hinterbau | ✅ original | – | ❓ | Abstand zum Ausfallende ❓ mm |
| **Bremsbeläge hinten** | ⚠️ **schwarz** (Spenderrad) | ❓ | 🔴 **Hauptverdacht Baustelle #3** | Länge ❓ mm |
| Felgenflanke vorne | ❓ | – | 🔴 prüfen | |
| Felgenflanke hinten | ❓ | – | 🔴 prüfen | scharfe Kante? |

---

## 6. 📐 Messliste für den nächsten Werkstattbesuch

| # | Messung | Wert |
|---|---|---|
| 1 | Modellnummer Bremshebel (Unterseite) | |
| 2 | Modellnummer Bremsarme vorne (schwarz) | |
| 3 | Modellnummer Bremsarme hinten (weiß) | |
| 4 | **Magnet-Test Gabel: Stahl oder Alu?** | |
| 5 | Bremssockel Gabel: Lack/Rost sichtbar? | |
| 6 | Bremssockel Gabel: 3 Bohrungen für die Federraste sichtbar? | |
| 7 | **In welchem Loch sitzt der Federstift aktuell?** | |
| 8 | Abstand Mitte Ausfallende → Mitte Bremssockel, **Gabel** | ____ mm |
| 9 | Abstand Mitte Ausfallende → Mitte Bremssockel, **Hinterbau** (Referenz) | ____ mm |
| 10 | Spalt zwischen Bremsarm und Sockel-Schulter | ____ mm |
| 11 | Länge der Bremsbeläge hinten (Spenderrad) | ____ mm |
| 12 | Konvex-/Konkav-Scheiben-Reihenfolge hinten korrekt? | |
| 13 | Restbelagstärke der weißen Original-Beläge (wurden ausgetauscht) | ____ mm |
| 14 | Innenzug-Ø gemessen (1,2 oder 1,5 mm) | ____ mm |
| 15 | Hüllen-Ø außen (5 mm?) | ____ mm |
| 16 | Länge der Nudel (Zugführungs-Röhrchen) | ____ mm |
| 17 | Felgenkante hinten: scharfkantig? | |
| 18 | Federspannschrauben: Inbus-Größe, noch Verstellweg? | |

## 7. 📸 Foto-Liste

| ☐ | Foto | Zweck |
|---|---|---|
| ☐ | Bremshebel Unterseite (Modellnummer) | Zugweg bestimmen |
| ☐ | Bremssockel Gabel, Nahaufnahme, seitlich beleuchtet | Lack? Rost? Abflachungen? |
| ☐ | Bremssockel ohne Bremsarm, von vorne | die 3 Federrasten-Bohrungen |
| ☐ | Rückseite eines Bremsarms | Federstift |
| ☐ | Weiße und schwarze Bremsarme nebeneinander | Vergleich |
| ☐ | Federn beider Bremsarme nebeneinander | Vergleich |
| ☐ | Belagträger hinten zerlegt (Scheiben-Reihenfolge) | 🔴 Baustelle #3 |
| ☐ | Alte weiße Beläge vs. neue Spenderrad-Beläge nebeneinander | Vergleich Länge/Form |
| ☐ | Seitenansicht Gabel mit Maßband am Sockel | Sockelhöhe |

## 8. 💰 Einkaufsbedarf

| Teil | Spec | Prio | ca. Preis | bestellt? |
|---|---|---|---|---|
| Schleifleinen 400/600 | Bremssockel entlacken | 🔴 | 3 € | ☐ |
| **V-Brake-Beläge** | Länge ~70 mm, für Alu-Felgen, Gewindebolzen mit Konvex/Konkav | 🔴 | 6–15 € | ☐ |
| **Bremszug-Set** | Innenzug **1,5 mm** Edelstahl + Hülle **5 mm spiral** + Endhülsen | 🔴 | 12–20 € | ☐ |
| Neue V-Brake vorne | ❓ Sockelhöhe beachten (26"/28") | 🟡 | 15–30 € | ☐ |
| Zughüllenschneider | oder scharfer Seitenschneider + Feile | 🟡 | 15–30 € | ☐ |
| Cantisockel zum Einschrauben | ❓ M8/M10 – **nur bei Alugabel** | 🟢 | 5–15 € | ☐ |
| Bremssockel-Adapter | nur bei 26"/28"-Versatz | 🟢 | 15–30 € | ☐ |
| Teflon-Fett für Züge | | 🟢 | 5 € | ☐ |

## 9. Verknüpfungen

- [`../04-diagnose/vordere-bremsarme-sockel.md`](../04-diagnose/vordere-bremsarme-sockel.md) – Baustelle #4
- [`../04-diagnose/hintere-bremse-kehrt-nicht-zurueck.md`](../04-diagnose/hintere-bremse-kehrt-nicht-zurueck.md) – Baustelle #3
- [`../05-anleitungen/bremsen-einstellen.md`](../05-anleitungen/bremsen-einstellen.md) – Einstellanleitung
- [`../05-anleitungen/referenzwerte.md`](../05-anleitungen/referenzwerte.md) – Momente & Maße
- [`../02-teile/30-laufrad-reifen-nabe.md`](30-laufrad-reifen-nabe.md) – Felgen-Bremsflanke
