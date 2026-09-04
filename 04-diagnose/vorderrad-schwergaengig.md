# 🔬 Diagnose: Vorderrad dreht nicht frei

**Baustelle #13** · Priorität 🟢 · Status: ✅ **ERLEDIGT**

> ✅ **GELÖST (2026-09-04):** *„…läuft jetzt auch die Achse mit der Dynamo-Nabe mehrere
> Umdrehungen nach, wenn es frei hängt, ohne dass da gleich das Rad stehen bleibt nach
> wenigen Umdrehungen."*
>
> | | |
> |---|---|
> | **Symptom vorher** | Rad stand nach 1–2 Umdrehungen |
> | **Zustand jetzt** | ✅ **mehrere Umdrehungen** frei hängend |
> | **Ursache** | Kombination aus **Nabendynamo-Rollwiderstand** (normal) + **zu strammer Lagervorspannung** |
> | **Status** | ✅ erledigt · 🟢 nur noch **Beobachtung**: bei nächster Gelegenheit Spiel prüfen |
>
> 💡 **Hinweis:** Dass ein Nabendynamo-Rad **mehrere** Umdrehungen nachläuft, ist ein gutes
> Zeichen – die Lagervorspannung stimmt jetzt. Ein Nabendynamo-Rad läuft **nie** so lange wie
> ein normales Nabenlager (das Magnet-Rasten bremst immer), aber „mehrere Umdrehungen" ist
> der **Sollbereich**.
>
> Die Anleitung unten bleibt als **Referenz**, falls das Rad je wieder schwergängig wird.

**Symptom (historisch):** Das Vorderrad dreht beim Anstoßen nur kurz weiter / ist schwergängig.
**Bereits ausgeschlossen:** Lenkkopf / Steuersatz (korrekt erkannt – der beeinflusst die
Radrotation nicht).

> ✅ **GEKLÄRT: Das Vorderrad ist ein Nabendynamo – Shimano DH-3N31-NT, 6 V / 3 W.**
> **Damit ist dieses „Problem“ mit hoher Wahrscheinlichkeit KEIN Defekt.**
> Ein Nabendynamo dreht von Hand konstruktionsbedingt nur **1–2 Umdrehungen** weiter.
> Das ist völlig normal und kostet auf der Straße nur ca. **1–3 W** Rollwiderstand –
> messtechnisch kaum nachweisbar. **Ein Nabendynamo-Rad dreht von Hand nie „ewig".**
>
> ✅ **ABGEHAKT:** Shimano-Nabendynamos sind ab Werk fast immer **zu stramm eingestellt**,
> und das kann man **nicht erfühlen**, weil das magnetische Rasten die Lager-Rauheit
> überdeckt. **Bei dir ist das inzwischen erledigt** – das Rad läuft mehrere Umdrehungen nach.
> Die Methode steht unten als **Referenz**, falls es wiederkommt.
> → Siehe Abschnitt „Nabendynamo korrekt einstellen (DH-3N31)".
> **Das kostet 0 € und ist die wahrscheinlichste Ursache für „dreht schwer".**
>
> **Priorität deshalb von 🔴 auf 🟢 herabgestuft.** Es bleibt ein kurzer Verifikationstest
> (unten), damit kein echter Lagerschaden übersehen wird.

---

## 🎯 Der Verifikationstest (5 Minuten) – Nabendynamo von echtem Defekt unterscheiden

```
Rad komplett ausbauen (Schnellspanner öffnen + entfernen)
Achse in der Hand halten, Rad drehen
                    │
   ┌────────────────┴─────────────────┐
   │                                  │
Dreht es in der Hand              Dreht es auch in der Hand
EWIG (5+ Umdrehungen)?            nur KURZ (1–2 Umdrehungen)?
   │                                  │
   ▼                                  ▼
Das Rad ist okay.                 Problem = LAGER oder
Problem = etwas KLEMMT            Nabendynamo oder
am Rad/Gabel:                     Bremsanlage selbst
- Bremse
- Schutzblech
- Reifen
- Gabel (Rad sitzt schief)
```

