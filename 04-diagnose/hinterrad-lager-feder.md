# 🔬 Diagnose: Hinterrad nicht mehr leichtgängig + verlorene Feder

**Baustelle #2** · Priorität 🔴 · Status: 🟡 Diagnose fehlt

**Symptome:**
1. Hinterrad läuft schwerer als vor dem Umbau
2. Beim Achsenausbau ging **eine kleine Feder verloren** – jetzt ist nur noch **eine Seite** vorhanden
3. Die **flache Mutter auf der Gegenseite wurde zu fest angezogen**; das Lager war offen und
   wurde wieder montiert

**Vermutung:** Lager zu stark vorgespannt (Konus/Kontermutter zu fest) + fehlende Feder
verändert die Vorspannung oder die Dichtung.

---

## Teil 1 – Lager neu einstellen

### Ablauf (Kurzform)

> Volle Anleitung: [`../05-anleitungen/lager-einstellen.md`](../05-anleitungen/lager-einstellen.md)

1. Rad ausbauen, **Schnellspanner komplett entfernen**
2. Auf der **linken Seite** (ohne Kassette) arbeiten – dort ist der Konus verstellbar
3. Kontermutter lösen (Konusschlüssel gegenhalten)
4. Konus **1/8 Umdrehung lösen**
5. Kontermutter wieder anziehen, Konus dabei **gegenhalten**
6. Test: Achse zwischen den Fingern drehen → leicht, kein Rauheitsgefühl, **kein** seitliches Spiel
7. Wenn noch schwergängig → Schritt 4 wiederholen
8. Schnellspanner mit **Handkraft** spannen, erneut testen
9. Wenn es jetzt schwergängig wird → Konus nochmal 1/16 Umdrehung lösen

### ⚠️ Besonderheit beim Hinterrad mit Kassette

- Auf der **Antriebsseite** ist der Freilaufkörper aufgeschraubt; der Konus dort ist
  **werksseitig fest eingestellt** und sollte **nicht** verstellt werden
- Einstellung deshalb **immer links** (gegenüber der Kassette)
- Wenn links der Konus gelöst wird, wandert die ganze Achse minimal → danach **erneut
  auf Spiel prüfen** und ggf. die rechte Kontermutter leicht nachziehen
- **Kassette bleibt montiert** – sie muss für die Lager-Einstellung nicht runter

### Test-Protokoll

| Schritt | Test | Ergebnis |
|---|---|---|
| 1 | Rad eingebaut, drehen – wie viele Umdrehungen? | ❓ ____ |
| 2 | Rad ausgebaut, **ohne** Schnellspanner – Umdrehungen? | ❓ ____ |
| 3 | Rad ausgebaut, **mit** gespanntem Schnellspanner – Umdrehungen? | ❓ ____ |
| 4 | Achse mit Fingern drehen: stramm / rau / leicht? | ❓ |
| 5 | Achse seitlich wackeln: Spiel? | ❓ ja (____ mm) / nein |
| 6 | Nach dem Lösen der Kontermutter um 1/8 Umdrehung: Umdrehungen? | ❓ ____ |
| 7 | Konusschlüssel-Größe links | ❓ ____ mm |
| 8 | Kontermutter-Größe links | ❓ ____ mm |
| 9 | Konusschlüssel-Größe rechts | ❓ ____ mm |
| 10 | Naben-Modellnummer | ❓ |
| 11 | Rauheit bleibt auch nach dem Lösen? → Lagerschaden wahrscheinlich | ❓ |

**Entscheidung:**

| Befund | Bedeutung | Maßnahme |
|---|---|---|
| Nach 1/8 Umdrehung lösen läuft es frei | Konus war zu fest | ✅ fertig, Kontermutter festziehen |
| Bleibt rau/knirscht | Fett verharzt oder Konus/Kugeln eingelaufen | Nabe überholen (Abschnitt unten) |
| Hat Spiel, läuft aber leicht | Konus zu lose | 1/16 Umdrehung anziehen |
| Lässt sich nicht spielfrei **und** leicht einstellen | Lagerschaden (Pitting) | Konen + Kugeln tauschen, ggf. Laufrad |

### Nabe überholen (falls rau)

1. Kassette **muss** runter (Kettenpeitsche + Kassettenabzieher) – nur wenn die Nabe geöffnet wird
2. Fotos von **beiden Seiten** machen, bevor etwas gelöst wird
3. Teile in Reihenfolge auf ein Papier legen: Kontermutter → Konus → Dichtung → Kugeln
4. Kugeln zählen (meist 9 pro Seite in einem Käfig, oder Einzelkugeln)
5. Konus-Lauffläche + Naben-Lauffläche prüfen: Rillen? Matt? Blau?
6. Reinigen (Bremsenreiniger), **neu fetten** (Kugeln ins Fett setzen)
7. Zusammenbau in umgekehrter Reihenfolge, Lager einstellen wie oben

---

## Teil 2 – Die verlorene „kleine Feder“ identifizieren

### Kandidaten

