# Logbuch – 2026-09-03 – Rückfrage: drei Diagnosen korrigiert

**Dauer:** 20 min · **Baustellen:** #3, #4, #5, #6, #13 · **Nächster Schritt:** Session 1 – Diagnose & Messen

## Auslöser

Vier Rückfragen an den Besitzer, um die `❓ TODO`-Lücken zu füllen. Die Antworten haben
**drei Diagnosen aus der Ursprungs-Zusammenfassung korrigiert** und eine Baustelle komplett
entwarnt.

## Die Antworten

| Frage | Antwort |
|---|---|
| Ist das Vorderrad ein Nabendynamo? | ✅ **Ja** |
| Welcher Bremsentyp? | ✅ **V-Brake** |
| Marke des weißen Rads? | ✅ **STAIGER** |
| Marke des Spenderrads? | ❓ „irgendwas Deutsches“, muss noch nachgeschaut werden |
| Welche Bremshebel sind montiert? | ⚠️ → siehe unten, hier lag die **wichtigste Klarstellung** |

## 🔴 Wichtigste Klarstellung: „Hebel“ war doppelt belegt

Der Besitzer hat zurecht darauf hingewiesen, dass es am Fahrrad mit Felgenbremse **zwei
verschiedene „Hebel“** gibt:

| Umgangssprachlich | Korrekt | Wo |
|---|---|---|
| „Bremshebel“ / „Armatur“ | **Bremshebel** (brake lever) | **am Lenker** |
| „die zwei Hebel unten an der Bremse“ | **Bremsarme** (brake arms) | an Gabel / Hinterbau |

**Die tatsächliche Konfiguration:**

| Position | Bremshebel (Lenker) | Bremsarme (Zange) | Beläge |
|---|---|---|---|
| **vorne** | ✅ weiß, original | ⚠️ **schwarz** (Spenderrad) | ❓ |
| **hinten** | ✅ weiß, original | ✅ **weiß**, original | ⚠️ **schwarz** (Spenderrad) |

**Warum die Bremsarme vorne getauscht wurden:** Die guten weißen Bremsarme passten nicht auf
den **Bremssockel** (den Stahlstift mit Innengewinde) der schwarzen Gabel.

**Warum die Beläge hinten getauscht wurden:** Die weißen Beläge waren „ziemlich runter“.

## Konsequenzen für die Diagnosen

### 1. Baustelle #13 „Vorderrad dreht nicht frei“ → ✅ ENTWARNT

Es ist ein **Nabendynamo**. Der dreht von Hand konstruktionsbedingt nur **1–2 Umdrehungen**
weiter – das ist normal und kein Defekt. Rollwiderstand auf der Straße ca. 1–3 W.
→ Priorität von 🔴 auf 🟢. Es bleibt nur ein **Verifikationstest** (7 Schritte), damit kein
echter Lagerschaden übersehen wird.

### 2. Baustelle #5 „Bremshebel zu weich“ → komplett neu eingeordnet

- Es geht **nicht** um die Bremshebel am Lenker (die sind original weiß und in Ordnung)
- Es geht um die **Bremsarme vorne** vom Spenderrad
- **„Die kleinen Stellschrauben ändern wirklich nur wenig“ ist konstruktiv normal:** Die
  Federspannschraube hat nur ±2–3 Umdrehungen Verstellweg und dient der **Zentrierung**,
  nicht der Rückstellkraft
- 💡 **Die echte Stellgröße ist die Federraste:** Der Federstift am Bremsarm kann in **eine
  von drei Bohrungen** im Bremssockel gesetzt werden. **0 €, 10 min.**
- 💡 Zweite 0-€-Maßnahme: die **Federn der weißen Bremsarme** in die schwarzen umsetzen
- 💡 Dritte Maßnahme (3 €): Bremssockel mit **400er Schleifleinen entlacken** – das ist die
  häufigste Ursache dafür, dass ein Bremsarm „nicht auf die Aufnahme passt“

**Zum geplanten Sockel-Tausch** (der Besitzer wollte „die Stahlstifte selbst tauschen“):

| Gabelmaterial | Sockel-Befestigung | Tauschbar? |
|---|---|---|
| **Stahl** | angeschweißt / aufgelötet | ❌ **nein** – Gabel ist ein Sicherheitsbauteil, nicht selbst schweißen/bohren |
| **Alu** | oft eingeschraubt (Stahlbolzen mit 2 Abflachungen, M8/M10) | ✅ ja, mit Schraubensicherung |

→ **Magnet-Test an der Gabel ist jetzt eine der ersten Messungen.**

