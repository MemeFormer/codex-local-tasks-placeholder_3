# Logbuch – 2026-09-04 – Komponenten entschlüsselt: 6 offene Fragen beantwortet

**Dauer:** 60 min (Recherche) · **Baustellen:** #1–#10 · **Nächster Schritt:** Session 1 – Messen am Rad

Der Besitzer hat die Aufdrucke aller Komponenten abgelesen. Damit ließen sich **sechs offene
Fragen klären**, eine Baustelle **komplett neu bewerten** und eine **exakte Ursache** für das
Gewinde-Problem finden.

---

## Die gelieferten Daten

### Rahmen

| Feld | Wert |
|---|---|
| Rahmennummer | **AWO7230329** |
| Modell | **Staiger Daytona Sportline** |
| Material | **Alloy 6061, Double Butted** (Aluminium) |

### Komponenten

| Baugruppe | Aufdruck | Entschlüsselt |
|---|---|---|
| Sattelstütze + Schnellspanner | XLC-comp, „31,35 mm AD" | XLC = Winora-Hausmarke ✅ Original-Daytona-Teil. ⚠️ **31,35 mm passt nicht zur Sattelstütze** – Original-Spec ist **27,2 mm** |
| „Pedale" | Shimano Deore Hollowtech, 170, **FC-M530/531** | 🔴 **FC = Front Chainwheel = Kurbelgarnitur**, nicht Pedale! **170** = Kurbelarmlänge |
| Bremshebel | Shimano Deore LX **BL-M571; 22.2** | Bremshebel, **V-Brake/long pull**, Lenkerklemmung **22,2 mm** |
| Schalthebel | Shimano Deore LX **SL-M580; 22.2** | **9-fach Rapidfire-Trigger**, Klemmung 22,2 mm |
| Kettenblätter | Shimano, 3 Stück, „Mega Drive Train" | ❓ Zähne noch zählen. Zum FC-M530: **48-36-26** (Trekking) oder 44-32-22 |
| Ritzel | Shimano, 9 Stück | ✅ **9-fach-Kassette** bestätigt |
| Hinterrad-Nabe | Shimano Deore **FH-M530 VIAM** | **Freilaufnabe hinten**, 9-fach HG, Konuslager |
| Hinterrad-Felge | **Mach1 210**, ETRTO **622 × 19c**, Alloy 6060 | ✅ **Original-Daytona-Felge** (in der Original-Spec belegt) |
| Hinterrad-Reifen | **Schwalbe Marathon Plus 47-622**, 28×1.75, **3.0–5.0 bar** | ✅ Original-Daytona-Reifenfamilie |
| Vorderrad-Nabe | **Shimano DH-3N31-NT**, **6V-3W**, 400-716 mm, K911 | ✅ **Nabendynamo** |
| Vorderrad-Felge | **Shining Double Wall 622 × 19**, A-M4 | Alu-Hohlkammer, Innenbreite 19 mm |
| Vorderrad-Reifen | **Schwalbe Active Line K-Guard 42-622**, 28×1.60, HS 377 | ⚠️ **42 mm vorne vs. 47 mm hinten** |
| Bremszangen vorne | **Tektro** | ⚠️ vom Spenderrad |
| Bremsbeläge vorne | **62 mm**, Tektro **836** EN-STANDARD **B61** (li+re) | ✅ 62 mm Messung bestätigt die **63-mm-Nennlänge** der Tektro 836 |
| Bremszangen hinten | **Shimano Deore** | ✅ original |
| Bremsbeläge hinten | **62 mm**, Tektro 836 – li **B1**, re **B44** | ⚠️ **unterschiedliche Codes links/rechts** |
| Gabel | **SR Suntour NEX**, KB1E0817, **SF14 NEX P**, **700C TS T63** | 🔴 **siehe unten – die zentrale Erkenntnis** |
| „Schaltwerk vo." | Shimano **050 OP Swing SIS (GD-C 050)** | 🔴 heißt **Umwerfer**. Entschlüsselt: **Shimano FD-C050**, Top Swing, SIS, 3-fach |
| Schaltwerk hi. | Shimano Deore **RD-M511** | **9-fach, SGS-Langkäfig** |

---

## 🎯 Erkenntnis 1: Das Gewinde-Problem ist jetzt exakt erklärbar