| # | Teil | Aussehen | Wo sitzt es | Funktion | Kritisch? |
|---|---|---|---|---|---|
| 1 | **Schnellspanner-Feder** | konische Spiralfeder, ~10 mm lang, Ø 8–10 mm, verjüngt sich | auf der QR-Stange, zwischen Hebel bzw. Spannmutter und Nabe | zentriert den QR | 🟡 läuft ohne, aber QR sitzt unsauber |
| 2 | **Wellenscheibe** | dünne, **gewellte** Scheibe | zwischen Konus/Kontermutter oder bei Industrielagern | hält Lagervorspannung | 🔴 wichtig |
| 3 | **Sprengring / Sicherungsring** | offener Metallring, rastet in eine Nut ein | am Achsende / an der Nabe | axiale Sicherung | 🔴 wichtig |
| 4 | **Zahnscheibe / Federring** | Scheibe mit Zacken | unter der Kontermutter | Sicherung gegen Lösen | 🟡 durch Loctite ersetzbar |
| 5 | **Kontaktfeder Nabendynamo** | kleine Blechfeder | an der Dynamo-Seite | Stromabnahme | 🔴 Licht fällt aus (aber: hinten kein Dynamo) |
| 6 | Freilauf-Klinke mit Feder | winzige Feder unter den Klinken | im Freilaufkörper | Rückstellung der Klinken | 🔴 aber nur bei geöffneter Nabe relevant |

> 💡 Da das **Hinterrad** betroffen ist und dort **kein Dynamo** sitzt, sind #1 (QR-Feder),
> #2 (Wellenscheibe) und #3 (Sprengring) die wahrscheinlichsten Kandidaten.
> **Am häufigsten verloren geht die Schnellspanner-Feder** – sie springt beim Rausziehen
> der Achse gern weg.

### So grenzt du es ein

| Frage | Antwort | Rückschluss |
|---|---|---|
| Wo genau saß die Feder – auf der Achse oder in der Nabe? | ❓ | auf der Achse → QR-Feder / Wellenscheibe · in der Nabe → Sprengring / Klinke |
| War sie **außen** (sichtbar nach dem Öffnen des QR) oder **innen**? | ❓ | außen → QR-Feder |
| Wie sah sie aus – **konische Spirale**, **gewellte Scheibe** oder **offener Ring**? | ❓ | siehe Tabelle |
| Ist die Nabe symmetrisch aufgebaut? | ❓ | Wenn ja → auf der anderen Seite muss dasselbe Teil sitzen |
| Hat das **Vorderrad** dieselbe Konstruktion? | ❓ | Dann dort nachsehen, wie es aussieht! |
| Hat das **Spenderrad** dieselbe Nabe? | ❓ | Dann dort vergleichen |

### Vorgehen

1. **Foto der intakten Seite** machen (Detail, scharf, gut beleuchtet)
2. Beide Seiten vergleichen – ist die Konstruktion symmetrisch?
3. **Naben-Modellnummer ablesen** → im Shimano-Explosionszeichnungs-PDF nachschlagen
   (Suche: `Shimano [Modell] exploded view` oder `bike.shimano.com` → Service-Informationen)
4. Ersatz: QR-Federn gibt es einzeln (💰 1–3 €) oder als kompletter Schnellspanner (💰 5–12 €)

### Bewertung der Konsequenz

| Wenn es war … | Konsequenz | Handeln |
|---|---|---|
| QR-Feder | Der Schnellspanner ist nicht mehr zentriert; er kann sich beim Spannen verkanten und das Lager drücken → **könnte sogar die Ursache der Schwergängigkeit sein!** | 💰 nachkaufen, sofort |
| Wellenscheibe | Lagervorspannung nicht mehr definiert, Spiel möglich | 🔴 Ersatz besorgen |
| Sprengring | Bauteil kann axial wandern | 🔴 Ersatz besorgen |
| Zahnscheibe | Mutter kann sich lösen | 🟡 Loctite als Ersatz |

> 💡 **Interessante These:** Wenn die verlorene Feder eine **QR-Feder** war und der QR
> deshalb verkantet gespannt wurde, könnte das **allein** schon die Schwergängigkeit erklären –
> zusammen mit der zu festen Mutter. Test: **QR komplett entfernen** und das Rad drehen.
> Läuft es dann frei? Dann liegt es am QR.

---

## 🧪 Zusammengefasstes Test-Protokoll

| # | Test | Ergebnis |
|---|---|---|
| 1 | Rad drehen, eingebaut, mit QR | ❓ ____ Umdrehungen |
| 2 | QR entfernt, Rad drehen | ❓ ____ Umdrehungen |
| 3 | Kontermutter links 1/8 gelöst, Rad drehen | ❓ ____ Umdrehungen |
| 4 | Achse mit Fingern: leicht/rau? | ❓ |
| 5 | Achse seitlich wackeln: Spiel? | ❓ |
| 6 | Konusschlüssel-Größen | ❓ ____ / ____ mm |
| 7 | Naben-Modellnummer | ❓ |
| 8 | Feder identifiziert (was war es?) | ❓ |
| 9 | Vorderrad als Vergleich: gleiche Konstruktion? | ❓ |
| 10 | Felgen-Bremsflanke geprüft? (Baustelle #9) | ❓ |

**Ergebnis:** ____________________________
**Nächste Maßnahme:** ____________________________
**Benötigte Teile:** ____________________________
