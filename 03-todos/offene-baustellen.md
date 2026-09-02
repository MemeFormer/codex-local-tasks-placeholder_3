# 📌 Offene Baustellen

Stand: 2026-09-02 · Quelle: zwei Zusammenfassungen + eigene Rückfragen

**Legende:** 🔴 hoch (Sicherheit/Funktion) · 🟡 mittel · 🟢 niedrig (Komfort/Optik)
Status: `🔴 offen` · `🟠 in Arbeit` · `🟡 Diagnose fehlt` · `✅ erledigt`

---

## Übersicht

| # | Baustelle | Prio | Status | Nächster konkreter Schritt | Detail |
|---|---|---|---|---|---|
| 1 | Vorderrad dreht nicht frei | 🔴 | 🟡 Diagnose fehlt | Schnelltest: Rad ausbauen, Achse in der Hand drehen | [`../04-diagnose/vorderrad-schwergaengig.md`](../04-diagnose/vorderrad-schwergaengig.md) |
| 2 | Hinterrad schwerer laufend + verlorene Feder | 🔴 | 🟡 Diagnose fehlt | Kontermutter 1/8 Umdrehung lösen, Feder identifizieren | [`../04-diagnose/hinterrad-lager-feder.md`](../04-diagnose/hinterrad-lager-feder.md) |
| 3 | Hintere Bremse kehrt nicht zurück | 🔴 | 🟡 Diagnose fehlt | Zug aushängen, prüfen ob die Zange allein zurückschnappt | [`../04-diagnose/hintere-bremse-kehrt-nicht-zurueck.md`](../04-diagnose/hintere-bremse-kehrt-nicht-zurueck.md) |
| 4 | Bremshebel zu weich / Federn zu schwach | 🟡 | 🔴 offen | Modellnummer ablesen → Zugweg prüfen → Pivot-Bolzen vermessen | [`../02-teile/40-bremsen.md`](../02-teile/40-bremsen.md) |
| 5 | Steuersatz: dauerhafte Lösung statt Loctite | 🟡 | 🔴 offen | Gewindesteigung + Schlüsselweite messen, flache Mutter besorgen | [`../02-teile/20-steuersatz-gabel-vorbau-lenker.md`](../02-teile/20-steuersatz-gabel-vorbau-lenker.md) |
| 5b | 🔴 **Quill-Vorbau-Mindesteinstecktiefe prüfen** | 🔴 | 🔴 offen | Markierung am Vorbau suchen, prüfen ob sie im Schaftrohr liegt | [`../02-teile/20-steuersatz-gabel-vorbau-lenker.md`](../02-teile/20-steuersatz-gabel-vorbau-lenker.md) |
| 6 | Ständer-Winkel zu schräg | 🟢 | 🔴 offen | Kipprichtung klären, Lochabstand messen, Distanzscheiben | [`../02-teile/70-staender-gepaecktraeger.md`](../02-teile/70-staender-gepaecktraeger.md) |
| 7 | Lenker-Ergonomie / Sitzposition | 🟢 | 🟠 beobachten | erst nach 3–5 Fahrten bewerten | [`../02-teile/20-steuersatz-gabel-vorbau-lenker.md`](../02-teile/20-steuersatz-gabel-vorbau-lenker.md) |
| 8 | Neue Kette (Kette ist zu kurz) | 🟡 | 🔴 offen | Big-Big-Test, Kettenstrebenlänge messen, 9-fach-Kette bestellen | [`../02-teile/10-antrieb-schaltung-kette.md`](../02-teile/10-antrieb-schaltung-kette.md) |
| 9 | 🔴 Felgen-Bremsflanken-Verschleiß prüfen | 🔴 | 🔴 offen | Verschleißindikator + Mulden-Tiefe prüfen (v + h) | [`../02-teile/30-laufrad-reifen-nabe.md`](../02-teile/30-laufrad-reifen-nabe.md) |
| 10 | Teile identifizieren + Stammdaten ausfüllen | 🟡 | 🔴 offen | Aufdrucke fotografieren, Messdatenblatt ausfüllen | [`../04-messdaten/messdatenblatt.md`](../04-messdaten/messdatenblatt.md) |
| 11 | Kassette vom Spenderrad lösen (optional) | 🟢 | 🔴 offen | Kettenpeitsche besorgen, dann erneut versuchen | [`../02-teile/10-antrieb-schaltung-kette.md`](../02-teile/10-antrieb-schaltung-kette.md) |
| 12 | Testfahrt + Gesamtcheck | 🟡 | 🔴 offen | [`sicherheitscheck.md`](sicherheitscheck.md) | |

