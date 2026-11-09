# Installation und Aktualisierung

## APK herunterladen – 0.6.0-dev

[Fleet Mira App 0.6.0-dev herunterladen](https://github.com/harzmann/fleet_mira_app_docs/releases/download/v0.6.0-dev/fleet-mira-app-0.6.0-dev-debug.apk){ .md-button .md-button--primary }

[Release-Hinweise](https://github.com/harzmann/fleet_mira_app_docs/releases/tag/v0.6.0-dev) · [SHA256SUMS.txt](https://github.com/harzmann/fleet_mira_app_docs/releases/download/v0.6.0-dev/SHA256SUMS.txt)

Dies ist eine **Debug-signierte Entwicklungsversion** für Android 10 oder neuer, Versionscode **9**. Sie ist als GitHub-Vorabversion veröffentlicht; eine Produktions- oder Hardwarefreigabe wird damit nicht erteilt. APK-Größe: 70048790 Bytes.

### SHA-256 prüfen

Datei: `fleet-mira-app-0.6.0-dev-debug.apk`

```text
dfd22147d574b52f8b414bf8ffc7ff1ba5e260cb152fa0c832be670bdc93f62f
```

Prüfen Sie nach dem Herunterladen die gesamte SHA-256-Prüfsumme. Auf Windows beispielsweise mit PowerShell:

```powershell
Get-FileHash -Algorithm SHA256 -LiteralPath '.\fleet-mira-app-0.6.0-dev-debug.apk'
```

Auf Linux:

```sh
sha256sum 'fleet-mira-app-0.6.0-dev-debug.apk'
```

Auf macOS:

```sh
shasum -a 256 'fleet-mira-app-0.6.0-dev-debug.apk'
```

Vergleichen Sie den vollständigen Wert mit der Angabe oben oder `SHA256SUMS.txt`. Groß-/Kleinschreibung der Hexadezimaldarstellung ist unerheblich. Bei Abweichung die Datei nicht installieren, sondern erneut vom Release laden. Die Prüfsumme bestätigt die Dateiidentität; für Updates ist zusätzlich eine passende APK-Signatur erforderlich.

## Vorbereiten

Sie benötigen Android 10 oder neuer und ausreichend freien Speicher für App und DDD-Dateien. Für USB-Downloads muss Ihr Gerät USB-Host/OTG unterstützen. Für Netzwerkfunktionen müssen die Gegenstellen erreichbar sein. Halten Sie die Serveradresse und den vom Administrator bereitgestellten Zugang bereit, wenn Sie diese Funktionen verwenden.

Verwenden Sie die oben verlinkte GitHub-Vorabversion nur im vereinbarten Test-/Entwicklungsrahmen oder ein ausdrücklich für Ihr Unternehmen freigegebenes Paket.

## Erstinstallation per APK

1. Laden oder übertragen Sie das bereitgestellte APK auf das Android-Gerät.
2. Öffnen Sie die Datei. Falls Android nachfragt, erlauben Sie der verwendeten Dateien- oder Browser-App vorübergehend **Apps aus dieser Quelle installieren**. Die genaue Bezeichnung hängt vom Hersteller ab.
3. Prüfen Sie den Namen **Fleet Mira App** und schließen Sie die Installation ab.
4. Öffnen Sie die App. Erlauben Sie Benachrichtigungen, wenn Sie Downloadstatus und aktivierte Erinnerungen sehen möchten.
5. Deaktivieren Sie die Installationsfreigabe der Dateien-/Browser-App wieder, wenn Sie sie nicht mehr benötigen.
6. Wählen Sie unter **Einstellungen → Darstellung** bei Bedarf **System**, **Hell** oder **Dunkel**.

Beim Verwenden eines Adapters fordert Android die USB-Freigabe an. Eine Ablehnung verhindert diesen Download, verändert aber keine vorhandenen Dateien. Für optionale Bildnachweise wird eine installierte Kamera-App geöffnet. NFC wird ausschließlich für die entsprechende Kontrollfunktion benötigt.

## Vorhandene Installation aktualisieren

1. Exportieren oder übertragen Sie wichtige vollständige Dateien und überprüfen Sie die Kopien am Ziel.
2. Verwenden Sie ein neueres Paket vom gleichen Bereitsteller, mit derselben Android-Kennung und demselben Signaturschlüssel.
3. Installieren Sie das Paket **über die vorhandene App**. Nicht vorher deinstallieren und nicht den App-Speicher löschen.
4. Prüfen Sie anschließend Profile, Verlauf und Verbindungen.

Der neue Name ersetzt **DTCO Download Android**. Die Android-Kennung `de.eh.dtco` bleibt erhalten. Die Umbenennung selbst setzt Dateien und Einstellungen nicht zurück. Android akzeptiert ein Update nur mit passender Signatur; gleich benannte APKs können unterschiedlich signiert sein. Bei einer Signaturmeldung den Bereitsteller kontaktieren, statt durch Deinstallation ein Update zu erzwingen.

!!! warning "Deinstallation ist keine Aktualisierung"
    Deinstallation oder das Löschen des App-Speichers entfernt private Dateien, Einstellungen und gespeicherte Zugänge. Die Android-Cloudsicherung der App ist deaktiviert. Sichern Sie Originaldateien vorher mit [Export oder Übertragung](sharing.md).

Führen Sie danach den [Schnellstart](quick-start.md) durch. Zugänge richten Sie unter [Server und Einstellungen](settings.md) ein. Ein USB-Kabel oder eine Serveradresse allein bestätigt keine Hardware- beziehungsweise Serverkompatibilität.
