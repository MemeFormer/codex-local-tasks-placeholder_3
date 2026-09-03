# 📌 Offene Baustellen

Stand: 2026-09-03 · Quelle: zwei Zusammenfassungen + **Rückfrage beim Besitzer** (siehe
[`../06-logbuch/2026-09-03-rueckfrage-korrekturen.md`](../06-logbuch/2026-09-03-rueckfrage-korrekturen.md))

**Legende:** 🔴 hoch (Sicherheit/Funktion) · 🟡 mittel · 🟢 niedrig (Komfort/Optik)
Status: `🔴 offen` · `🟠 in Arbeit` · `🟡 Diagnose fehlt` · `✅ erledigt` · `🟢 entwarnt`

---

## 🔄 Was sich durch die Rückfrage geändert hat

| Vorher (aus der Zusammenfassung) | Jetzt (geklärt) | Konsequenz |
|---|---|---|
| „Vorderrad dreht nicht frei“ – 🔴 hoch | ✅ **Es ist ein Nabendynamo.** Von Hand nur 1–2 Umdrehungen = **normal** | 🟢 **entwarnt**, nur Verifikationstest |
| „Bremshebel zu weich, Federn zu schwach“ | Die **Bremshebel am Lenker sind die originalen weißen** (gut). Gemeint waren die **Bremsarme vorne** (vom Spenderrad) | völlig anderer Reparaturweg, **viel einfacher** |
| „Bolzen tauschen?“ (Pivot-Bolzen am Hebel) | Gemeint war der **Bremssockel** (Stahlstift an der Gabel), auf den die Bremsarme gesteckt werden | Tausch nur bei **Alugabel** möglich (eingeschraubt), bei **Stahlgabel** angeschweißt → ❌ nicht selbst |
| „Die kleinen Stellschrauben ändern nur wenig“ | ✅ **Konstruktiv normal.** Die echte Stellgröße ist die **Federraste** (3 Bohrungen im Sockel) | 💡 **0-€-Lösung**, 10 min |
| Hintere Bremse: „Zug/Hülle wahrscheinlich“ | Zange, Federn, Zug sind original – **nur die Beläge wurden getauscht** (Spenderrad) | 🔴 **Beläge sind der Hauptverdacht** |
| Bremsentyp unbekannt | ✅ **V-Brake** (long pull, Zug 1,5 mm, Hülle 5 mm) | Zugweg-Falle entfällt, Ersatzteil-Specs klar |
| Marke unbekannt | ✅ **STAIGER** (weißes Rad) | Baujahr eingrenzbar, evtl. Modellrecherche möglich |

---

## Übersicht (neue Priorisierung)

