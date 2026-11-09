# Produktbeschreibung

Fleet Mira App richtet sich an Fahrer, Fuhrparkmitarbeiter und berechtigte Prüfer. Die App unterstützt einen Fuhrpark beziehungsweise ein Unternehmen pro Installation. Ein Fleet-Mira-Server ist für lokale USB-Downloads nicht erforderlich.

## Funktionen

- **Fahrtenschreiber auslesen:** USB-RS-232-Verbindung, auswählbare Profile, Aktivitäten, Ereignisse, Technik und optional Fahrerkarte sowie genaue Geschwindigkeit.
- **Originaldateien lokal behalten:** Vollständige DDD-Dateien bleiben auf dem Android-Gerät und lassen sich exportieren oder an eine Mail-App übergeben.
- **Verlauf durchsuchen:** Kennzeichen, FIN, Fahrernamen, Kartennummern, Zeitraum und getrennte Download-/Übertragungszustände.
- **Dateien übertragen:** Mehrere Profilziele, WLAN als Standard, dauerhafte Aufträge und nachvollziehbare Bestätigungen.
- **DLTNG-Dateien übernehmen:** Vorhandene Originaldateien abrufen und optional an konfigurierte Ziele weiterleiten.
- **Fleet Mira einbinden:** Berechtigter Fahrzeug- und Fahrerbestand, serverseitige Fälligkeiten, gespeicherte Offline-Stände und historische Tätigkeiten.
- **Mobile Führerscheinkontrolle:** Freigeschaltete Online-NFC-Kontrollen; optionale Kameranachweise, Datenabgleich und berechtigte manuelle Bildprüfung.
- **Smartphone und Tablet:** Blaue Material-3-Oberfläche, Hell/Dunkel/System, Icons und an die Fenstergröße angepasste Navigation.

## Voraussetzungen

| Aufgabe | Zusätzlich benötigt |
|---|---|
| USB-Download | Android ab Version 10, USB-Host/OTG, echter RS-232-Adapter, passendes Kabel und zulässiger Kartenzugang |
| DLTNG-Dateiübernahme | Erreichbares kompatibles Gerät und dessen Geräte-API-Schlüssel |
| Fleet-Mira-Fuhrpark | Kompatibler API-Dienst, HTTPS und freigeschalteter Zugang |
| NFC-Kontrolle | NFC-fähiges Gerät, registrierter Chip, freigeschaltete Person und Benutzerrechte |
| Bildnachweise | Kamera-App und serverseitig freigeschalteter Ablauf |

## Grenzen

Die App berechnet keine eigenen gesetzlichen Downloadfristen, Lenkzeitverstöße oder Live-Restlenkzeiten. Fälligkeiten und Auswertungen stammen aus Fleet Mira und zeigen ihren Datenstand. Dateieingang allein bestätigt keinen Fachimport. Die App führt keine eigene kryptografische Signaturprüfung durch.

Direkte Bluetooth-Downloads, eine vollständig übersetzte Download-/Einstellungsoberfläche und automatische Echtheitsprüfung von Führerscheinen gehören nicht zum freigegebenen Funktionsumfang dieses Stands. Die [Versionshinweise](release-notes.md) grenzen Entwicklung und Abnahme ab.