---

## Empfohlene Reihenfolge der Werkstatt-Sessions

Nicht alles auf einmal. Diese Reihenfolge minimiert Umbauten:

### Session 1 – Diagnose & Messen (ca. 60–90 min, kaum Werkzeug nötig)

**Ziel: nichts reparieren, nur herausfinden.** Danach weißt du, was du bestellen musst.

1. Rad vorne ausbauen → Achse in der Hand drehen → **Baustelle 1** eingrenzen
2. Ist das Vorderrad ein Nabendynamo? (klärt evtl. alles)
3. Hinterrad: Kontermutter prüfen, Feder identifizieren → **Baustelle 2**
4. Bremse hinten: Zug aushängen, Binärsuche → **Baustelle 3**
5. Felgen-Bremsflanken prüfen → **Baustelle 9** 🔴
6. Quill-Vorbau-Einstecktiefe prüfen → **Baustelle 5b** 🔴
7. Alle Modellnummern fotografieren + [`Messdatenblatt`](../04-messdaten/messdatenblatt.md) ausfüllen → **Baustelle 10**
8. Konusschlüssel-Größen messen, Gewindesteigung Steuersatz bestimmen

**Output:** ausgefülltes Messdatenblatt + [`Einkaufsliste`](einkaufsliste.md)

### Session 2 – Bestellen (0 min Werkstatt)

Aus der [`Einkaufsliste`](einkaufsliste.md) bestellen. Wartezeit für Session 3 nutzen.

### Session 3 – Lager einstellen (ca. 60 min)

1. Vorderrad-Lager einstellen → **Baustelle 1**
2. Hinterrad-Lager einstellen, Feder ersetzen → **Baustelle 2**
3. Schnellspanner korrekt spannen

### Session 4 – Bremsen (ca. 90 min)

1. Neue Züge + Hüllen hinten → **Baustelle 3**
2. Hebel: Pivot-Bolzen/Federn tauschen oder neue Hebel → **Baustelle 4**
3. Beläge einstellen (Abstand, Toe-in), Zentrierung
4. Probefahrt im Hof

### Session 5 – Steuersatz dauerhaft sichern (ca. 30 min)

1. Flache Mutter montieren + Loctite → **Baustelle 5**
2. Markierung mit Lackstift setzen, Kontrollroutine einrichten

### Session 6 – Neue Kette (ca. 45 min)

1. Länge berechnen, Kette kürzen, montieren → **Baustelle 8**
2. Big-Big-Test wiederholen
3. Schaltung neu justieren

### Session 7 – Kleinkram (ca. 30 min)

1. Ständer-Winkel → **Baustelle 6**
2. Lenker-Ergonomie bewerten → **Baustelle 7**
3. Schutzbleche final prüfen

### Session 8 – Testfahrt

[`Sicherheitscheck`](sicherheitscheck.md) durchgehen, dann längere Probefahrt.

---

## Baustellen-Detail (Arbeitskopie)

### 1. Vorderrad dreht nicht frei 🔴