| # | Baustelle | Prio | Status | Nächster konkreter Schritt | Detail |
|---|---|---|---|---|---|
| 1 | 🔴 **Quill-Vorbau-Mindesteinstecktiefe** prüfen | 🔴 | 🔴 offen | Markierung suchen, prüfen ob sie **im** Schaftrohr liegt | [`../02-teile/20-steuersatz-gabel-vorbau-lenker.md`](../02-teile/20-steuersatz-gabel-vorbau-lenker.md) |
| 2 | 🔴 **Felgen-Bremsflanken** prüfen (v + h) | 🔴 | 🔴 offen | Verschleißindikator + Muldentiefe messen | [`../02-teile/30-laufrad-reifen-nabe.md`](../02-teile/30-laufrad-reifen-nabe.md) Abs. 2.3 |
| 3 | 🔴 **Hintere Bremse kehrt nicht zurück** | 🔴 | 🟡 Diagnose fehlt | **Abschnitt 0: Beläge prüfen** (Scheiben-Reihenfolge, Länge, Kante) | [`../04-diagnose/hintere-bremse-kehrt-nicht-zurueck.md`](../04-diagnose/hintere-bremse-kehrt-nicht-zurueck.md) |
| 4 | Hinterrad schwerer laufend + verlorene Feder | 🔴 | 🟡 Diagnose fehlt | Kontermutter 1/8 Umdrehung lösen, Feder identifizieren | [`../04-diagnose/hinterrad-lager-feder.md`](../04-diagnose/hinterrad-lager-feder.md) |
| 5 | **Vordere Bremsarme zu weich** + passen nicht auf den Sockel | 🟡 | 🟡 Diagnose fehlt | 💡 **Federraste in anderes Loch** + Sockel mit 400er Schleifleinen entlacken + Magnet-Test Gabel | [`../04-diagnose/vordere-bremsarme-sockel.md`](../04-diagnose/vordere-bremsarme-sockel.md) |
| 6 | Steuersatz-Gewinde: dauerhafte Lösung | 🟡 | 🔴 offen | Gewindesteigung + Schlüsselweite messen, flache Mutter besorgen. 💡 **Oder: alte weiße Gabel zurück** | [`../02-teile/20-steuersatz-gabel-vorbau-lenker.md`](../02-teile/20-steuersatz-gabel-vorbau-lenker.md) |
| 7 | Neue Kette (Kette zu kurz) | 🟡 | 🔴 offen | Big-Big-Test, Kettenstrebenlänge messen, 9-fach-Kette bestellen | [`../02-teile/10-antrieb-schaltung-kette.md`](../02-teile/10-antrieb-schaltung-kette.md) |
| 8 | Ständer-Winkel zu schräg | 🟢 | 🔴 offen | Kipprichtung klären, Lochabstand messen, Distanzscheiben | [`../02-teile/70-staender-gepaecktraeger.md`](../02-teile/70-staender-gepaecktraeger.md) |
| 9 | Lenker-Ergonomie / Sitzposition | 🟢 | 🟠 beobachten | erst nach 3–5 Fahrten bewerten. ⚠️ evtl. Geometrie-Änderung durch fremde Gabel | [`../02-teile/20-steuersatz-gabel-vorbau-lenker.md`](../02-teile/20-steuersatz-gabel-vorbau-lenker.md) |
| 10 | Teile identifizieren + Stammdaten ausfüllen | 🟡 | 🔴 offen | Aufdrucke fotografieren, Messdatenblatt ausfüllen | [`../04-messdaten/messdatenblatt.md`](../04-messdaten/messdatenblatt.md) |
| 11 | Kassette vom Spenderrad lösen (optional) | 🟢 | 🔴 offen | 💡 **Kettenpeitsche** besorgen – ohne die dreht sich das Paket mit | [`../02-teile/10-antrieb-schaltung-kette.md`](../02-teile/10-antrieb-schaltung-kette.md) Abs. 4 |
| 12 | Testfahrt + Gesamtcheck | 🟡 | 🔴 offen | [`sicherheitscheck.md`](sicherheitscheck.md) | |
| ~~13~~ | ~~Vorderrad dreht nicht frei~~ | 🟢 | ✅ **entwarnt** | **Nabendynamo** – normal. Nur Verifikationstest (7 Schritte) | [`../04-diagnose/vorderrad-schwergaengig.md`](../04-diagnose/vorderrad-schwergaengig.md) |

---

## 💡 Der Synergie-Effekt: eine Maßnahme, zwei Baustellen

Baustelle **5** und **6** haben dieselbe Wurzel: **die fremde (schwarze) Gabel**.

| Baustelle | Problem | Wurzel |
|---|---|---|
| 5 | Die guten weißen Bremsarme passen nicht auf den Bremssockel | fremder Sockel an der schwarzen Gabel |
| 6 | Zu wenig Gewinde für die Kontermutter | schwarzer Schaft ist zu kurz für den weißen Steuerkopf |

**Kommt die weiße Original-Gabel zurück, sind beide Probleme weg.** Neu lösen müsste man dann
nur:
- Schutzblech-Befestigung vorne (die schwarze Gabel hatte die passenden Ösen) →
  **Universal-Schellen / P-Schellen**, 💰 3–8 €
- Bremssockel-Höhe prüfen (war original passend)

**⚠️ Erste Frage: Ist die alte weiße Gabel noch vorhanden?**
→ [`werkzeug-und-material.md`](werkzeug-und-material.md) Abschnitt 4 „Ersatzteilkiste“

