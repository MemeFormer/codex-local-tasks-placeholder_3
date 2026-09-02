# 🔬 Diagnose: Hintere Bremse kehrt nicht selbstständig zurück

**Baustelle #3** · Priorität 🔴 · Status: 🟡 Diagnose fehlt

**Symptom:** Nach dem Loslassen des Bremshebels gehen die Bremsbeläge nicht (oder nur langsam)
von der Felge weg. Die Bremse schleift, der Hebel fühlt sich „klebrig“ an.

**Besonderheit:** Zange, Federn **und** Zug wurden **original** übernommen – die Zange war
vorher also vermutlich okay. → **Wahrscheinlichste Ursache: Reibung im Zug/Hüllensystem
durch die neue Verlegung**, oder eine Belag/Felgen-Kante, an der es hakt.

> ⚠️ **Sicherheitsrelevant:** Eine nicht zurückkehrende Bremse wird bei längerer Bergabfahrt
> heiß → Felge erhitzt → Reifen kann platzen, Beläge verglasen. Bis zur Reparatur:
> vorausschauend fahren, keine langen Abfahrten mit schleifender Bremse.

---

## 🧪 Die Binärsuche (in dieser Reihenfolge, 5–10 Minuten)

### Schritt 1 – Zange isolieren

**Zug an der Zange aushängen:** Klemmschraube lösen, Innenzug rausziehen, Hülle aus dem
Zuganschlag/Zughalter nehmen.

```
Jetzt die Bremsarme von Hand zusammendrücken und loslassen:
Schnappen sie KRÄFTIG und KOMPLETT zurück?
   │
   ├── JA  → Zange ist okay. Problem = ZUG oder HÜLLE oder HEBEL  → Schritt 2
   │
   └── NEIN → Problem = ZANGE (Feder / Pivot / Belag)             → Abschnitt B
```

### Schritt 2 – Innenzug aus der Hülle ziehen

```
Innenzug ganz aus der Hülle ziehen.
Zug allein in der Hand: gleichmäßig, glatt, ohne Verdickungen/Rost?
Hülle allein: ein Stück Zugdraht durchschieben – geht es leicht und ohne Ruckeln?
   │
   ├── Zug rau/rostig/ausgefranst      → Zug ersetzen            → Abschnitt C
   ├── Hülle blockiert/ruckelt         → Hülle ersetzen          → Abschnitt C
   └── Beides leicht                   → Problem = HEBEL         → Abschnitt D
```

### Schritt 3 – Hebel prüfen

```
Zug am Hebel eingehängt lassen, Zange ausgehängt.
Hebel drücken und loslassen: schnappt er kräftig und vollständig zurück?
   │
   ├── JA  → Hebel okay. Dann liegt es an der Kombination Zuglänge/Verlegung → Abschnitt C
   └── NEIN → Rückholfeder im Hebel schwach/defekt, Pivot trocken,
              oder die Griffweiten-Einstellschraube steht zu weit rein → Abschnitt D
```

---

## A. Wenn die Zange allein nicht zurückschnappt

| # | Ursache | Test | Lösung |
|---|---|---|---|
| A1 | **Rückholfeder falsch eingehängt** | Die Feder hat ein **kurzes** und ein **langes** Ende. Das kurze Ende muss in die Bohrung des Bremssockels, das lange in den Arm. Falsch herum = keine Rückstellung! | Feder korrekt einsetzen |
| A2 | Feder schwach / ermüdet | Arme von Hand spreizen → wenig Kraft spürbar | Feder in ein anderes Einhängeloch (falls mehrere), oder nachbiegen, oder neu |
| A3 | **Pivot-Bolzen der Zange trocken/rostig** | Zange vom Sockel abschrauben, Bolzen ansehen | Bolzen raus, Rost entfernen, **dünn fetten**, wieder montieren (nicht zu fest!) |
| A4 | Zange zu fest am Bremssockel angezogen | Zange dreht sich schwergängig auf dem Sockel | Schraube lösen, Sockel + Zange reinigen/fetten, mit 6–8 Nm anziehen |
| A5 | **Beläge haken an der Felgenkante** | 🔴 Bei **abgefahrener Bremsflanke** entsteht eine scharfe Kante, an der der Belag hängen bleibt | Belag tiefer setzen / Felge tauschen |
| A6 | Belag sitzt zu nah an der Felge | Abstand < 0,5 mm | auf **1 mm** einstellen |
| A7 | Belag verbogen / Träger ausgeschlagen | Sichtprüfung | Beläge tauschen |
| A8 | Felge hat Seitenschlag | Felge beobachten | zentrieren |
| A9 | Federspannschraube ganz rausgedreht | Schraube am Arm prüfen | beide Arme gleichmäßig **reindrehen** (erhöht Vorspannung) |

