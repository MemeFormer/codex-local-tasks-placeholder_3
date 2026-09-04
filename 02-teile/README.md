# 02 – Teileträger: eine Datei pro Baugruppe

Das ist das **Herzstück** dieses Repos. Jede Baugruppe hat eine eigene Datei mit:

1. **Fachbegriffen** (Deutsch + Englisch + was man im Handel sucht) – damit du weißt, wie
   das Teil heißt, wenn du es beschreiben oder bestellen willst
2. **Ist-Zustand**: was aktuell verbaut ist
3. **Messwerte**: was noch offen ist (`❓ TODO`)
4. **Kompatibilität & Fallstricke**
5. **Ersatzteilbedarf**

| Datei | Baugruppe | Enthält |
|---|---|---|
| [`00-fachbegriffe-glossar.md`](00-fachbegriffe-glossar.md) | **Alle Begriffe DE ↔ EN** | Nachschlagewerk, wenn dir ein Name fehlt |
| [`00-teil-identifizieren.md`](00-teil-identifizieren.md) | **Workflow** | Wie finde ich heraus, was das für ein Teil ist? |
| [`10-antrieb-schaltung-kette.md`](10-antrieb-schaltung-kette.md) | Kurbel, Innenlager, Kette, Kassette, Schaltwerk, Umwerfer, Schalthebel, Pedale | Kettenlänge, Kapazität, 8/9-fach-Kompatibilität |
| [`20-steuersatz-gabel-vorbau-lenker.md`](20-steuersatz-gabel-vorbau-lenker.md) | Gabel, Steuersatz, Vorbau, Lenker, Griffe | 🔴 **Gabel-Situation**: jetzt **NEX (Bergamont)** verbaut, **Original = RST Vogue TNL** · Gewinde-Problem · 🔴 **Quill-Mindesteinstecktiefe** |
| [`30-laufrad-reifen-nabe.md`](30-laufrad-reifen-nabe.md) | Nabe, Freilaufkörper, Speichen, Felge, Felgenband, Reifen, Schlauch, Ventil, Achse | ⚠️ Bremsflanken-Verschleiß, Lager-Einstellung |
| [`40-bremsen.md`](40-bremsen.md) | Bremshebel, Züge, Hüllen, Bremskörper, Federn, Beläge | ✅ #3 erledigt (**Klemmschelle**, nicht Beläge) · 🔴 #5 **Cantistifte zu kurz** · 🟡 #3a Belaglängen |
| [`50-beleuchtung-elektrik.md`](50-beleuchtung-elektrik.md) | Nabendynamo, Scheinwerfer, Rücklicht, Kabel, Flachstecker, Lötverbindungen | ✅ **DH-3N31-NT** identifiziert · ✅ #13 erledigt · 🔴 **nur links einstellen** |
| [`60-schutzbleche.md`](60-schutzbleche.md) | Kotflügel, V-Streben, Schellen, Halter | Montagepunkte, Freigängigkeit |
| [`70-staender-gepaecktraeger.md`](70-staender-gepaecktraeger.md) | Ständer, Aufnahme, Gepäckträger | ⚠️ Winkelkorrektur |
| [`80-rahmen-kleinteile.md`](80-rahmen-kleinteile.md) | Rahmen, Ausfallende, Zuganschläge, Kleinteile, Schrauben | ✅ **STAIGER Daytona Sportline**, Alu 6061, **AWO7230329** · Gewindetabelle · 🔴 **Steuerrohr 20–30 mm länger** |

## Reihenfolge beim Durcharbeiten

Nicht alles auf einmal. Jede Datei hat am Ende eine **Messliste für den nächsten
Werkstattbesuch**.

🔴 **Aktuelle Reihenfolge (Stand 2026-09-05)** – maßgeblich ist
[`../03-todos/offene-baustellen.md`](../03-todos/offene-baustellen.md):

1. **[`20-steuersatz-gabel-vorbau-lenker.md`](20-steuersatz-gabel-vorbau-lenker.md)** – 🔴 **Baustelle #14
   (RST Vogue TNL retten?)** hat Vorrang: ihr Ausgang entscheidet über **#1** (Quill-Einstecktiefe),
   **#5** (Cantistifte) und **#6** (Steuersatz-Gewinde) auf einen Schlag.
2. **[`30-laufrad-reifen-nabe.md`](30-laufrad-reifen-nabe.md)** – 🔴 **#2 Felgen-Bremsflanken**
   (sicherheitsrelevant, die Originalbeläge waren durchgefahren).
3. **[`40-bremsen.md`](40-bremsen.md)** – 🔴 **#5 Bremsarme/Cantistifte** (⛔ **Stifte nicht
   zurückdrehen!**).
4. **[`10-antrieb-schaltung-kette.md`](10-antrieb-schaltung-kette.md)** – 🟡 **#7 Kette**.
5. Der Rest (**50/60/70/80**) – 🟢 niedrig.