**Zusätzlicher Bonus:** Falls die schwarze Gabel eine **geringere Einbauhöhe** hat, ist auch
das „ungewohnte Lenker-Gefühl“ (Baustelle 9) teilweise erklärt – steilerer Lenkwinkel,
weniger Nachlauf, nervöseres Lenken. Das wäre mit der Originalgabel ebenfalls erledigt.

---

## Empfohlene Reihenfolge der Werkstatt-Sessions

Nicht alles auf einmal. Diese Reihenfolge minimiert Umbauten und Kosten.

### Session 1 – Diagnose & Messen (60–90 min, kaum Werkzeug nötig, 0 €)

**Ziel: nichts reparieren, nur herausfinden.** Danach weißt du, was du bestellen musst.

1. 🔴 **Quill-Vorbau-Einstecktiefe** prüfen → Baustelle 1
2. 🔴 **Felgen-Bremsflanken** prüfen (v + h) → Baustelle 2
3. 🔴 **Hintere Beläge** prüfen: Länge, Konvex/Konkav-Reihenfolge, Position auf der Flanke,
   Felgenkante → Baustelle 3 (Abschnitt 0)
4. 💡 **Federraste vorne** in ein anderes Loch setzen + Sockel entlacken + **Magnet-Test Gabel**
   → Baustelle 5 (das ist schon eine Reparatur, kostet aber nichts)
5. Hinterrad: Kontermutter prüfen, **Feder identifizieren** → Baustelle 4
6. Nabendynamo-Verifikationstest (7 Schritte) → Baustelle 13
7. Alle Modellnummern fotografieren + [`Messdatenblatt`](../04-messdaten/messdatenblatt.md) ausfüllen → Baustelle 10
8. Konusschlüssel-Größen messen, Gewindesteigung Steuersatz bestimmen
9. Klären: **Ist die alte weiße Gabel noch da?** → entscheidet über Baustelle 5 + 6

**Output:** ausgefülltes Messdatenblatt + [`Einkaufsliste`](einkaufsliste.md)

### Session 2 – Bestellen (0 min Werkstatt)

Aus der [`Einkaufsliste`](einkaufsliste.md) bestellen. Wartezeit für Session 3 nutzen.

### Session 3 – Hintere Bremse + Lager (60–90 min)

1. Beläge hinten korrekt montieren (oder neue V-Brake-Beläge) → Baustelle 3
2. Falls immer noch: Binärsuche Zug/Hülle/Zange → Baustelle 3
3. Hinterrad-Lager einstellen, Feder ersetzen → Baustelle 4
4. Schnellspanner korrekt spannen

### Session 4 – Vordere Bremse (30–60 min)

1. Federraste, Federtausch (weiße Federn in die schwarzen Arme) → Baustelle 5
2. Sockel reinigen + fetten → Baustelle 5
3. Falls die weiße Gabel da ist: **Gabel zurückbauen** → löst Baustelle 5 + 6
4. Schutzblech vorne neu befestigen (Universal-Schellen)

### Session 5 – Steuersatz dauerhaft sichern (30 min)

1. Flache Mutter montieren + Loctite 243 (Gewinde vorher entfetten!) → Baustelle 6
2. Lackstift-Markierung setzen, Kontrollroutine einrichten

### Session 6 – Neue Kette (45 min)

1. Länge berechnen (nicht die alte Kette als Maß nehmen!), kürzen, montieren → Baustelle 7
2. Big-Big-Test wiederholen, Schaltung neu justieren

### Session 7 – Kleinkram (30 min)

1. Ständer-Winkel → Baustelle 8
2. Lenker-Ergonomie bewerten → Baustelle 9
3. Schutzbleche final prüfen

### Session 8 – Testfahrt

[`Sicherheitscheck`](sicherheitscheck.md) durchgehen, dann längere Probefahrt.

---

## Baustellen-Detail (Arbeitskopie)

### 1. 🔴 Quill-Vorbau-Mindesteinstecktiefe (neu hinzugekommen)