Die **SR Suntour NEX mit Gewindeschaft** hat laut Händler-Spezifikation:

| Größe | Wert |
|---|---|
| Schaft-Ø außen | **28,6 mm = 1⅛ Zoll** |
| Schaftlänge (Handelsvarianten) | **210 mm** oder **225 mm** |
| 🔴 **Gewindelänge ab Werk** | **nur 55 mm** – am oberen Schaftende. Der Rest ist glatt |
| Achse bis Krone | 445–469 mm (50 mm) bzw. 477 mm (63 mm) |
| Gabelscheiden | **Aluminium** |

**Der Mechanismus:**

```
Ein Gewindesteuersatz braucht über dem Steuerrohr ca. 27 mm:
   Lagerkonus 7 mm + Mutter 10 mm + Kontermutter 10 mm

Der NEX-Gewindeschaft hat ab Werk nur 55 mm Gewinde – ganz oben.
Ein Gewindeschaft wird beim Einbau OBEN gekürzt → jedes abgesägte
Millimeter ist verlorene Gewindelänge.
```

→ Der Schaft wurde für den **kürzeren Steuerkopf des Spenderrads** gekürzt. Der STAIGER-Rahmen
hat ein ca. **23 mm längeres Steuerrohr** → es bleiben **1–2 Gewindegänge (ca. 2 mm)**.
**Das ist exakt der Befund.**

**Korrekturen gegenüber dem bisherigen Stand:**
- 🔴 Es ist **1⅛ Zoll × 24 tpi**, **nicht 1 Zoll**. Eine flache Mutter muss entsprechend bestellt werden.
- ⚠️ Eine flache Mutter bringt nur ca. 5 mm – bei 2 mm Rest **vermutlich nicht ausreichend**.
- 💡 **Neue konkrete Option:** Die NEX-Gewindegabel gibt es mit **210 mm und 225 mm** Schaft.
  Die 225-mm-Version bringt **+15 mm** → Problem gelöst, gleiche Geometrie. 💰 50–90 €
- 💡💡 **Beste Option: Ahead-Umbau.** Bei 1⅛ Zoll sind die Rahmenschalen für **Gewinde und
  Ahead identisch (34 mm / EC34)**. Eine gewindelose NEX (Schaft 255 mm) + Ahead-Steuersatz +
  Ahead-Vorbau macht das Gewinde-Problem **komplett verschwinden**. 💰 70–130 €

---

## 🎯 Erkenntnis 2: Die Federgabel passt – das Lenkproblem liegt woanders

Recherche zur Original-Ausstattung des **Staiger Daytona** ergab:
**Federgabel Suntour mit 63 mm Federweg**, **Felgen Mach1 210**, **XLC Comp** Vorbau/Sattelstütze/
Griffe, **Shimano Deore V-Brakes**, **Schwalbe Marathon**.

| Original-Daytona | Dein Rad | Treffer |
|---|---|---|
| Federgabel Suntour, **63 mm** | SR Suntour **NEX T63** (63 mm) | ✅ |
| Felgen **Mach1 210** | Mach1 210 (hinten) | ✅ |
| **XLC Comp** Vorbau, Sattelstütze, Griffe | XLC-comp Sattelstütze + Schnellspanner | ✅ |
| Shimano **Deore V-Brakes** | Bremszangen hinten Shimano Deore | ✅ |
| Schwalbe **Marathon** | Marathon Plus 47-622 | ✅ |

> 🎉 **Die NEX T63 ist geometrisch ein passender Ersatz für die originale Daytona-Gabel.**
> Die befürchtete Geometrie-Verfälschung (60–90 mm höhere Front durch eine Federgabel an einem
> Starrgabel-Rahmen) **trifft nicht zu** – das Daytona war ab Werk ein Federgabel-Rad.

**Damit verschiebt sich die Ursache für das „ungewohnte Lenker-Gefühl":**

| Neue Verdächtige | Prüfung |
|---|---|
| 🔴 **Federgabel-Vorspannung (Preload) falsch** oder Gabel trocken/schwergängig | Bremse ziehen, Rad nach unten drücken: federt sie leicht ein **und von selbst wieder aus**? Standrohre reinigen + dünn mit Federgabel-Öl benetzen |
| Breiterer, gekröpfter Lenker (Original: **XLC Comp Alu Flatbar** = gerade, schmal) | Lenker kürzen oder Flatbar zurück |
| Anderer Vorbau (Original: **XLC Comp**) | winkelverstellbaren Vorbau neu einstellen |
| Sattelposition | waagerecht, vor/zurück |

