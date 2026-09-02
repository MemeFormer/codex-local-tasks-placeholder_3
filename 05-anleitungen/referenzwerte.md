# 📊 Referenzwerte

Nachschlagewerk mit Zahlen, die man sonst jedes Mal googeln muss.

---

## 1. Anzugsmomente (Nm)

### Lenkkopf

| Verbindung | Nm |
|---|---|
| Ahead-Topcap | 1–2 (nur Spielbeseitigung!) |
| Ahead-Vorbau Klemmschrauben | 5–6 |
| Quill-Vorbau Keilschraube (M6/M8 Inbus) | 20–25 |
| Lenkerklemmschrauben (Faceplate) | 5–6 |
| Bremshebel-Klemmschelle | 5–7 |
| Schalthebel-Klemmschelle | 5–7 |
| Steuersatz-Mutter (Gewinde) | **handfest + 1/8 Umdrehung**, dann kontern |

### Antrieb

| Verbindung | Nm |
|---|---|
| Kurbelschraube Vierkant (M8/M14) | 35–50 |
| Kurbelschraube Hollowtech II (M14) | 35–50 |
| Hollowtech-Klemmschrauben (M5) | 12–14 |
| Kettenblattschrauben | 8–14 |
| Pedale | 35–40 |
| Innenlager-Schalen (BSA) | 35–50 (bzw. handfest mit langem Werkzeug) |
| Kassette-Lockring | **40–50** |
| Schaltwerk-Befestigungsschraube (M10 × 1) | 8–10 |
| Schaltwerk-Zugklemmschraube | 5–7 |
| Umwerfer-Schelle | 5–7 |
| Umwerfer-Zugklemmschraube | 5–7 |
| Schaltröllchen | 3–4 |

### Laufrad & Bremsen

| Verbindung | Nm |
|---|---|
| Konus Nabe | **handfest + 1/16–1/8 Umdrehung lösen** |
| Kontermutter Nabe | handfest + 1/4 Umdrehung, Konus gegenhalten |
| Schnellspanner | **Handkraft** (kein Drehmoment!) |
| Achsmuttern (Vollachse M9/M10) | 15–20 |
| Bremssattel/Zange am Bremssockel | 6–8 |
| Bremsbelagschrauben | 5–7 |
| Bremszug-Klemmschraube | 5–7 |
| Federspannschraube | handfest (kleine Schraube!) |
| Speichennippel | 1,0–1,5 Nm (bzw. nach Felgenhersteller) |

### Anbauteile

| Verbindung | Nm |
|---|---|
| Sattelklemme | 5–8 |
| Sattelstreben-Klemmung | 15–20 (je nach Hersteller) |
| Schutzblechschrauben M5 | ≤ 5 |
| Schutzblechstreben M4/M5 | 3–5 |
| Ständerschrauben | 8–12 |
| Gepäckträgerschrauben M5 | 5–8 |
| Flaschenhalteraufnahme M5 | 3–4 |
| Zuganschläge/Führungen | 3–5 |

⚠️ **Ohne Drehmomentschlüssel:** Bei M5-Inbus mit einem **kurzen** Schlüssel
(≤ 100 mm) „handfest plus eine Viertel Umdrehung“. Bei Alu-Teilen nie mit vollem
Körpereinsatz. Überdrehen von Alu-Gewinden ist der teuerste Fehler beim Schrauben.

---

## 2. Ketten & Kassetten

### Ritzelabstände (Shimano HG)

| Anzahl Ritzel | Ritzelabstand | Ketten-Außenbreite | Innenbreite |
|---|---|---|---|
| 6-fach | 5,5 mm | 7,8 mm | 2,38 mm |
| 7-fach | 5,0 mm | 7,3 mm | 2,38 mm |
| 8-fach | 4,8 mm | 7,1 mm | 2,38 mm |
| **9-fach** | **4,34 mm** | **6,6–6,8 mm** | 2,18 mm |
| 10-fach | 3,95 mm | 5,9 mm | 2,18 mm |
| 11-fach | 3,75 mm | 5,5 mm | 2,18 mm |
| 12-fach | 3,65 mm | 5,2 mm | 2,18 mm |