| Feld | Wert |
|---|---|
| Symptom | Gabelschaft steht nur 1–2 Gewindegänge über → Schaft ist sehr kurz |
| Risiko | Steht die „MIN INSERTION“-Markierung **über** der Schaftoberkante, wirkt eine große Hebelkraft an der Schaftkante → 🔴 **Gabelschaft-Bruch, schwerer Unfall** |
| Prüfung | Markierung am Vorbau suchen → messen, wie tief das Einsteckteil im Schaftrohr sitzt |
| Falls zu flach | nicht fahren. Lösung: Gabel mit längerem Schaft, oder Ahead-Vorbau (klemmt außen, braucht weniger Tiefe) |
| Detail | [`../02-teile/20-steuersatz-gabel-vorbau-lenker.md`](../02-teile/20-steuersatz-gabel-vorbau-lenker.md) Abs. 6 |
| Ergebnis | ❓ |

### 2. 🔴 Felgen-Bremsflanken

| Feld | Wert |
|---|---|
| Symptom | Bremsflanken am weißen Rad waren abgefahren; Original-Hinterrad ist wieder eingebaut |
| Risiko | Felgendurchbruch unter Bremsdruck (Felgenplatzer) |
| **Zusatz-Zusammenhang** | Eine **scharfe Felgenkante** ist ein Hauptverdächtiger für Baustelle 3 – die neuen weichen Beläge haken daran |
| Prüfung | Verschleißindikator sichtbar? Muldentiefe messen? Kante mit dem Fingernagel prüfen |
| Detail | [`../02-teile/30-laufrad-reifen-nabe.md`](../02-teile/30-laufrad-reifen-nabe.md) Abs. 2.3 |
| Ergebnis | ❓ |

### 3. 🔴 Hintere Bremse kehrt nicht selbstständig zurück

| Feld | Wert |
|---|---|
| Symptom | Beläge gehen nach dem Loslassen nicht von der Felge weg |
| Original übernommen | ✅ Zange · ✅ Federn · ✅ Zug |
| **Geändert** | ⚠️ **Beläge** (vom Spenderrad, weil die weißen runter waren) |
| 🔴 **Hauptverdacht** | Beläge: Konvex-/Konkavscheiben vertauscht (dünn/dick), Beläge zu kurz (Canti statt V-Brake ≈ 70 mm), Belag trifft die scharfe Felgenkante, Belag verhärtet |
| Zweiter Verdacht | Zug/Hüll-Reibung durch neue Verlegung |
| Vorgehen | **Erst Abschnitt 0 (Beläge, 10 min, 0 €)**, dann Binärsuche |
| Detail | [`../04-diagnose/hintere-bremse-kehrt-nicht-zurueck.md`](../04-diagnose/hintere-bremse-kehrt-nicht-zurueck.md) |
| Material | ggf. neue V-Brake-Beläge (💰 6–15 €), ggf. Bremszug-Set 1,5 mm + Hülle 5 mm (💰 12–20 €) |
| Ergebnis | ❓ |

### 4. Hinterrad schwerer laufend + verlorene Feder 🔴

| Feld | Wert |
|---|---|
| Symptom | Rad läuft schwerer als vor dem Umbau |
| Bekannte Fehler | Kontermutter zu fest angezogen · **eine kleine Feder verloren** |
| Vermutung | Lager zu stark vorgespannt. Feder = wahrscheinlich **Schnellspanner-Feder** (oder Wellenscheibe) |
| 💡 These | Wenn die QR-Feder fehlt, verkantet der Schnellspanner beim Spannen und **drückt das Lager zusammen** – das allein könnte die Schwergängigkeit erklären |
| Vorgehen | QR komplett entfernen und drehen → läuft es frei? Dann liegt es am QR |
| Detail | [`../04-diagnose/hinterrad-lager-feder.md`](../04-diagnose/hinterrad-lager-feder.md) |
| Werkzeug | Konusschlüssel ❓ Größe, Fett, ggf. Ersatzfeder |
| Ergebnis | ❓ |

### 5. 🟡 Vordere Bremsarme zu weich / Federn zu schwach (korrigiert)