**Neue Erkenntnis aus der Recherche:** Die Bremssockel-Höhe ist **laufradgrößenabhängig**
(Shimano-Referenz: Abstand Mitte Ausfallende → Mitte Sockel: 26" ≈ **253,5 mm**,
28" ≈ **283 mm**). Falls die schwarze Gabel für 26" gebaut ist, sitzen die Bremsarme ca.
30 mm zu tief – dann „passen“ die weißen Arme geometrisch nicht, egal wie der Sockel aussieht.

### 3. Baustelle #3 „Hintere Bremse kehrt nicht zurück“ → Verdacht verschoben

Zange ✅ original · Federn ✅ original · Zug ✅ original – **aber die Beläge wurden getauscht**.
Damit sind die **Spenderrad-Beläge der Hauptverdächtige**, nicht der Zug.

Mögliche Fehler beim Belagwechsel, die genau dieses Symptom erzeugen:

| Fehler | Wirkung |
|---|---|
| **Konvex-/Konkavscheiben dünn/dick vertauscht** | Belag kann nicht schwenken, verkantet → kehrt nicht zurück (**sehr häufig!**) |
| Beläge zu kurz (Canti ~55–65 mm statt V-Brake ~70 mm) | liegen nicht voll auf der Flanke, Kante gräbt sich ein |
| Belag zu hoch/tief positioniert | trifft die Felgenoberkante oder die **scharfe Kante der abgefahrenen Bremsflanke** |
| Belag verhärtet/verglast (lange Standzeit am Spenderrad) | bleibt an der Felge kleben |

**Zusatz-These:** Falls die Felgen-Bremsflanke abgefahren ist (Baustelle #2), hat sie eine
**scharfe Kante**. Die neuen, weichen Spenderrad-Beläge graben sich dort fest – die alten,
eingelaufenen Beläge hatten sich an die Kante angepasst. Das passt zeitlich exakt.

### 4. Synergie: eine Maßnahme löst zwei Baustellen

Baustelle #5 (Bremsarme passen nicht auf den Sockel) und #6 (zu wenig Gewinde für die
Kontermutter) haben dieselbe Wurzel: **die fremde Gabel**.
→ Kommt die **weiße Original-Gabel** zurück, sind beide Probleme weg. Neu lösen müsste man
dann nur die Schutzblech-Befestigung vorne (Universal-/P-Schellen, 💰 3–8 €).

**🔴 Neue erste Frage: Ist die alte weiße Gabel noch vorhanden?**

### 5. Marke STAIGER – Kontext

Gegründet 1898/99 von **Paul Staiger** (1897 württembergischer Radrennmeister) in Stuttgart,
ab 1982 Gerlingen, 1988 Übernahme durch die **E. Wiener GmbH (Winora)** in Schweinfurt,
1997 Winora-Staiger GmbH, seit 2002 **Accell Group** (NL). Staiger stand für solide deutsche
Tourenräder.

→ **Baujahr-Eingrenzung:** Winora-Staiger-Ära = 1997 oder später. Mit 3×9 Shimano +
Nabendynamo + V-Brake grob **ca. 2000–2008**.

## Geänderte Dateien

| Datei | Änderung |
|---|---|
| `README.md` | Mischkonfigurations-Tabelle, neue Priorisierung, Begriffs-Trennung |
| `01-bikes/weisses-trekkingbike.md` | STAIGER, V-Brake, Nabendynamo, Brems-Aufteilung |
| `01-bikes/schwarzes-spenderrad.md` | Bremsarme/Beläge als entnommene Teile |
| `02-teile/40-bremsen.md` | **komplett neu geschrieben** – Bremsarme statt Bremshebel, Federraste, Bremssockel |
| `02-teile/00-fachbegriffe-glossar.md` | Bremsarme, Bremssockel, Federraste, Nudel, Faltenbalg |
| `03-todos/offene-baustellen.md` | neue Priorisierung, Korrekturen, Synergie-Hinweis |
| `03-todos/einkaufsliste.md` | V-Brake-Beläge, Schleifleinen, Kettenpeitsche; Hebel entfallen |
| `03-todos/werkzeug-und-material.md` | Schleifleinen, Gabelschlüssel, Ersatzteilkiste (alte Gabel!) |
| `04-diagnose/vorderrad-schwergaengig.md` | Nabendynamo bestätigt → Verifikationstest statt Reparatur |
| `04-diagnose/hintere-bremse-kehrt-nicht-zurueck.md` | **neuer Abschnitt 0: Beläge zuerst** |
| `04-diagnose/vordere-bremsarme-sockel.md` | **neu angelegt** |
| `04-messdaten/messdatenblatt.md` | Bremssockel-Messungen, Belag-Messungen, Dynamo bestätigt |

## Offene Punkte nach dieser Session

- [ ] 🔴 Ist die **alte weiße Gabel** noch vorhanden?
- [ ] 🔴 **Magnet-Test** an der schwarzen Gabel: Stahl oder Alu?
- [ ] 🔴 Quill-Vorbau-**Mindesteinstecktiefe** prüfen
- [ ] 🔴 **Felgen-Bremsflanken** prüfen (v + h)
- [ ] 🔴 **Hintere Beläge** prüfen: Länge, Scheiben-Reihenfolge, Position
- [ ] 💡 **Federraste vorne** in ein anderes Loch setzen (0 €, 10 min)
- [ ] Marke/Modell des Spenderrads nachschauen
- [ ] Modell + Baujahr des weißen STAIGER-Rads finden
- [ ] Abstand Mitte Ausfallende → Mitte Bremssockel messen (26" oder 28"?)

## Nächster Schritt

**Session 1: Diagnose & Messen** – Reihenfolge siehe
[`../03-todos/offene-baustellen.md`](../03-todos/offene-baustellen.md).
Die vier 🔴-Prüfungen zuerst (Vorbau-Einstecktiefe, Felgenflanken, hintere Beläge, Magnet-Test),
dann die 0-€-Reparatur Federraste, dann das Messdatenblatt ausfüllen.
