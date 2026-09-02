# 🚲 Bike-Swap – Teile-Datenbank & Werkstatt-Doku

Zwei Räder, ein Frankenstein-Bike, viele offene Punkte. Dieses Repo ist das **Gedächtnis**:
Hier stehen die **korrekten Namen** aller Teile, welche **Maße** noch fehlen, was schon
**gemacht** wurde und was als Nächstes ansteht. Ziel: Nie wieder am Rad stehen und nicht
wissen, wie das Ding heißt oder welche Größe man bestellen muss.

---

## ⚡ Schnelleinstieg – wo steht was?

| Ich will … | Datei |
|---|---|
| Wissen, welche Baustellen offen sind | [`03-todos/offene-baustellen.md`](03-todos/offene-baustellen.md) |
| Ein Teil richtig benennen / identifizieren | [`02-teile/00-fachbegriffe-glossar.md`](02-teile/00-fachbegriffe-glossar.md) |
| Nachschlagen, was an einer Baugruppe verbaut ist | [`02-teile/`](02-teile/) → passende Baugruppe |
| Sehen, was ich kaufen/bestellen muss | [`03-todos/einkaufsliste.md`](03-todos/einkaufsliste.md) |
| Ein Maß am Rad ablesen und eintragen | [`04-messdaten/messdatenblatt.md`](04-messdaten/messdatenblatt.md) |
| Eine konkrete Anleitung (Lager einstellen, Bremse …) | [`05-anleitungen/`](05-anleitungen/) |
| Nachlesen, was ich wann gemacht habe | [`06-logbuch/`](06-logbuch/) |
| Alles auf einmal ausdrucken | [`tools/generate-print-sheet.py`](tools/generate-print-sheet.py) |

---

## 🚴 Die beiden Räder (Arbeitsnamen)

| Arbeitsname | Beschreibung | Rolle | Stammdaten |
|---|---|---|---|
| **Weißes Trekkingbike** | 3×9 (27 Gänge), Shimano, Gewindesteuersatz → jetzt mit schwarzer Gabel | **Hauptbike / Zielrad** | [`01-bikes/weisses-trekkingbike.md`](01-bikes/weisses-trekkingbike.md) |
| **Schwarzes Spenderrad** | 3×8, Metall-Schutzbleche, winkelverstellbarer Vorbau, breiterer Lenker | **Teileträger** | [`01-bikes/schwarzes-spenderrad.md`](01-bikes/schwarzes-spenderrad.md) |

> **TODO ganz am Anfang:** echte Hersteller / Modell / Baujahr / Rahmennummer eintragen
> (steht meist unter dem Tretlagergehäuse eingestanzt). Danach sind viele Maße online
> recherchierbar statt mühsam messbar. Siehe [`01-bikes/README.md`](01-bikes/README.md).

---

## 🔴 Sicherheitsrelevant (bitte zuerst prüfen)

1. **Steuersatz-Gewinde** – oben stehen nur noch 1–2 Gewindegänge über, es gibt aktuell
   **keine echte Kontermutter**, nur Mutter + Loctite. Das ist ein **Provisorium**.
   → [`02-teile/20-steuersatz-gabel-vorbau-lenker.md`](02-teile/20-steuersatz-gabel-vorbau-lenker.md)
2. **Felgen-Bremsflanken** – am weißen Rad waren sie abgefahren; das **Original-Hinterrad
   wurde wieder eingebaut**. Abgefahrene Bremsflanke = Risiko Felgenbruch/Platzer beim Bremsen.
   → [`02-teile/30-laufrad-reifen-nabe.md`](02-teile/30-laufrad-reifen-nabe.md)
3. **Kette ist ~½–1 Glied kürzer** als Soll. Große Gänge vorne + hinten (**Big-Big**) können
   das Schaltwerk überstrecken → **diese Kombination vermeiden**, bis neue Kette da ist.
   → [`02-teile/10-antrieb-schaltung-kette.md`](02-teile/10-antrieb-schaltung-kette.md)
4. **Bremsfunktion hinten**: kehrt nicht selbstständig zurück. Solange das so ist:
   defensive Fahrweise, vorausschauend bremsen.
   → [`05-anleitungen/bremsen-einstellen.md`](05-anleitungen/bremsen-einstellen.md)

---

## 📋 Offene Baustellen (Priorität)