| Feld | Wert |
|---|---|
| Symptom | Bremsarme vorne (vom Spenderrad) fühlen sich weich an, schnappen schwach zurück |
| ❌ **Nicht** das Problem | Die Bremshebel am Lenker – die sind die **originalen weißen** und in Ordnung |
| Bisher versucht | Federspannschrauben → „ändern wirklich nur wenig“ |
| 💡 **Erklärung** | Die Federspannschraube hat konstruktiv nur ±2–3 Umdrehungen und dient der **Zentrierung**, nicht der Rückstellkraft. Das Verhalten ist **normal** |
| 💡 **Lösung 1 (0 €)** | **Federraste**: Federstift in ein **anderes der 3 Löcher** im Bremssockel setzen (beide Arme ins gleiche Loch) |
| 💡 **Lösung 2 (0 €)** | **Federn der weißen Bremsarme** in die schwarzen umsetzen (V-Brake-Federn sind meist baugleich) |
| 💡 **Lösung 3 (3 €)** | Bremssockel mit 400er Schleifleinen **entlacken** → häufigste Ursache, warum die weißen Arme „nicht passten“ |
| ⚠️ Sockel-Tausch | Nur bei **Alugabel** (eingeschraubt, M8/M10). Bei **Stahlgabel** ist er angeschweißt → ❌ nicht selbst. **Magnet-Test!** |
| 💡 **Lösung 4** | **Weiße Original-Gabel zurück** → löst Baustelle 5 **und** 6 gleichzeitig |
| Detail | [`../04-diagnose/vordere-bremsarme-sockel.md`](../04-diagnose/vordere-bremsarme-sockel.md) |
| Ergebnis | ❓ |

### 6. Steuersatz-Gewinde – dauerhafte Lösung 🟡 (sicherheitsrelevant)

| Feld | Wert |
|---|---|
| Symptom | nur 1–2 Gewindegänge frei → keine Kontermutter möglich |
| Aktuell | Mutter + Loctite 243, regelmäßige Kontrolle |
| ⚠️ Hinweis | Loctite wirkt **nicht auf fettigem Gewinde** → vorher mit Bremsenreiniger/Isopropanol entfetten, 24 h aushärten lassen |
| Dauerhaft (kurz) | **flache Steuersatz-Mutter** – ⚠️ **1" × 24 tpi bzw. 1⅛" × 24 tpi, kein Metrik-Gewinde, nicht aus dem Baumarkt!** |
| Dauerhaft (sauber) | 💡 **Weiße Original-Gabel zurück** (falls vorhanden) oder gebrauchte Gabel mit langem Schaft |
| Detail | [`../02-teile/20-steuersatz-gabel-vorbau-lenker.md`](../02-teile/20-steuersatz-gabel-vorbau-lenker.md) |
| Ergebnis | ❓ |

### 7. Neue Kette 🟡

| Feld | Wert |
|---|---|
| Symptom | Kette durch Reparatur ~½–1 Glied zu kurz |
| Risiko | Big-Big überstreckt das Schaltwerk → Schaltauge/Käfig-Schaden |
| Lösung | **9-fach**-Kette, Länge neu berechnen (⚠️ **nicht** die alte Kette als Maß nehmen!) |
| Detail | [`../02-teile/10-antrieb-schaltung-kette.md`](../02-teile/10-antrieb-schaltung-kette.md) Abs. 3 |
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
| Bewertung | vermutlich Gewöhnung + Einstellsache |
| ⚠️ Zusatz-Aspekt | Falls die schwarze Gabel eine **geringere Einbauhöhe** hat: steilerer Lenkwinkel, weniger Nachlauf → **nervöseres Lenken**. Das ist keine Einstellsache, sondern Geometrie |
| Plan | 3–5 Fahrten, dann bewerten. Einstellmöglichkeiten ohne Teiletausch: Vorbauwinkel/-höhe, Lenker drehen, Hebelposition, Sattelposition |
| Detail | [`../02-teile/20-steuersatz-gabel-vorbau-lenker.md`](../02-teile/20-steuersatz-gabel-vorbau-lenker.md) Abs. 7 |
| Ergebnis | ❓ |

### 10. Teile identifizieren & dokumentieren 🟡