**Zusätzliche Prüfung:** Achse-bis-Krone-Maß der NEX messen (ca. 445–477 mm) und mit der
Original-Spec vergleichen. Falls die NEX-Variante deutlich abweicht, ändert sich die Geometrie doch.

---

## 🎯 Erkenntnis 3: Warum die weißen Bremsarme nicht auf die Gabel passten

Die Suntour NEX hat **Aluminium-Gabelscheiden** → der V-Brake-Sockel ist dort in der Regel ein
**eingeschraubter Stahlbolzen mit zwei Abflachungen** für einen Gabelschlüssel (nicht angeschweißt).

Ein gut dokumentiertes Problem – und zwar **spezifisch bei Shimano-Deore-Bremsarmen**:

| Maß | typisch |
|---|---|
| Länge des Sockel-Bunds | ca. **5,6 mm** |
| Tiefe der Ausnehmung im Deore-Bremsarm | ca. **4,3 mm** |
| → Spalt | ca. **1,3 mm** – der Arm liegt nicht an, „passt nicht auf die Aufnahme" |

**Belegter Fix:** Den eingeschraubten Sockel **ca. 2–2,5 mm zurückdrehen** → danach passt der
Bremsarm bündig. (In einem Schrauber-Forum exakt so mit einer Deore-V-Brake durchexerziert:
„Sockel um 2,5 mm zurück gesetzt! Jetzt passt.")

> 🎯 **Der Plan des Besitzers („die Stahlstifte selbst tauschen") ist damit machbar** –
> weil die Gabel Alu-Scheiden hat. Es muss nicht einmal getauscht werden, oft reicht
> **Zurückdrehen**. Grenze: mindestens **8–10 mm Gewindeeingriff** müssen bleiben.

**Zusätzlich bleibt die 0-€-Maßnahme:** Federspannung über die **Federraste** (3 Bohrungen im
Sockel) ändern – die Federspannschraube ist nur für die Zentrierung.

---

## 🎯 Erkenntnis 4: Die Bremsbeläge sind zu kurz – Hauptverdacht für Baustelle #3

**Tektro 836 = 63 mm V-Type-Beläge** (deine Messung 62 mm ✅ bestätigt das).

| | Wert |
|---|---|
| Verbaute Beläge | Tektro 836, **63 mm** |
| Shimano-Deore-V-Brakes sind ausgelegt für | **70 mm** (M70T4 = 72 mm, S65T = 70 mm) |
| Differenz | **7–10 mm zu kurz** |

**Warum das die nicht zurückkehrende Bremse erklären kann:**

1. **Fremder Scheibensatz:** Tektro-Beläge kommen mit eigenem Konvex-/Konkav-Satz. In einer
   Shimano-Deore-Zange kann die Stapelreihenfolge nicht stimmen → **der Belag steht schräg und
   verkantet** → kehrt nicht zurück. (Klassiker: dünne Konvexscheibe gehört armseitig, dicke außen.)
2. **Kürzerer Belag = andere Kantenposition:** Bei einer **abgefahrenen Bremsflanke mit scharfer
   Kante** hakt eine kurze Belagkante leichter ein.
3. **Weniger Auflagefläche** → ca. 10–15 % weniger Bremsleistung.
4. ⚠️ **Links/rechts unterschiedliche Codes** (B1 vs. B44) → falls verschiedene Mischungen,
   bremst und kehrt die Seite unterschiedlich zurück.

💰 **Empfehlung:** hinten auf **Shimano V-Brake-Beläge 70 mm** wechseln (M70T4 / S65T / M65T,
8–15 €) – inklusive korrektem Scheibensatz für die Deore-Zange.

---

## 🎯 Erkenntnis 5: Der Nabendynamo braucht eine ANDERE Einstellmethode

Zur **Shimano DH-3N31** gibt es einen wichtigen Praxis-Befund:

> Shimano-Nabendynamos sind ab Werk praktisch immer **zu stramm** eingestellt. Bei einem neuen
> Dynamo muss man den linken Konus oft um bis zu **eine halbe Umdrehung** lösen.
> **Und man kann es nicht erfühlen**, weil das magnetische Rasten des Dynamos die Wahrnehmung
> der Lager-Rauheit überdeckt.

**Korrekturen gegenüber der bisherigen Diagnose:**

| Vorher angenommen | Korrekt |
|---|---|
| „Nabendynamo = alles normal, nichts tun" | ⚠️ Der Rollwiderstand ist normal, **aber die Lagervorspannung ist sehr wahrscheinlich zu fest** |
| Leichtgängigkeit erfühlen („samtig-rastend" vs. „rau") | 🔴 **funktioniert beim Nabendynamo nicht** – das Magnet-Rasten täuscht. **Nur nach Spiel gehen!** |
| Lager wie bei einer normalen Nabe einstellen | 🔴 **Nur LINKS** einstellen (Seite ohne Kabelanschluss). Die Dynamo-Seite **nicht öffnen** – die Kabel sind extrem empfindlich |
| Ziel: spielfrei und leicht | 🎯 Ziel: **minimales Spiel ohne Schnellspanner, das beim Spannen des Schnellspanners gerade verschwindet** |

💡 **Fett nachfüllen ohne Zerlegen:** linken Konus lösen, Achse nach rechts drücken und mit
einer Spritze Fett durch den Dichtungsspalt auf der Dynamo-Seite pressen.

---

## 🎯 Erkenntnis 6: Exakte Ersatzteil-Specs für den Antrieb

Aus der Shimano-Dokumentation zum **FC-M530**:

| Teil | Exakte Spec |
|---|---|
| **Kette** | ✅ **Shimano CN-HG53 oder CN-HG73** (Original-Spec zum FC-M530), 9-fach |
| **Innenlager** | **BB-ES25 Octalink**, BSA 68 mm (1,37" × 24 tpi), Achslänge 113/118/121/126 mm, Kettenlinie 47,5 oder 50 mm |
| **Pedalgewinde** | **9/16" × 20 tpi** (bestätigt) |
| Kurbelarmlänge | **170 mm** ✅ |
| Schnittstelle | **Octalink** („Hollowtech" = hohlgeschmiedete Arme, **nicht** Hollowtech II!) |
| Kurbelabzieher | Standard-Kurbelabzieher (nach Entfernen der Kurbelschraube) |
| Innenlager-Werkzeug | **Octalink/ISIS-Vielzahn** (20-Spline, z. B. Shimano TL-FC15 / Park BBT-22) |

Zum **RD-M511** (Deore 9-fach, SGS):

| Wert | Spec |
|---|---|
| Max. größtes Ritzel | **34 Zähne** |
| Max. Differenz vorne | **22 Zähne** |
| Gesamtkapazität | **45 Zähne** |

**Kapazitätsprüfung** – beide wahrscheinlichen Kurbel-Varianten passen, aber **ohne Spielraum**:

| Kombination | Differenz vorne | Differenz hinten | Gesamt | Urteil |
|---|---|---|---|---|
| 48-36-26 + 11-32 | 22 ✅ (am Limit) | 21 | **43 ≤ 45** | ✅ |
| 44-32-22 + 11-34 | 22 ✅ (am Limit) | 23 | **45 = 45** | ✅ exakt an der Grenze |

Zum **Umwerfer FD-C050** (Top Swing, SIS, 3-fach):

| Wert | Spec |
|---|---|
| Befestigung | **5 mm Inbus, 5–7 Nm** |
| Klemmung | 28,6 / 31,8 mm |
| Max. großes Kettenblatt | **48 Zähne** |
| Kapazität | **20 Zähne** |
| Kettenlinie | 46,0 / 48,5 / 50,0 / 52,5+t mm |
| Für Kurbeltyp | **Spline (Octalink)** ✅ passt zum FC-M530 |

⚠️ **Auffälligkeit:** Der FD-C050 ist ein **einfaches Non-Series-Teil** mit **20 Zähnen
Kapazität**, die Kurbel hat aber **22 Zähne Differenz** → **0,5–2 Zähne über Spec.**
Funktioniert in der Praxis (und tut es bei dir ja auch), ist aber offiziell außerhalb der
Freigabe. Vermutlich Original-Ausstattung – Staiger hat beim Daytona günstigere Umwerfer
verbaut (spätere Baujahre: Acera FD-T3000).

---

## ⚠️ Offene Widersprüche / Klärbedarf

| Punkt | Befund | Klärung |
|---|---|---|
| **Sattelstütze 31,35 mm** | Original-Daytona-Spec: **XLC Comp 27,2 mm**. 31,35 mm passt nicht | Vermutlich das **Sitzrohr außen** oder die **Sattelklemme** gemessen. → **Zahl unter der Sattelstütze ablesen** |
| **Baujahr** | Rahmennummer `AWO7230329` | Hypothese **2007, KW 23** (`7` `23`). Passt zur Komponenten-Ära. Gegenprüfen |
| **Steuerkopf-Typ** | War das Daytona ab Werk für **Ahead** ausgelegt? | Bei 1⅛ Zoll sind die Rahmenschalen für Gewinde und Ahead **identisch (34 mm / EC34)**. Prüfen: **Konussitz an der Gabel 26,4 mm (Gewinde) oder 30 mm (Ahead)?** |
| **Vorderrad original?** | Felge **Shining A-M4** vorne vs. **Mach1 210** hinten – unterschiedliche Hersteller | Ist das Vorderrad original STAIGER oder vom Spenderrad? (Der Nabendynamo spricht für original) |
| **Reifenbreiten gemischt** | vorne **42-622**, hinten **47-622** | Welcher ist original? Schutzblech-Freigängigkeit bei 47 mm hinten prüfen |
| **„Mega Drive Train"** | keine Shimano-Bezeichnung | Kettenblatt-Aufdruck nochmal suchen / **Zähne zählen** |
| **Kassette** | „9 Stück, auch Shimano" | Modell + Abstufung fehlt – auf dem größten Ritzel oder unter dem Lockring |
| **Pedale** | unbekannt (FC-M530 ist die Kurbel) | Aufdruck an der Pedal-Innenseite |

---

## Geänderte Dateien

| Datei | Änderung |
|---|---|
| `01-bikes/weisses-trekkingbike.md` | **komplett neu geschrieben** mit allen entschlüsselten Daten |
| `02-teile/20-steuersatz-gabel-vorbau-lenker.md` | SR Suntour NEX, 1⅛ Zoll × 24 tpi, 55 mm Gewinde, Ahead-Option |
| `02-teile/10-antrieb-schaltung-kette.md` | FC-M530/Octalink/BB-ES25, CN-HG53, RD-M511, FD-C050, Kapazitätsrechnung |
| `02-teile/30-laufrad-reifen-nabe.md` | DH-3N31, FH-M530, Mach1 210, Shining A-M4, Reifenbreiten |
| `02-teile/40-bremsen.md` | BL-M571, 63-mm-Tektro-Beläge vs. 70-mm-Soll |
| `04-diagnose/vordere-bremsarme-sockel.md` | Sockel-Bund 5,6 mm vs. Arm-Ausnehmung 4,3 mm, Alu-Gabel bestätigt |
| `04-diagnose/hintere-bremse-kehrt-nicht-zurueck.md` | Tektro-836-Beläge als konkreter Hauptverdacht |
| `04-diagnose/vorderrad-schwergaengig.md` | Nabendynamo-Einstellmethode (nur links, nach Spiel nicht nach Gefühl) |
| `03-todos/offene-baustellen.md`, `einkaufsliste.md` | neue Prioritäten, exakte Bestell-Specs |
| `04-messdaten/messdatenblatt.md` | erledigte Punkte abgehakt |

## Nächster Schritt

**Session 1: Messen am Rad** – die 20 Punkte aus Abschnitt 9 der
[Bike-Datei](../01-bikes/weisses-trekkingbike.md), davon diese **fünf zuerst**:

1. 🔴 Zähne der Kettenblätter + Kassette zählen (→ Kettenlänge berechenbar)
2. 🔴 Quill-Vorbau: liegt der Innenkeil **unterhalb** des Gewindebereichs?
3. 🔴 Felgen-Bremsflanke v/h: Verschleißindikator + Muldentiefe
4. 🔴 Magnet-Test Gabelscheiden + hat der Bremssockel zwei Abflachungen?
5. 🔴 Sattelstützen-Ø **unter** der Stütze ablesen (27,2 erwartet)