### 🔴 Nabendynamo korrekt einstellen (DH-3N31) – andere Methode als bei normalen Naben!

Praxis-Befund zu Shimano-Nabendynamos:

> Die Lager sind ab Werk praktisch immer **zu stramm**. Bei einem neuen Dynamo muss man den
> linken Konus oft um bis zu **eine halbe Umdrehung** lösen, bevor es richtig läuft.
> **Und man kann es nicht erfühlen**, weil das magnetische Rasten die Wahrnehmung der
> Lager-Rauheit überdeckt.

| Regel | Detail |
|---|---|
| 🔴 **Nur LINKS einstellen** | Seite **ohne** Kabelanschluss. Die Dynamo-Seite **niemals öffnen** – die Kabel sind extrem empfindlich und brechen nach wenigen Biegungen |
| 🔴 **Nicht nach Gefühl gehen** | Das Magnet-Rasten täuscht. **Nur nach Spiel beurteilen** |
| 🎯 **Ziel** | **Minimales Spiel ohne Schnellspanner, das beim Spannen des Schnellspanners gerade eben verschwindet** |
| Werkzeuge | 2× Konusschlüssel ❓ Größe messen (Shimano typisch **13/15 mm** oder **15/17 mm**), Fett |
| 💡 Fett nachfüllen ohne Zerlegen | Linken Konus lösen, Achse nach **rechts** drücken, mit einer Spritze Fett durch den Dichtungsspalt auf der Dynamo-Seite pressen |
| Rotor ausbauen (nur bei echter Überholung) | Ein **Kassetten-Lockring-Werkzeug** passt oft auf die Mutter des Front-Rotors |
| ⚠️ Rechte Seite | Konus dort **nicht** verdrehen, sonst fallen die Kugeln heraus und der Dynamo-Innenteil wird beschädigt |

**Ablauf:**

1. Schnellspanner **komplett entfernen**
2. Links: Kontermutter lösen (Konus gegenhalten)
3. Konus lösen, bis **leichtes Spiel** spürbar ist
4. Konus soweit anziehen, dass **gerade noch minimales Spiel** bleibt
5. Kontermutter anziehen, Konus dabei gegenhalten
6. Schnellspanner mit **Handkraft** spannen → jetzt muss das Spiel **gerade eben** weg sein
7. Falls danach zu stramm: Konus **1/8 Umdrehung** lösen, erneut prüfen
8. Kontermutter final anziehen, Spiel bleibt unter Schnellspanner-Spannung = 0

| Konus-Schlüsselweite | Wert |
|---|---|
| links (Einstellseite) | ❓ ____ mm |
| Kontermutter | ❓ ____ mm |

---

### ✅ So trennst du „normaler Dynamo-Widerstand“ von „echtem Lagerschaden“

| # | Test | Normal beim Nabendynamo | 🔴 Echter Defekt |
|---|---|---|---|
| 1 | Rad ausbauen, **Kabel am Dynamo abziehen**, Achse in der Hand drehen | 2–4 Umdrehungen, gleichmäßig | < 1 Umdrehung, oder rau/knirschend |
| 2 | Achse mit zwei Fingern **seitlich wackeln** | **kein** Spiel | Spiel spürbar |
| 3 | Achse drehen und **fühlen** | ⚠️ **beim Nabendynamo NICHT aussagekräftig** – das Magnet-Rasten überdeckt Lager-Rauheit. **Nur nach Spiel gehen!** | – |
| 4 | Schnellspanner **entfernen**, erneut drehen | kaum Unterschied | wird deutlich leichter → Lager war geklemmt |
| 5 | Rad eingebaut, Bremse ausgehängt, drehen | kaum Unterschied zum ausgebauten Zustand | deutlich schlechter → es klemmt etwas (Bremse/Schutzblech/Reifen) |
| 6 | **Licht einschalten** und bei Fahrt vergleichen | Widerstand minimal höher | – |
| 7 | Dynamo-Gehäuse: warm geworden nach 10 min Fahrt? | handwarm = normal | heiß = Kurzschluss im Lichtsystem oder Lagerschaden |