### Kettenlängen-Berechnung

**Methode A (empfohlen):** Kette um großes Kettenblatt + größtes Ritzel legen,
**nicht durchs Schaltwerk**, schließen und stramm ziehen, dann **+2 Glieder**.

**Methode B (Rechnung):**

```
L = (2 × C) / 12,7 + (Z_groß + Z_ritz) / 2 + 2

C      = Kettenstrebenlänge in mm
Z_groß = Zähne großes Kettenblatt
Z_ritz = Zähne größtes Ritzel
→ auf ganze Glieder aufrunden; bei 3-fach-Kurbeln eher +0,5 Glied extra
```

**Methode C (alte Kette):** nur, wenn die alte Kette die richtige Länge hatte.
⚠️ **Bei deinem Rad nicht anwendbar** – die alte Kette wurde gekürzt.

### Kettenverschleiß

| Messwert (Kettenlehre) | Bedeutung |
|---|---|
| < 0,5 % | neuwertig |
| 0,5–0,75 % | beobachten |
| **0,75 %** | Kette wechseln (Kassette wird geschont) |
| 1,0 % | Kette wechseln – Kassette vermutlich mitverschlossen |
| > 1,0 % | 🔴 Kette + Kassette + Kettenblätter prüfen |

Ketten-Teilung: **12,7 mm** (1/2") pro Glied.

### Schaltwerk-Kapazität

```
Kapazitätsbedarf = (Z_kettenblatt_max − Z_kettenblatt_min) + (Z_ritzel_max − Z_ritzel_min)
```

| Käfiglänge Shimano | Kapazität | max. größtes Ritzel (typisch) |
|---|---|---|
| SS (kurz) | ca. 29 Zähne | 28 |
| GS (mittel) | ca. 35–37 Zähne | 32–34 |
| SGS (lang) | ca. 43–45 Zähne | 36–42 |

### B-Spannung (Abstand Leitrolle → größtes Ritzel)

Soll: **5–6 mm** (Shimano-Angabe; bei modernen 1x-Antrieben herstellerspezifisch)

---

## 3. Durchmesser-Referenz (Wiedererkennen)

| Maß | Was es ist |
|---|---|
| 22,2 mm | Innen-Ø 1"-Gabelschaft = Einsteck-Ø Quill-Vorbau 1" |
| 25,4 mm | Außen-Ø 1"-Gabelschaft **oder** Lenker-Klemm-Ø Standard |
| 25,4 mm | Innen-Ø 1⅛"-Gabelschaft = Einsteck-Ø Quill-Vorbau 1⅛" |
| 28,6 mm | Außen-Ø 1⅛"-Gabelschaft |
| 26,0 mm | Lenker-Klemm-Ø (manche City-/MTB-Lenker) |
| 31,8 mm | Lenker-Klemm-Ø Oversize |
| 35,0 mm | Lenker-Klemm-Ø Super-Oversize (MTB) |
| 9 mm | Achse/Schnellspanner vorne |
| 10 mm | Achse/Schnellspanner hinten |
| 12 / 15 / 20 mm | Steckachsen |
| 100 mm | Einbaubreite vorne (Standard) |
| 110 mm | Einbaubreite vorne (alte Rennräder) |
| 120 / 126 mm | Einbaubreite hinten (alte Rennräder) |
| 130 mm | Einbaubreite hinten (Rennrad) |
| **135 mm** | Einbaubreite hinten (MTB/Trekking) |
| 142 / 148 mm | Steckachse hinten (MTB) |
| 1,5 mm | Bremszug-Innenzug MTB/V-Brake |
| 1,2 mm | Bremszug-Innenzug Rennrad, Schaltzug |
| 5 mm | Bremszug-Hülle außen |
| 4 mm | Schaltzug-Hülle außen |
| 6,5 mm | Felgenbohrung Sclaverand-Ventil |
| 8,5 mm | Felgenbohrung Schrader-Ventil |
| 27,2 / 28,6 / 30,9 / 31,6 mm | gängige Sattelstützen-Ø |
| 28,6 / 31,8 / 34,9 mm | Umwerfer-Schellen-Ø |
| 6,3 × 0,8 mm | Flachstecker Standard |
| 4,8 × 0,8 mm | Flachstecker klein |

---

## 4. Gewinde

| Anwendung | Gewinde | Hinweis |
|---|---|---|
| Steuersatz 1" | **1" × 24 tpi** (25,4 mm, Steigung 1,058 mm) | ⚠️ kein Metrik-Gewinde |
| Steuersatz 1⅛" | **1⅛" × 24 tpi** (28,6 mm) | ⚠️ |
| Pedale | **9/16" × 20 tpi** | links = Linksgewinde |
| Pedale (Kinder/ billige Kurbeln) | 1/2" × 20 tpi | selten |
| Innenlager BSA/Englisch | **1,37" × 24 tpi** | links = Linksgewinde |
| Innenlager Italienisch | 36 mm × 24 tpi | **beide Seiten Rechtsgewinde** ⚠️ |
| Innenlager Französisch | 35 mm × 1,0 | selten |
| Freilaufkörper an der Nabe | M35 × 1,0 | |
| Achse hinten (Vollachse) | M10 × 1,0 | Feingewinde |
| Achse vorne (Vollachse) | M9 × 1,0 | |
| Schnellspanner-Stange | M5 | |
| Bremssattel-Sockel | M6 | |
| Schutzblech / Ständer / Träger | M5, M6 | |
| Schaltwerk-Aufnahme | M10 × 1,0 | |
| Sattelstützen-Klemmschraube | M5, M6 | |
| Ventil (Sclaverand) | M5 × 0,5 | |

**Gewindesteigung bestimmen ohne Lehre:**
- Mutter aus dem Baumarkt testen (M10 × 1,5 Standard / M10 × 1,0 Fein)
- Passen keine Metrik-Muttern → sehr wahrscheinlich Zoll-/Sondergewinde
- Mit einer **Kamm-Gewindelehre** (💰 5–10 €) messen
- Zählen: Gewindegänge pro Zoll (mit Messschieber 25,4 mm abmessen und Gänge zählen)

---

## 5. Reifendruck (bar) – Richtwerte

### Trekking/City (z. B. 37-622)

| Fahrergewicht | vorne | hinten |
|---|---|---|
| < 70 kg | 3,5–4,0 | 4,0–4,5 |
| 70–85 kg | 4,0–4,5 | 4,5–5,0 |
| 85–100 kg | 4,5–5,0 | 5,0–5,5 |
| > 100 kg / mit Gepäck | 5,0 | 5,5–6,0 |

⚠️ Immer den **Maximaldruck auf der Reifenflanke** beachten (z. B. „Max 6,5 bar“).

### Faustformel

```
Druck hinten ≈ Druck vorne × 1,15   (hinten lastet mehr Gewicht)
```

| Reifenbreite | typischer Druckbereich |
|---|---|
| 23–25 mm (Rennrad) | 6–8 bar |
| 28–32 mm | 5–7 bar |
| 35–42 mm (Trekking) | 3,5–5,5 bar |
| 47–57 mm (MTB/City) | 2,5–4 bar |
| 60+ mm | 1,8–3 bar |

---

## 6. ETRTO-Laufradgrößen

| ETRTO-Felgendurchmesser | Zoll-Bezeichnung | Typisch für |
|---|---|---|
| 406 mm | 20" | Klapprad, Kinderrad |
| 451 mm | 20" (sportlich) | BMX, Klapprad |
| 507 mm | 24" | Jugendrad |
| 559 mm | 26" | MTB klassisch, City |
| 584 mm | 27,5" / 650B | MTB, Gravel |
| 590 mm | 26" (englisch) | alte englische Räder |
| **622 mm** | **28" / 29" / 700C** | **Trekking, City, Rennrad, MTB 29"** |
| 630 mm | 27" | alte Rennräder |

> ⚠️ **Die Zoll-Bezeichnung ist nicht eindeutig!** 26" kann 559, 590 oder 597 mm bedeuten.
> **Immer die ETRTO-Zahl verwenden** (steht auf der Reifenflanke, z. B. „37-622“).

**Aufbau der ETRTO-Angabe:** `Reifenbreite - Felgeninnendurchmesser`
z. B. **37-622** = 37 mm breiter Reifen für 622-mm-Felge.

### Reifenbreite ↔ Felgeninnenbreite (Faustregel ETRTO)

| Felgeninnenbreite | passende Reifenbreiten |
|---|---|
| 13–15 mm | 18–25 mm |
| 17–19 mm | 25–35 mm |
| 19–21 mm | 32–45 mm |
| 21–25 mm | 40–60 mm |
| 25–30 mm | 47–75 mm |

---

## 7. Bremsen

| Größe | Sollwert |
|---|---|
| Belagabstand zur Felge (V-Brake) | 1 mm pro Seite |
| Belagabstand (Cantilever) | 1,5–2 mm |
| Toe-in | 0,5–1 mm (vorderer Belagsrand näher an der Felge) |
| Hebelweg bis Druckpunkt | max. 1/3–1/2 |
| Belag-Reststärke (Minimum) | 1 mm über der Trägerplatte |
| Bremszug-Ø V-Brake | 1,5 mm |
| Bremszug-Ø Rennrad | 1,2 mm |
| Bremszughülle-Ø | 5 mm außen, 1,8–2,0 mm innen |
| Biegeradius der Hülle | ≥ 50 mm |

---

## 8. Schaltung

| Größe | Sollwert |
|---|---|
| Abstand Leitrolle → größtes Ritzel (B-Spannung) | 5–6 mm |
| Umwerfer-Höhe über den Zähnen des großen Blatts | 1–3 mm |
| Umwerfer-Parallelität | Leitblech parallel zu den Kettenblättern |
| Zugvorstreckung | einmal mit 60–70 % Kraft anziehen, lösen, neu spannen |

---

## 9. Licht / Elektrik

| Größe | Wert |
|---|---|
| Nabendynamo Nennspannung | 6 V AC |
| Nabendynamo Nennleistung | 3 W |
| Scheinwerfer-Leistung | 3 W |
| Rücklicht-Leistung | 0,6 W |
| Leerlaufspannung bei schneller Fahrt | bis 30–60 V |
| Kabelquerschnitt typisch | 0,75 mm² |
| Flachstecker Standard | 6,3 × 0,8 mm |
| Schrumpfschlauch | mit Innenkleber für Außenbereich |
| Löttemperatur | ca. 350 °C |

---

## 10. Umrechnung & Hilfswerte

| Größe | Wert |
|---|---|
| Ketten-Teilung | 12,7 mm (1/2") |
| 1 Zoll | 25,4 mm |
| 1" × 24 tpi | Steigung 1,058 mm |
| 9/16" | 14,29 mm |
| π | 3,1416 |
| Durchmesser aus Umfang | Umfang ÷ 3,1416 |
| 1 Nm | ca. 0,102 kp·m |
| bar → PSI | bar × 14,5 |
| 1 Umdrehung M10 × 1,0 | 1,0 mm Vorschub |
| 1/16 Umdrehung M10 × 1,0 | 0,06 mm |
| 1/8 Umdrehung M10 × 1,0 | 0,125 mm |

---

## 11. Häufige Ersatzteil-Suchbegriffe

| Ich brauche … | Suchbegriff |
|---|---|
| flache Mutter fürs Gewindesteuersatz | „headset locknut 1 inch thin“ / „Steuersatz Kontermutter 1 Zoll“ |
| Konen für eine Nabe | „Shimano [Nabenmodell] cone axle set“ / „Naben Konus Ersatzteil“ |
| Explosionszeichnung | „Shimano [Modell] EV document pdf“ / „[Modell] exploded view“ |
| Federn für V-Brake | „V-brake return spring“ / „Bremsarm Feder Ersatzteil“ |
| QR-Federn | „quick release spring 9mm 10mm“ |
| Kette 9-fach | „chain 9 speed HG“ |
| Bremszug-Set | „brake cable set MTB stainless“ |
| Ständer KSA 40 | „kickstand KSA 40 adjustable“ |
| Schutzblech-Schellen | „fender universal clamp“ / „P-Schelle“ |
| Schaltauge | „derailleur hanger [Rahmenhersteller] [Modell]“ |