**A9 im Detail – Federspannschrauben:**

| Drehrichtung | Effekt |
|---|---|
| **Rein** (im Uhrzeigersinn) | mehr Federvorspannung → Arm geht **weiter weg** von der Felge |
| **Raus** | weniger Vorspannung → Arm geht näher an die Felge |

Beide Seiten **gleichmäßig** einstellen, sonst zieht die Bremse einseitig. Verstellbereich
typisch ±2–3 Umdrehungen. Ist er am Ende → Feder in ein anderes Loch / neue Feder.

---

## B. Wenn Zug oder Hülle das Problem sind (wahrscheinlichster Fall!)

### B1. Ursachen-Ranking

| # | Ursache | Warum bei deinem Umbau wahrscheinlich |
|---|---|---|
| B1 | **Hülle zu lang** → enger Bogen → Reibung | neue Verlegung am weißen Rad, andere Geometrie |
| B2 | **Hülle zu kurz** → straffer Zug → Knick | dito |
| B3 | **Hüllenende verquetscht / nicht entgratet** | beim Neuverlegen geschnitten, Enden nicht gefeilt |
| B4 | **Falsche Hülle**: Schaltzug-Hülle (4 mm, Längsdrähte) statt Bremszug-Hülle (5 mm, Spirale) | Verwechslungsgefahr beim Kauf |
| B5 | Innenzug **rostig / ausgefranst** | alter Zug übernommen |
| B6 | **Keine Endhülsen (Ferrules)** | Druckkraft wird nicht verteilt → Hülle arbeitet |
| B7 | Wasser/Dreck in der Hülle | altes Kabel |
| B8 | Zug hat eine **Verdickung** (aufgequetschte Litze) an der Klemmschraube | Zug wurde schon mal geklemmt |
| B9 | Zug an der Klemmschraube **ausgefranst** | |
| B10 | Hülle scheuert am Rahmen / ist geknickt | neue Verlegung |

### B2. Der Reibungstest

1. Zug aushängen
2. Innenzug aus der Hülle ziehen
3. Ein Stück **neuen** Zug oder einen dünnen Draht durch die Hülle schieben
4. Geht es **ohne spürbaren Widerstand**? Wenn nicht → wo klemmt es? (Hüllenende? Bogen?)
5. Hüllenenden ansehen: **querverquetscht**? **aufgebogene Drähte**? → nacharbeiten

### B3. Lösung: Zug + Hülle neu

> Das ist bei diesem Symptom in ~80 % der Fälle die Lösung. Aufwand: 30–40 min,
> Kosten: 12–20 €.

**Material:**

| Teil | Spec |
|---|---|
| Bremszug-Innenzug | Edelstahl, Ø **1,5 mm** (MTB/V-Brake) oder **1,2 mm** (Rennrad/Canti) ❓ erst klären |
| Bremszug-Hülle | **Spiralgewickelt**, Ø außen **5 mm**, innen 1,8–2,0 mm ⚠️ **keine** Schaltzug-Hülle (4 mm)! |
| Endhülsen (Ferrules) | 5 mm, Metall |
| Zugendhülse (Donut) | für das Zugende an der Klemmschraube |
| Fett | Teflon-/Kabel-Fett, dünn |

**Ablauf:**

1. Alte Hülle ausbauen, **Länge messen** (als Referenz, aber die neue Länge nach der
   Lenkergeometrie bestimmen!)
2. Neue Hülle zuschneiden – **mit Zughüllenschneider** oder einem sehr scharfen
   Seitenschneider
3. **Beide Enden entgraten**: Feile, dann eine Ahle/Nagel in die Öffnung drehen, damit die
   Spiraldrähte nicht nach innen stehen
4. Endhülsen auf beide Enden
5. Innenzug **dünn fetten** (nicht ölen!) und durchziehen
6. Verlegen: **große, weiche Bögen**, in jeder Lenkstellung genug Reserve
7. Am Zuganschlag/Halter einführen
8. An der Zange klemmen: Zug **vorstrecken** (einmal mit 60–70 % Kraft anziehen, dann lösen),
   dann auf **1 mm Belagabstand** spannen und klemmen
9. Zugende kürzen (ca. 3–4 cm über der Klemmschraube), **Donut** aufschieben
   ⚠️ **Niemals** ein ausgefranstes Zugende – immer sauber mit einem Seitenschneider schneiden