**Wichtig:** Der charakteristische Nabendynamo-Widerstand fühlt sich **„samtig-rastend“** an
(die Magnete ziehen an den Spulen) – das ist etwas anderes als das **„raue, sandige“**
Gefühl eines eingelaufenen Konuslagers.

**Faustregel:** Wenn das Rad **im Fahrbetrieb** frei rollt und kein Schleifgeräusch macht,
ist alles in Ordnung. Der Hand-Drehtest ist bei einem Nabendynamo **kein** aussagekräftiges
Kriterium für den Rollwiderstand.

---

## 🔍 Ursachen-Checkliste (in Prüf-Reihenfolge)

### A. Rad dreht in der Hand frei, aber eingebaut nicht → es klemmt etwas

| # | Ursache | Test | Lösung |
|---|---|---|---|
| A1 | **Bremsbeläge schleifen** | Bremse komplett aushängen (Zug lösen), Rad drehen | Beläge auf 1 mm Abstand einstellen, Zentrierung korrigieren |
| A2 | **Reifen streift am Schutzblech** | Sichtprüfung bei drehendem Rad, engste Stelle suchen | Schutzblech nachsetzen (Distanzscheiben), Streben verstellen |
| A3 | **Reifen streift an der Gabel** | dito | – |
| A4 | **Rad sitzt schief in der Gabel** | Abstand Felge → linke/rechte Gabelscheide messen | Rad neu zentriert einspannen |
| A5 | **Schnellspanner zu stark angezogen** | QR lösen, Rad drehen, dann mit **normaler Handkraft** wieder spannen | QR richtig einstellen (siehe C3) |
| A6 | **Seitenschlag der Felge** | Felge beobachten / Kabelbinder als Zeiger an die Gabel | zentrieren |
| A7 | **Speiche berührt Schutzblech/Bremse** | Sichtprüfung | Speiche richten |

### B. Rad dreht auch in der Hand schwer → Lager

| # | Ursache | Test | Lösung |
|---|---|---|---|
| B1 | **Konus zu fest angezogen** | Achse mit den Fingern drehen: fühlt sich „stramm“/rau an, kein Spiel | Konus lösen, neu einstellen ([Anleitung](../05-anleitungen/lager-einstellen.md)) |
| B2 | **Lager trocken / altes verharztes Fett** | Nabe öffnen: Fett schwarz, klumpig, trocken? | Nabe reinigen, neu fetten, Kugeln prüfen |
| B3 | **Konus eingelaufen (Pitting)** | Nabe öffnen: matte Rille / Druckstellen auf der Konus-Lauffläche | Konus + Kugeln tauschen (nabenspezifisch!) |
| B4 | **Kugeln beschädigt** | Kugeln ansehen: matt, blau angelaufen, unrund | Kugeln tauschen (ganzen Satz, nie einzeln mischen) |
| B5 | **Lagerschale im Nabenkörper eingelaufen** | Lauffläche im Nabenkörper prüfen | 🔴 Nabe/Laufrad tauschen |
| B6 | **Achse verbogen** | Achse ausbauen, auf Glasplatte rollen | Achse tauschen |
| B7 | **Dichtung schleift** | Staubschutz/Kontaktdichtung prüfen | dünn fetten |
| B8 | **Nabendynamo** (Normales Verhalten!) | Kabel abziehen, erneut drehen | ✅ kein Defekt |

### C. Sonderfall Schnellspanner

