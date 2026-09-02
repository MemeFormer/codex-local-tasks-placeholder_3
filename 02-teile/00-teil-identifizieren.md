# 🔍 Ein Teil richtig identifizieren und benennen

Der Grund, warum du bisher immer ans Rad gehen musstest: Es gab keinen Ort, an dem die
Information **einmal** erfasst und dann **wiedergefunden** wird. Dieser Workflow ändert das.

## Der 5-Schritte-Ablauf

### 1. Aufdruck suchen (bringt in 80 % der Fälle die exakte Antwort)

Shimano-Teile sind fast immer **graviert oder geprägt**. Typische Stellen:

| Teil | Wo steht die Modellnummer? |
|---|---|
| Schaltwerk | Innenseite des Käfigs, Rückseite des Parallelogramms, unter der Leitrolle |
| Umwerfer | Innenseite des Klemmrings / auf dem Leitblech |
| Schalthebel | Unterseite des Gehäuses, oft unter dem Gummi |
| Kurbel | **Innenseite** des Kurbelarms (Rad muss ausgebaut / Kurbel gedreht werden) |
| Kassette | Auf dem größten Ritzel oder auf dem Freilaufkörper-Aufdruck |
| Nabe | Auf der Nabenhülse zwischen den Flanschen, oder unter dem Schnellspanner |
| Felge | Aufkleber an der Flanke, **oder** Prägung im Felgenbett (Reifen runter!) |
| Bremskörper | Rückseite / Innenseite des Arms, unter dem Belag |
| Bremshebel | Unterseite des Hebels, Innenseite des Gehäuses |
| Vorbau | Unterseite, oder **am Einsteckschaft nach dem Ausbau** (Ø eingestanzt) |
| Lenker | In der Mitte, neben der Klemmung (Aufdruck + Klemm-Ø + ggf. Biegung) |
| Sattelstütze | **Unter der Stütze**, nach dem Ausbau (z. B. „27.2“) |
| Steuersatz | Selten beschriftet → messen |
| Dynamo | Auf der Gehäuseseite (z. B. „DH-3N31“) |
| Reifen | Auf der Flanke: ETRTO („37-622“) + Hersteller + Modell |
| Pedale | Auf der Innenseite / Rückseite, Gewindegröße „9/16" |

**Format der Modellnummer:** Shimano = `XX-NNNN` (z. B. `RD-M410`, `CS-HG50`, `ST-EF51`,
`FC-M371`, `FH-RM30`). Andere Hersteller ähnlich. Mit dieser Nummer findet man Datenblatt,
Ersatzteilnummern, Kompatibilität und Preis.

### 2. Foto machen – immer diese drei

1. **Übersicht**: Teil im verbauten Zustand, mit Umgebung (damit man die Montageposition sieht)
2. **Detail**: Teil allein, scharf, gut beleuchtet
3. **Aufdruck**: Makro auf die Gravur – ruhig mit Taschenlampe seitlich anleuchten, dann
   werden Prägeschriften sichtbar

Zusätzlich bei **Lagern und Verschraubungen**: Foto **vor** dem Zerlegen, damit die Reihenfolge
der Scheiben/Hülsen/Federn erhalten bleibt. Und: Teile in der ausgebauten Reihenfolge auf ein
Blatt Papier legen und fotografieren („Exploded View“).

### 3. Messen – die vier Standardmessungen

| Was | Wie | Werkzeug |
|---|---|---|
| **Durchmesser außen** | Messschieber, senkrecht ansetzen | Messschieber |
| **Durchmesser innen** | Messschieber-Innenbacken | Messschieber |
| **Länge** | Zollstock reicht | Zollstock |
| **Gewinde** | Durchmesser messen + **Mutter aus dem Baumarkt testen** | Messschieber + Vergleichsmuttern |

Ohne Messschieber: **Papierstreifen-Trick**. Streifen einmal stramm um das Teil legen,
Markierung setzen, Länge messen, ÷ 3,1416 = Außendurchmesser. Genauigkeit ±0,3 mm.

Typische Fahrrad-Durchmesser zum Wiedererkennen:

