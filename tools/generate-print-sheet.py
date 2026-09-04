#!/usr/bin/env python3
"""
Erzeugt eine einzige Markdown-Datei aus allen Doku-Dateien dieses Repos,
zum Ausdrucken (oder zum Umwandeln in PDF, z. B. mit pandoc).

Benutzung:
    python3 tools/generate-print-sheet.py
    python3 tools/generate-print-sheet.py -o druck/ALLES.md
    python3 tools/generate-print-sheet.py --nur 03-todos,04-diagnose

Danach z. B. mit pandoc:
    pandoc PRINT-ALLES.md -o PRINT-ALLES.pdf --pdf-engine=xelatex -V geometry:margin=15mm

Es werden bewusst KEINE externen Python-Pakete benötigt.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# Reihenfolge der Ausgabe (Ordner + Dateien). Was nicht aufgelistet ist, wird
# über die Glob-Muster weiter unten eingesammelt.
ORDNUNG = [
    "README.md",
    "01-bikes/README.md",
    "01-bikes/weisses-trekkingbike.md",
    "01-bikes/schwarzes-spenderrad.md",
    "02-teile/README.md",
    "02-teile/00-fachbegriffe-glossar.md",
    "02-teile/00-teil-identifizieren.md",
    "02-teile/10-antrieb-schaltung-kette.md",
    "02-teile/20-steuersatz-gabel-vorbau-lenker.md",
    "02-teile/30-laufrad-reifen-nabe.md",
    "02-teile/40-bremsen.md",
    "02-teile/50-beleuchtung-elektrik.md",
    "02-teile/60-schutzbleche.md",
    "02-teile/70-staender-gepaecktraeger.md",
    "02-teile/80-rahmen-kleinteile.md",
    "03-todos/offene-baustellen.md",
    "03-todos/einkaufsliste.md",
    "03-todos/werkzeug-und-material.md",
    "03-todos/sicherheitscheck.md",
    "04-diagnose/README.md",
    "04-diagnose/rst-vogue-tnl-federgabel.md",
    "04-diagnose/vorderrad-schwergaengig.md",
    "04-diagnose/hinterrad-lager-feder.md",
    "04-diagnose/hintere-bremse-kehrt-nicht-zurueck.md",
    "04-diagnose/vordere-bremsarme-sockel.md",
    "04-messdaten/messdatenblatt.md",
    "05-anleitungen/README.md",
    "05-anleitungen/lager-einstellen.md",
    "05-anleitungen/bremsen-einstellen.md",
    "05-anleitungen/steuersatz-einstellen.md",
    "05-anleitungen/referenzwerte.md",
    "06-logbuch/README.md",
    "06-logbuch/2026-09-02-bestandsaufnahme.md",
    "06-logbuch/2026-09-03-rueckfrage-korrekturen.md",
    "06-logbuch/2026-09-04-komponenten-entschluesselt.md",
    "06-logbuch/2026-09-05-korrektur-runde.md",
]

AUSGESCHLOSSEN = {"templates", "tools", "fotos", ".git", ".arena"}

# generierte Ausgaben (werden gitignored und duerfen nicht in sich selbst landen)
GENERIERTE_AUSGABEN = {"print-alles.md", "werkstatt-zettel.md"}

LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
CODEBLOCK_RE = re.compile(r"^```")


def sammle_dateien(nur: list[str] | None) -> list[Path]:
    """Dateien in der gewünschten Reihenfolge sammeln."""
    dateien: list[Path] = []
    gesehen: set[Path] = set()

    def hinzufuegen(pfad: Path) -> None:
        if pfad.exists() and pfad.is_file() and pfad not in gesehen:
            if nur and not any(segment in str(pfad.relative_to(REPO)) for segment in nur):
                return
            gesehen.add(pfad)
            dateien.append(pfad)

    for rel in ORDNUNG:
        hinzufuegen(REPO / rel)

    # alles Weitere, das nicht ausgeschlossen ist (z. B. neue Logbuch-Einträge)
    for pfad in sorted(REPO.rglob("*.md")):
        rel = pfad.relative_to(REPO)
        if rel.parts and rel.parts[0] in AUSGESCHLOSSEN:
            continue
        # generierte Druckausgaben nicht in sich selbst aufnehmen
        if pfad.name.lower() in GENERIERTE_AUSGABEN:
            continue
        hinzufuegen(pfad)

    return dateien


def bereinige(text: str) -> str:
    """Links in reinen Text umwandeln, Überschriften herunterstufen."""
    zeilen = text.splitlines()
    ausgabe: list[str] = []
    in_code = False

    for zeile in zeilen:
        if CODEBLOCK_RE.match(zeile.strip()):
            in_code = not in_code
            ausgabe.append(zeile)
            continue

        if not in_code:
            # [Text](pfad.md) -> Text  ·  [Text](http…) -> Text (URL)
            def ersetze(m: re.Match[str]) -> str:
                label, ziel = m.group(1), m.group(2)
                if ziel.startswith(("http://", "https://")):
                    return f"{label} ({ziel})"
                return label

            zeile = LINK_RE.sub(ersetze, zeile)
            # Überschriften um eine Ebene herunterstufen (# -> ##), max. 6
            m = re.match(r"^(#{1,5})\s", zeile)
            if m:
                zeile = "#" + zeile

        ausgabe.append(zeile)

    return "\n".join(ausgabe).strip()


def baue_ausgabe(dateien: list[Path]) -> str:
    heute = dt.date.today().isoformat()
    teile: list[str] = []

    teile.append(f"# Bike-Swap – Gesamtdokument\n")
    teile.append(f"Erzeugt am {heute} mit `tools/generate-print-sheet.py`\n")
    teile.append(f"Umfang: {len(dateien)} Dateien\n")

    teile.append("\n---\n\n## Inhalt\n")
    for i, pfad in enumerate(dateien, start=1):
        teile.append(f"{i}. `{pfad.relative_to(REPO)}`")
    teile.append("\n")

    for i, pfad in enumerate(dateien, start=1):
        rel = pfad.relative_to(REPO)
        inhalt = pfad.read_text(encoding="utf-8")
        teile.append(f"\n\n\\newpage\n\n---\n\n# Teil {i} – {rel}\n")
        teile.append(bereinige(inhalt))
        teile.append("\n")

    return "\n".join(teile)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-o",
        "--output",
        default=str(REPO / "PRINT-ALLES.md"),
        help="Zieldatei (Standard: PRINT-ALLES.md im Repo-Root)",
    )
    parser.add_argument(
        "--nur",
        default=None,
        help="Nur Dateien aus diesen Ordnern/Pfaden, komma-separiert (z. B. '03-todos,04-diagnose')",
    )
    parser.add_argument(
        "--liste",
        action="store_true",
        help="Nur die gefundenen Dateien auflisten, nichts schreiben",
    )
    args = parser.parse_args()

    nur = [s.strip() for s in args.nur.split(",")] if args.nur else None
    dateien = sammle_dateien(nur)

    if not dateien:
        print("Keine Dateien gefunden.", file=sys.stderr)
        return 1

    if args.liste:
        for pfad in dateien:
            print(pfad.relative_to(REPO))
        return 0

    ausgabe = baue_ausgabe(dateien)
    ziel = Path(args.output)
    if not ziel.is_absolute():
        ziel = REPO / ziel
    ziel.parent.mkdir(parents=True, exist_ok=True)
    ziel.write_text(ausgabe, encoding="utf-8")

    zeilen = ausgabe.count("\n") + 1
    try:
        anzeige = ziel.relative_to(REPO)
    except ValueError:
        anzeige = ziel
    print(f"✅ {len(dateien)} Dateien → {anzeige} ({zeilen} Zeilen, {len(ausgabe)} Zeichen)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