| Feld | Wert |
|---|---|
| Symptom | Rad stoppt beim Drehen von Hand schnell |
| Lenkkopf als Ursache | ❌ ausgeschlossen (korrekt erkannt) |
| Mögliche Ursachen | Lager zu fest · Schnellspanner zu stark · Nabendynamo (normal!) · Schmutz/alter Fett · Lagerschaden · Reifen/Felge streift · Bremse schleift |
| Diagnose-Datei | [`../04-diagnose/vorderrad-schwergaengig.md`](../04-diagnose/vorderrad-schwergaengig.md) |
| Benötigtes Werkzeug | Konusschlüssel ❓ Größe, zweiter Schlüssel, Fett |
| Ergebnis | ❓ |

### 2. Hinterrad schwerer laufend + verlorene Feder 🔴

| Feld | Wert |
|---|---|
| Symptom | Rad läuft schwerer als vor dem Umbau |
| Bekannte Fehler | Kontermutter zu fest angezogen · **eine kleine Feder verloren** |
| Vermutung | Lager zu stark vorgespannt; Feder = QR-Feder oder Wellenscheibe |
| Diagnose-Datei | [`../04-diagnose/hinterrad-lager-feder.md`](../04-diagnose/hinterrad-lager-feder.md) |
| Benötigtes Werkzeug | Konusschlüssel ❓ Größe, Fett, ggf. Ersatzfeder |
| Ergebnis | ❓ |

### 3. Hintere Bremse kehrt nicht selbstständig zurück 🔴

| Feld | Wert |
|---|---|
| Symptom | Bremse bleibt nach dem Loslassen ganz/teilweise angezogen |
| Besonderheit | Zange, Federn und Zug sind **original** übernommen → Zange vermutlich okay |
| Wahrscheinlichste Ursache | Zug/Hüll-Reibung |
| Diagnose-Datei | [`../04-diagnose/hintere-bremse-kehrt-nicht-zurueck.md`](../04-diagnose/hintere-bremse-kehrt-nicht-zurueck.md) |
| Benötigtes Material | Bremszug 1,5 mm + Bremszug-Hülle 5 mm + Endhülsen |
| Ergebnis | ❓ |

### 4. Bremshebel zu weich, Federn zu schwach 🟡

| Feld | Wert |
|---|---|
| Symptom | Hebel fühlen sich schwammig an, schnappen schwach zurück |
| Bisher versucht | kleine Stellschrauben → bringen nur wenig |
| **Wichtige neue Hypothese** | ⚠️ **falscher Zugweg** (Hebel ≠ Zange) – das wäre durch Federn nicht zu beheben |
| Geplante Lösung | Pivot-Bolzen der guten Hebel umbauen, sonst neue Hebel |
| Detail | [`../02-teile/40-bremsen.md`](../02-teile/40-bremsen.md) Abschnitt 3 |
| Ergebnis | ❓ |

### 5. Steuersatz-Gewinde – dauerhafte Lösung 🟡 (sicherheitsrelevant)

| Feld | Wert |
|---|---|
| Symptom | nur 1–2 Gewindegänge frei → keine Kontermutter möglich |
| Aktuell | Mutter + Loctite 243, regelmäßige Kontrolle |
| Dauerhaft | flache Steuersatz-Mutter (Fachhandel!) oder Gabel mit längerem Schaft |
| 🔴 **Zusatzprüfung** | Quill-Vorbau-Mindesteinstecktiefe (Bruchgefahr!) |
| Detail | [`../02-teile/20-steuersatz-gabel-vorbau-lenker.md`](../02-teile/20-steuersatz-gabel-vorbau-lenker.md) |
| Ergebnis | ❓ |

### 6. Ständer zu stark geneigt 🟢

| Feld | Wert |
|---|---|
| Symptom | Rad kippt fast von selbst |
| Vergleich | alter Ständer war zu aufrecht |
| Lösung | Distanzscheiben unter eine Seite, Längenverstellung, oder KSA-40-Montage |
| Offene Frage | **In welche Richtung kippt das Rad?** (zum Ständer hin / weg) |
| Detail | [`../02-teile/70-staender-gepaecktraeger.md`](../02-teile/70-staender-gepaecktraeger.md) |
| Ergebnis | ❓ |