| Maß | Was es ist |
|---|---|
| 22,2 mm | Innen-Ø 1"-Gabelschaft (für Quill-Vorbau 22,2) |
| 25,4 mm | Außen-Ø 1"-Gabelschaft **oder** Lenkerklemmung Standard |
| 28,6 mm | Außen-Ø 1⅛"-Gabelschaft |
| 26,0 / 25,4 mm | Quill-Vorbau-Einsteckteil für 1⅛" / 1" |
| 31,8 mm | Lenkerklemmung Oversize |
| 25,4 / 26,0 / 31,8 mm | Lenkerklemmungen |
| 9 mm | Schnellspanner-Achse vorne |
| 10 mm | Schnellspanner-Achse hinten |
| 5 mm | Bremszug-Ø Nabe / Standard-Außenzug 5 mm |
| 4 mm | Schaltzug-Hülle |
| 1,2 mm | Bremszug-Innendurchmesser (Stärke) |
| 1,1–1,2 mm | Schaltzug-Stärke |
| 27,2 / 28,6 / 30,9 / 31,6 mm | gängige Sattelstützen-Ø |
| 34,9 / 31,8 / 28,6 mm | Umwerfer-Schellen-Ø |
| 6,3 × 0,8 mm | Flachstecker Standardgröße |

### 4. Eintragen

In die passende Datei unter [`02-teile/`](.) und zusätzlich ins
[`Messdatenblatt`](../04-messdaten/messdatenblatt.md). Dabei:

- Modellnummer **exakt** abschreiben (auch das `-I` oder `-A` am Ende kann wichtig sein)
- Zähnezahlen zählen (bei Kassette: größtes und kleinstes Ritzel ablesen, meist aufgeprägt)
- Zustand in Worten: `gut` / `brauchbar` / `verschlissen` / `defekt`

### 5. Benennen nach Schema

Damit die Einträge später suchbar sind, immer diese Form:

```
[Hersteller] [Modell] [Baugruppe] – [Größe/Specs] – [Zustand]
Beispiel: Shimano CS-HG50 Kassette 9-fach 11-32 Zähne – gut
Beispiel: no-name Quill-Vorbau winkelverstellbar Schaft 22,2 mm Klemmung 25,4 mm – gut
```

---

## Wenn sich partout nichts ablesen lässt

Dann hilft **Ausschluss** über die Geometrie:

| Frage | Antwort → Rückschluss |
|---|---|
| Wie viele Ritzel hinten? | 8 → 8-fach, 9 → 9-fach … bestimmt Kette, Schalthebel, Kassette |
| Zähnezahl größtes Ritzel? | bestimmt Schaltwerk-Kapazität (Käfiglänge: kurz/mittel/lang) |
| Wie viele Kettenblätter? | 3 = Trekking/MTB, 2 = Rennrad/Gravel, 1 = Singlespeed |
| Bremszug geht **direkt** an den Bremsarm (kein Mittelzug)? | → **V-Brake** |
| Bremszug geht über einen **Mittelzug** zwischen den Armen? | → Cantilever |
| Bremse hängt an **einem zentralen Bolzen** über dem Reifen? | → Seitenzugbremse (Rennrad) |
| Hebel hat lange Arme, Zugweg groß? | → V-Brake-Hebel (long pull) |
| Hebel kurz, wenig Zugweg? | → Rennrad-/Canti-Hebel (short pull) |
| Nabe mit Kabelanschluss? | → Nabendynamo |
| Gabelschaft hat außen Gewinde? | → Gewindesteuersatz (1" oder 1⅛") |
| Gabelschaft glatt, Vorbau klemmt außen? | → Ahead |
| Zahnkranz mit **großer Mutter** (12-Spline) in der Mitte befestigt? | → **Kassette** |
| Zahnkranz, der **als Ganzes aufgeschraubt** ist (kleinste Ritzel = Kontermutter)? | → **Schraubkranz / Freewheel** |

### ⚠️ Häufige Verwechslungen (die wirklich teuer oder gefährlich werden)

| Verwechslung | Folge |
|---|---|
| **Kassette** vs. **Schraubkranz (Freewheel)** | falsches Werkzeug gekauft, Kassette lässt sich „nicht lösen“ |
| **Schnellspanner (QR)** vs. **Steckachse (thru axle)** | völlig andere Achssysteme, nicht kompatibel |
| **V-Brake-Hebel** vs. **Rennrad-Hebel** | falscher Zugweg → Bremse blockiert oder zieht nicht |
| **1" vs. 1⅛" Gewindesteuersatz** | Gabel/Vorbau passen nicht |
| **Quill-Vorbau** vs. **Ahead-Vorbau** | grundverschiedene Systeme |
| **BSA** vs. **italienisches** Tretlagergewinde | Innenlager zerstört beim Einschrauben (ital.: 36 × 24 tpi, **Rechtsgewinde links!**) |
| **Sclaverand** vs. **Schrader**-Felgenbohrung | falscher Schlauch (6,5 mm vs. 8,5 mm Bohrung) |
| **Bremszug-Hülle** (Spirale) vs. **Schaltzug-Hülle** (Längsdrähte) | Schaltzug-Hülle hält Bremskräften nicht stand → Bruch |
| **Loctite blau (243)** vs. **rot (270)** | rot ist nur mit Hitze lösbar |