| # | Baustelle | Prio | Diagnose-Status |
|---|---|---|---|
| 1 | Vorderrad dreht nicht frei | 🔴 hoch | Ursache noch nicht eingegrenzt → Schnelltest in [`04-diagnose/vorderrad-schwergaengig.md`](04-diagnose/vorderrad-schwergaengig.md) |
| 2 | Hinterrad schwerer laufend (Lager zu fest + verlorene Feder) | 🔴 hoch | [`04-diagnose/hinterrad-lager-feder.md`](04-diagnose/hinterrad-lager-feder.md) |
| 3 | Hintere Bremse kehrt nicht zurück | 🔴 hoch | [`04-diagnose/hintere-bremse-kehrt-nicht-zurueck.md`](04-diagnose/hintere-bremse-kehrt-nicht-zurueck.md) |
| 4 | Bremshebel zu weich / Federn zu schwach | 🟡 mittel | [`02-teile/40-bremsen.md`](02-teile/40-bremsen.md) |
| 5 | Steuersatz-Gewinde: dauerhafte Lösung statt Loctite-Provisorium | 🟡 mittel (aber sicherheitsrelevant) | [`02-teile/20-steuersatz-gabel-vorbau-lenker.md`](02-teile/20-steuersatz-gabel-vorbau-lenker.md) |
| 6 | Ständer-Winkel zu schräg | 🟢 niedrig | [`02-teile/70-staender-gepaecktraeger.md`](02-teile/70-staender-gepaecktraeger.md) |
| 7 | Lenker-Ergonomie / Sitzposition | 🟢 niedrig – erst nach ein paar Fahrten bewerten | [`02-teile/20-steuersatz-gabel-vorbau-lenker.md`](02-teile/20-steuersatz-gabel-vorbau-lenker.md) |
| 8 | Neue Kette (Provisorium ablösen) | 🟡 mittel | [`02-teile/10-antrieb-schaltung-kette.md`](02-teile/10-antrieb-schaltung-kette.md) |

Vollständige Liste inkl. Zwischenstatus: [`03-todos/offene-baustellen.md`](03-todos/offene-baustellen.md)

---

## ✅ Erledigt (Kurzfassung)

- Kette gerissen → mit altem Kettenschloss repariert, Stift aus Außenlasche gedrückt (Kette dadurch kürzer)
- Schwarze Gabel (Gewindeschaft) in weißen Rahmen umgebaut, inkl. Quill-Vorbau (Innenkeil)
- Steuersatz eingestellt: freigängig, kein axiales Spiel
- Winkelverstellbarer Vorbau + Faceplate montiert → Lenkerwechsel ohne Griffe abziehen möglich
- Metall-Schutzbleche mit V-Streben und integrierter Rücklicht-Kabelführung montiert, streifenfrei
- Rücklicht-Kabel: Flachstecker waren in den Rahmen gerutscht → **neu gelötet**, am weißen Rad verlegt
- Nabendynamo + Vorder-/Rücklicht funktionieren
- Hinterrad: **Kassette ließ sich nicht lösen** → komplettes Original-Hinterrad wieder eingebaut

Details & Datumsangaben: [`06-logbuch/`](06-logbuch/)

---

## 🧭 Arbeitsweise mit diesem Repo

1. **Ans Rad gehen = Messen + Fotografieren.** Nicht nur schrauben. Jedes Mal, wenn du am Rad
   bist, trage offene Werte aus [`04-messdaten/messdatenblatt.md`](04-messdaten/messdatenblatt.md) ein.
2. **Foto-Regel:** jede Baugruppe mindestens 3× fotografieren – Gesamtansicht, Detail,
   **und die Beschriftung/Aufdruck auf dem Teil** (daraus ergibt sich die exakte Bezeichnung).
   Fotos **nicht** ins Repo (siehe `.gitignore`), sondern lokal ablegen und hier nur den
   Dateinamen/Pfad notieren.
3. **Teil identifiziert?** → korrekten Namen + Maße in die passende Datei unter [`02-teile/`](02-teile/) eintragen
   und die `❓ TODO`-Markierung löschen.
4. **Etwas bestellt/verbaut?** → in [`03-todos/einkaufsliste.md`](03-todos/einkaufsliste.md) abhaken und
   einen Logbuch-Eintrag machen ([Vorlage](templates/logbuch-eintrag-template.md)).
5. **Neues Teil/eine neue Baugruppe?** → [Vorlage](templates/teilegruppe-template.md) kopieren.

### Konventionen

- `❓ TODO` = Wert fehlt noch, muss am Rad gemessen/abgelesen werden
- `⚠️` = sicherheitsrelevant oder Provisorium
- `💰` = es wird etwas bestellt werden müssen
- Maße immer in **mm**, Gewinde immer als **Nenndurchmesser × Steigung** (z. B. M10 × 1,0)
- Bei Kaufteilen immer angeben: **Hersteller + Modell + Größe** (z. B. „Shimano HG40 9-fach 11-32“)

---

## 📁 Struktur

```
.
├── README.md                     ← du bist hier
├── 01-bikes/                     Stammdaten der beiden Räder + Vorlage für weitere
├── 02-teile/                     Teileträger: eine Datei pro Baugruppe (mit Fachbegriffen)
├── 03-todos/                     offene Baustellen, Einkaufsliste, Werkzeug & Material
├── 04-diagnose/                  Fehlersuche: Symptom → Test → Ursache → Maßnahme
├── 04-messdaten/                 Messdatenblatt: alles, was noch am Rad abgelesen werden muss
├── 05-anleitungen/               Schritt-für-Schritt-Anleitungen + Referenzwerte
├── 06-logbuch/                   was wurde wann gemacht
├── templates/                    Vorlagen (Baugruppe, Messung, Logbuch)
└── tools/                        generate-print-sheet.py (alles in eine Druckdatei)
```