| # | Punkt | richtig |
|---|---|---|
| C1 | Konuslager wird **ohne** QR eingestellt | QR komplett entfernen, einstellen, dann QR rein |
| C2 | QR-Spannkraft | mit **Handkraft** schließen – der Hebel hinterlässt einen Abdruck in der Handfläche, aber kein Kraftakt, keine Zange |
| C3 | QR-Federn | **schmale Seite zeigt nach innen** (zur Nabe). Falsch herum = verkantet und drückt das Lager zusammen |
| C4 | QR zu fest | → Lager wird vorgespannt → schwergängig + Lagerschaden |

---

## 🧪 Test-Protokoll zum Ausfüllen

| Schritt | Test | Ergebnis |
|---|---|---|
| 1 | Ist das Vorderrad ein Nabendynamo? | ✅ **ja – geklärt** |
| 2 | Dreht es mit abgezogenem Kabel 2–4 Umdrehungen? | ❓ |
| 2b | Fühlt sich der Widerstand „samtig-rastend“ (normal) oder „rau/sandig“ (defekt) an? | ❓ |
| 3 | Rad eingebaut drehen – wie viele Umdrehungen? | ❓ ____ |
| 4 | Rad ausgebaut, Achse in der Hand – wie viele Umdrehungen? | ❓ ____ |
| 5 | Mit gelöstem Schnellspanner – wie viele Umdrehungen? | ❓ ____ |
| 6 | Mit komplett ausgehängter Bremse – wie viele? | ❓ ____ |
| 7 | Ohne Schutzblech – wie viele? | ❓ ____ |
| 8 | Achse mit Fingern drehen: stramm / rau / leicht? | ❓ |
| 9 | Achse seitlich wackeln: Spiel? | ❓ ja (____ mm) / nein |
| 10 | Konusschlüssel-Größe gemessen | ❓ ____ mm |
| 11 | Kontermutter-Größe gemessen | ❓ ____ mm |
| 12 | Naben-Modellnummer | ❓ |

**Ergebnis der Eingrenzung:** ____________________________

---

## 🛠️ Maßnahme je nach Ergebnis

| Ergebnis | Maßnahme | Anleitung |
|---|---|---|
| Nur Rollwiderstand durch Magnete | nichts tun, normal | – |
| 🔴 **Lagervorspannung zu fest** (wahrscheinlich!) | 🔴 **nur links** einstellen; Ziel: Spiel verschwindet erst beim Spannen des Schnellspanners | Abschnitt „Nabendynamo korrekt einstellen (DH-3N31)" |
| Bremse schleift | Beläge einstellen, zentrieren | [`../05-anleitungen/bremsen-einstellen.md`](../05-anleitungen/bremsen-einstellen.md) |
| Schutzblech streift | Streben verstellen, Distanzscheiben | [`../02-teile/60-schutzbleche.md`](../02-teile/60-schutzbleche.md) |
| QR zu fest | QR korrekt spannen | [`../05-anleitungen/lager-einstellen.md`](../05-anleitungen/lager-einstellen.md) |
| Konus zu fest | Lager neu einstellen | [`../05-anleitungen/lager-einstellen.md`](../05-anleitungen/lager-einstellen.md) |
| Fett verharzt / Lagerschaden | Nabe überholen, ggf. Konen + Kugeln neu | [`../05-anleitungen/lager-einstellen.md`](../05-anleitungen/lager-einstellen.md) Abschnitt 4 |

---

## 💰 Falls Ersatz nötig wird

| Teil | Spec | Preis |
|---|---|---|
| Konen | ❓ nabenspezifisch | 3–6 €/Stück |
| Kugeln | ❓ 1/4" (6,35 mm) typisch Nabe | 2–4 €/Satz |
| Komplettes Vorderrad | ETRTO + Speichenzahl + **Nabendynamo ja/nein** + Einbaubreite 100 mm | 40–120 € |
| Fett | Shimano Premium Grease | 6–10 € |