10. Beläge einstellen (Abstand 1 mm, Toe-in 0,5–1 mm), Zentrierung über Federspannschrauben
11. **Funktionstest:** Hebel 20× betätigen → muss jedes Mal **vollständig** zurück

### B4. Verlege-Regeln (das ist der Knackpunkt bei Umbauten)

| Regel | Detail |
|---|---|
| **Weiche Bögen, keine Knicke** | Biegeradius ≥ 50 mm |
| **In jeder Lenkstellung testen** | Lenker komplett links und rechts einschlagen – die Hülle darf nie straff werden |
| **Nicht am Rahmen scheuern** | mit Kabelschellen/Tüllen fixieren |
| **Nicht zu viele Bögen** | jeder Bogen = mehr Reibung |
| **Hinter dem Tretlager** | dort nicht zu eng bündeln, Kabel vom Spenderrad waren dort zweigeteilt |
| **Zugrichtung** | Der Zug sollte möglichst **gerade** in die Hülle eintaufen (kein Versatz) |

---

## C. Wenn der Hebel das Problem ist

| # | Ursache | Lösung |
|---|---|---|
| C1 | **Rückholfeder im Hebel zu schwach / ermüdet** | Feder tauschen (vom guten Hebel), oder neue Hebel |
| C2 | **Pivot-Bolzen trocken/rostig** | Bolzen raus, reinigen, dünn fetten |
| C3 | **Griffweiten-Einstellschraube zu weit rein** | Schraube rausdrehen → Hebel weiter vom Lenker, Federweg besser |
| C4 | **Falscher Zugweg** (Hebel ≠ Zange) | 🔴 Hebel gegen passende tauschen – das ist **nicht** reparierbar |
| C5 | Hebelgehäuse ausgeschlagen | neue Hebel |
| C6 | Zug-Klemmung am Hebel verquetscht | Zug neu |

> 💡 **Zusammenhang mit Baustelle #4:** Deine schwarzen Hebel sind „weicher und die Federn
> zu schwach“. Wenn **derselbe Hebel** auch für die Rückstellung der hinteren Bremse
> verantwortlich ist, dann ist Baustelle #3 und #4 **vermutlich dieselbe Ursache**!
> → Prüfe: Ist der hintere Bremshebel einer der schwarzen? Wenn ja: **Hebel tauschen**
> löst evtl. beide Probleme auf einmal.

---

## 🧪 Test-Protokoll

| # | Test | Ergebnis |
|---|---|---|
| 1 | Zange ausgehängt: schnappt sie kräftig zurück? | ❓ ja / nein |
| 2 | Zug allein: glatt, ohne Rost/Ausfransung? | ❓ |
| 3 | Hülle allein: Draht geht leicht durch? | ❓ |
| 4 | Hüllenenden: entgratet, mit Endhülsen? | ❓ |
| 5 | Hülle: 5 mm Bremszug-Hülle (Spirale) oder 4 mm Schaltzug-Hülle? | ❓ |
| 6 | Hüllenlänge: in jeder Lenkstellung weich gebogen? | ❓ |
| 7 | Hebel ausgehängt von der Zange: schnappt er zurück? | ❓ |
| 8 | Ist der hintere Hebel einer der schwarzen (schwachen)? | ❓ |
| 9 | Federspannschrauben: Verstellweg noch vorhanden? | ❓ |
| 10 | Belagabstand eingestellt auf 1 mm? | ❓ |
| 11 | Hakt der Belag an der Felgenkante (abgefahrene Flanke)? | ❓ 🔴 |
| 12 | Rückholfeder der Zange korrekt eingehängt (kurzes Ende im Sockel)? | ❓ |

**Ursache:** ____________________________
**Maßnahme:** ____________________________
**Benötigtes Material:** ____________________________

---

## 🔁 Nach der Reparatur – Abnahmetest

| Test | Soll |
|---|---|
| Hebel 20× schnell betätigen | kehrt jedes Mal **vollständig** zurück |
| Hebelweg bis zum Druckpunkt | max. **1/3–1/2** des Wegs zum Lenker |
| Belagabstand | 1 mm pro Seite |
| Rad dreht frei | kein Schleifgeräusch |
| Bremstest bei Fahrt | hinten blockiert bei kräftigem Zug, Rad hebt nicht ab |
| Lenker komplett einschlagen | Bremse bleibt funktionsfähig, Hülle wird nicht straff |
| Rücklicht-Kabel | nicht eingeklemmt / beschädigt |