### 7. Lenker-Gefühl ungewohnt 🟢

| Feld | Wert |
|---|---|
| Symptom | breiterer, geschwungener Lenker → andere Sitzposition/Hebelwege |
| Bewertung | vermutlich Gewöhnung + Einstellsache |
| Plan | 3–5 Fahrten, dann bewerten. Einstellmöglichkeiten ohne Teiletausch nutzen |
| **Zusatz-Aspekt** | ⚠️ die schwarze Gabel hat evtl. eine **geringere Einbauhöhe** → steilerer Lenkwinkel, weniger Nachlauf → nervöseres Lenken. Das ist keine Einstellsache! |
| Detail | [`../02-teile/20-steuersatz-gabel-vorbau-lenker.md`](../02-teile/20-steuersatz-gabel-vorbau-lenker.md) Abschnitt 7 |
| Ergebnis | ❓ |

### 8. Neue Kette 🟡

| Feld | Wert |
|---|---|
| Symptom | Kette durch Reparatur ~½–1 Glied zu kurz |
| Risiko | Big-Big überstreckt das Schaltwerk → Schaltauge/Käfig-Schaden |
| Lösung | 9-fach-Kette, Länge neu berechnen (nicht die alte als Maß nehmen!) |
| Detail | [`../02-teile/10-antrieb-schaltung-kette.md`](../02-teile/10-antrieb-schaltung-kette.md) Abschnitt 3 |
| Ergebnis | ❓ |

### 9. Felgen-Bremsflanken 🔴

| Feld | Wert |
|---|---|
| Symptom | Bremsflanken am weißen Rad abgefahren; Original-Hinterrad ist wieder eingebaut |
| Risiko | Felgendurchbruch unter Bremsdruck (Felgenplatzer) |
| Lösung | Verschleißindikator prüfen, Mulde messen → ggf. Felge/Laufrad tauschen |
| Detail | [`../02-teile/30-laufrad-reifen-nabe.md`](../02-teile/30-laufrad-reifen-nabe.md) Abschnitt 2.3 |
| Ergebnis | ❓ |

### 10. Teile identifizieren & dokumentieren 🟡

Der eigentliche Zweck dieses Repos.

| Teilschritt | Erledigt |
|---|---|
| Hersteller/Modell/Rahmennummer beider Räder ablesen | ☐ |
| Alle Shimano-Aufdrücke fotografieren | ☐ |
| [`Messdatenblatt`](../04-messdaten/messdatenblatt.md) ausfüllen | ☐ |
| Modellnummern in die `02-teile/`-Dateien eintragen | ☐ |
| ❓ TODO-Markierungen löschen, wo Werte eingetragen sind | ☐ |

---

## ✅ Erledigt (Archiv)

| Datum | Was | Notiz |
|---|---|---|
| ❓ | Kettenreparatur mit Fremdschloss | Kette dadurch kürzer → Baustelle 8 |
| ❓ | Gabel- und Steuersatztausch | → Baustelle 5 |
| ❓ | Vorbau/Lenker montiert (winkelverstellbar, Faceplate) | Lenkerwechsel ohne Griffabbau möglich |
| ❓ | Schutzbleche montiert (vorne über Originalpunkte der Gabel, hinten mit Fummelei) | streifenfrei |
| ❓ | Rücklicht-Kabel neu gelötet + verlegt | Flachstecker entfernt |
| ❓ | Licht getestet: Nabendynamo + vorne/hinten funktionieren | |
| ❓ | Original-Hinterrad wieder eingebaut | Kassette ließ sich nicht lösen → Baustelle 11 |
| ❓ | Steuersatz eingestellt | freigängig, kein Spiel |
| ❓ | Kette/Schaltung/Umwerfer funktionieren | |

> Bitte Datumsangaben ergänzen und neue Einträge in [`../06-logbuch/`](../06-logbuch/) anlegen.