| Teilschritt | Erledigt |
|---|---|
| ✅ Hersteller weißes Rad bekannt: **STAIGER** | ☑ |
| Hersteller/Modell/Rahmennummer des Spenderrads | ☐ |
| Modell + Baujahr des weißen Rads | ☐ |
| Alle Shimano-Aufdrücke fotografieren | ☐ |
| [`Messdatenblatt`](../04-messdaten/messdatenblatt.md) ausfüllen | ☐ |
| Modellnummern in die `02-teile/`-Dateien eintragen | ☐ |
| ❓ TODO-Markierungen löschen, wo Werte eingetragen sind | ☐ |

### 11. Kassette vom Spenderrad lösen (optional) 🟢

| Feld | Wert |
|---|---|
| Symptom | „Lockring hat nichts gebracht, Ritzel haben sich nicht bewegt“ |
| 💡 **Erklärung** | Ohne **Kettenpeitsche** dreht sich das Ritzelpaket einfach mit – exakt dieses Symptom. Der Lockring braucht **30–50 Nm** |
| Vorher klären | Ist es eine **Kassette** (Lockring, 12-Spline) oder ein **Schraubkranz** (freewheel, aufgeschraubt)? Anderes Werkzeug! |
| Notlösung | alte Kette um ein großes Ritzel wickeln + Knebel als Hebel |
| Bewertung | 🟢 **Nicht dringend.** Das Original-Hinterrad läuft, die 9-fach-Kassette passt zur Schaltung |
| Detail | [`../02-teile/10-antrieb-schaltung-kette.md`](../02-teile/10-antrieb-schaltung-kette.md) Abs. 4 |
| Ergebnis | ❓ |

### 13. ~~Vorderrad dreht nicht frei~~ → ✅ ENTWARNT

| Feld | Wert |
|---|---|
| Symptom | „Vorderrad etwas schwergängig“ |
| ✅ **Geklärte Ursache** | Es ist ein **Nabendynamo**. Der dreht von Hand konstruktionsbedingt nur **1–2 Umdrehungen** weiter |
| Bewertung | 🟢 **Normal, kein Defekt.** Rollwiderstand auf der Straße ca. **1–3 W** – messtechnisch kaum nachweisbar |
| Rest-Aufgabe | Nur der **Verifikationstest** (7 Schritte), damit kein echter Lagerschaden übersehen wird: Kabel abziehen, seitliches Spiel, „samtig-rastend“ vs. „rau/sandig“ |
| Detail | [`../04-diagnose/vorderrad-schwergaengig.md`](../04-diagnose/vorderrad-schwergaengig.md) |
| Ergebnis | ❓ Verifikationstest offen |

---

## ✅ Erledigt (Archiv)

| Datum | Was | Notiz |
|---|---|---|
| ❓ | Kettenreparatur mit Fremdschloss | Kette dadurch kürzer → Baustelle 7 |
| ❓ | Gabel- und Steuersatztausch | → Baustelle 1 + 6 |
| ❓ | Vorbau/Lenker montiert (winkelverstellbar, Faceplate) | Lenkerwechsel ohne Griffabbau möglich |
| ❓ | Bremsarme vorne vom Spenderrad montiert | weil die weißen nicht auf den Sockel passten → Baustelle 5 |
| ❓ | Bremsbeläge hinten vom Spenderrad montiert | weiße waren runter → Baustelle 3 |
| ❓ | Schutzbleche montiert (vorne über Originalpunkte der Gabel) | streifenfrei |
| ❓ | Rücklicht-Kabel neu gelötet + verlegt | Flachstecker entfernt |
| ❓ | Licht getestet: Nabendynamo + vorne/hinten funktionieren | ✅ |
| ❓ | Original-Hinterrad wieder eingebaut | Kassette ließ sich nicht lösen → Baustelle 11 |
| ❓ | Steuersatz eingestellt | freigängig, kein Spiel |
| ❓ | Kette/Schaltung/Umwerfer funktionieren | ✅ |

> Bitte Datumsangaben ergänzen und neue Einträge in [`../06-logbuch/`](../06-logbuch/) anlegen.
