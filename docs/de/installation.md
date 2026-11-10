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

Die betreuende IT findet die Einrichtung interner Fleet-Mira-Server ohne zusätzliche CA-Installation auf Tablets unter [Öffentliches Serverzertifikat](#public-server-certificate).

## Erstinstallation per APK

1. Laden oder übertragen Sie das bereitgestellte APK auf das Android-Gerät.
2. Öffnen Sie die Datei. Falls Android nachfragt, erlauben Sie der verwendeten Dateien- oder Browser-App vorübergehend **Apps aus dieser Quelle installieren**. Die genaue Bezeichnung hängt vom Hersteller ab.
3. Prüfen Sie den Namen **Fleet Mira App** und schließen Sie die Installation ab.
4. Öffnen Sie die App. Erlauben Sie Benachrichtigungen, wenn Sie Downloadstatus und aktivierte Erinnerungen sehen möchten.
5. Deaktivieren Sie die Installationsfreigabe der Dateien-/Browser-App wieder, wenn Sie sie nicht mehr benötigen.
6. Wählen Sie unter **Einstellungen → Darstellung** bei Bedarf **System**, **Hell** oder **Dunkel**.

Beim Verwenden eines Adapters fordert Android die USB-Freigabe an. Eine Ablehnung verhindert diesen Download, verändert aber keine vorhandenen Dateien. Für optionale Bildnachweise wird eine installierte Kamera-App geöffnet. NFC wird ausschließlich für die entsprechende Kontrollfunktion benötigt.

## Öffentliches Zertifikat für interne Fleet-Mira-Server { #public-server-certificate }

Dieser Abschnitt richtet sich an die betreuende IT. Ein interner Fleet-Mira-Server kann ein Zertifikat einer auf den Zielgeräten anerkannten öffentlichen Zertifizierungsstelle verwenden. Dann benötigen die Tablets keine zusätzliche Kunden-CA. Der Server bleibt ausschließlich im internen Netz beziehungsweise über den vorgesehenen VPN-Zugang erreichbar.

### 1. DNS-Namen und DNS-01 vorbereiten

Verwenden Sie einen Namen unter einer tatsächlich registrierten, vom Unternehmen kontrollierten Domain. Alle folgenden Werte sind Beispiele und müssen ersetzt werden:

| Einstellung | Beispiel |
| --- | --- |
| Name im Zertifikat und in der App | `fleet.example.com` |
| Interner DNS-Eintrag | `fleet.example.com → 192.168.10.20` |
| HTTPS-Adresse | `https://fleet.example.com:8443` |
| Öffentlicher Nachweis für ACME | TXT unter `_acme-challenge.fleet.example.com` |

Bei **DNS-01** weist der ACME-Client die Kontrolle über den Namen durch einen vorübergehenden TXT-Eintrag im **öffentlichen autoritativen DNS** nach. Ein Eintrag ausschließlich im internen DNS genügt nicht. Die interne Namensauflösung liefert dagegen die private Serveradresse. Es ist keine eingehende Internetfreigabe von Port 80, 443 oder 8443 für diese Validierung erforderlich. Der ACME-Rechner benötigt ausgehenden Zugriff auf Zertifizierungsstelle, DNS-Provider-API und die benötigte DNS-Auflösung. [DNS-01 bei Let's Encrypt](https://letsencrypt.org/docs/challenge-types/#dns-01-challenge)

Für unbeaufsichtigte Erneuerung einen DNS-Provider mit automatisierbarer API und einem passenden ACME-Plugin verwenden. Manuelles Eintragen des TXT-Werts automatisiert die Erneuerung nicht. API-Rechte möglichst auf die benötigte Zone beziehungsweise Challenge beschränken; bei Bedarf kann die IT die Challenge per CNAME oder NS an eine eigene Validierungszone delegieren. [DNS-Delegation und getrennte Validierung](https://letsencrypt.org/docs/challenge-types/#dns-01-challenge)

### 2. Zertifikat unter Windows ausstellen

Eine mögliche Umsetzung ist **win-acme**. Es ist ein separat einzurichtendes Werkzeug und kein Bestandteil des Fleet-Mira-Installers:

1. Den freigegebenen Client von der [offiziellen win-acme-Seite](https://www.win-acme.com/manual/getting-started) in ein dauerhaftes, geschütztes Verzeichnis installieren, etwa `C:\Program Files\win-acme`. Ein benötigtes DNS-Plugin muss zur verwendeten Version und zur Variante mit Plugin-Unterstützung passen.
2. Ein neues, leeres Verzeichnis `C:\ProgramData\FleetMira\TLS` vorbereiten. Über die NTFS-Sicherheit Vererbung und bestehende Freigaben prüfen: Administratoren und das ACME-Aufgabenkonto benötigen Schreibzugriff; das tatsächliche FleetMiraApi-Dienstkonto benötigt Lesen und Verzeichniszugriff. Keine allgemeinen Benutzerrechte auf private Schlüssel vergeben. Skripte und ACME-Zugangsdaten ebenfalls schützen.
3. `wacs.exe` mit Administratorrechten starten und die Zertifikaterstellung mit **vollständigen Optionen** wählen. Den Domainnamen manuell vorgeben; eine IIS-Bindung ist nicht erforderlich. Als Validierung ausdrücklich **DNS-01** und das DNS-Provider-Plugin auswählen. Die Standardauswahl HTTP-01 passt nicht zu diesem Ablauf. [Vollständige Optionen](https://www.win-acme.com/manual/advanced-use/)
4. Als Speicher **PEM files** wählen, das TLS-Verzeichnis und den festen Dateinamenspräfix `fleet` konfigurieren. Den PEM-Schlüssel ohne Passwortabfrage exportieren, da FleetMiraApi keine interaktive Schlüsselentsperrung unterstützt. Er wird durch die Dateirechte geschützt.
5. Bei der ersten Ausstellung noch keinen automatischen Dienstneustart auswählen. Zuerst die folgenden API-Einstellungen und die Verbindung prüfen. Danach den Erneuerungsauftrag um den Installationsschritt aus Abschnitt 4 ergänzen.

Mit dem konfigurierten Präfix erzeugt der [PEM-Speicher](https://www.win-acme.com/reference/plugins/store/pemfiles) unter anderem `fleet-chain.pem` (Serverzertifikat mit Zwischenzertifikaten) und `fleet-key.pem` (passender privater Schlüssel). Für die API die Kettendatei verwenden, nicht `fleet-chain-only.pem`. Ein Import nur in den Windows-Zertifikatsspeicher oder eine PFX-Datei allein ersetzt diese PEM-Dateien nicht.

### 3. FleetMiraApi konfigurieren

Im **Enterprise-Client → Administration → Kommunikation und Integrationen → API-Konfiguration** speichern:

| Feld | Beispiel |
| --- | --- |
| URL | `https://fleet.example.com:8443` |
| Server / Bind-Adresse | `0.0.0.0` oder die gewünschte lokale Schnittstelle |
| Port | `8443` |
| Zertifikat | `C:\ProgramData\FleetMira\TLS\fleet-chain.pem` |
| Privater Schlüssel | `C:\ProgramData\FleetMira\TLS\fleet-key.pem` |

Die Pfade beziehen sich auf den **API-Server**, auch wenn der Enterprise-Client auf einem anderen Rechner läuft. Das Dienstkonto lässt sich in den Windows-Diensteigenschaften prüfen; bei einer Standardinstallation kann es `NT SERVICE\FleetMiraApi` sein. Zertifikatsname, DNS, URL, Port und Firewallfreigabe für die vorgesehenen internen Clientnetze müssen zusammenpassen.

Nach **Speichern** unter **API-Dienst** die richtige Instanz auswählen und **Neu laden** ausführen. Der Dienst prüft zunächst, ob er Zertifikat und Schlüssel laden kann. Auf dem Server und einem Tablet `https://fleet.example.com:8443/health/live` ohne Zertifikatswarnung aufrufen. In der App das Fleet-Mira-Ziel auf denselben DNS-Namen umstellen; bei gesperrter Adressänderung ein neues Ziel anlegen. Gegebenenfalls den Hauptserver neu auswählen, erneut anmelden und den Fuhrpark abgleichen. Die private IP-Adresse darf nicht als Ersatzadresse verwendet werden, wenn das Zertifikat nur für den DNS-Namen ausgestellt ist.

### 4. Automatische Erneuerung und Aktivierung

Die [win-acme-Aufgabenplanung](https://www.win-acme.com/manual/automatic-renewal) prüft regelmäßig die gespeicherten Erneuerungsaufträge. Kontrollieren Sie Aufgabe, Ausführungskonto, Rechte und Fehlerbenachrichtigung. Das Konto muss auch ohne interaktive Anmeldung auf DNS-API, ACME-Konfiguration und PEM-Verzeichnis zugreifen können. Unter Split-DNS muss die DNS-Vorprüfung die öffentliche Challenge-Zone erreichen können.

**Neue PEM-Dateien allein aktivieren das Zertifikat nicht im laufenden Listener.** Nach erfolgreichem Export in dieselben konfigurierten Pfade muss der API-Dienst neu laden. Für einen vollständig unbeaufsichtigten Windows-Ablauf kann der ACME-Installationsschritt den Dienst `FleetMiraApi` neu starten. Das verursacht eine kurze API-Unterbrechung und benötigt entsprechende Dienstrechte; Worker und PostgreSQL werden dafür nicht neu gestartet.

Das folgende Beispiel als `C:\ProgramData\FleetMira\Scripts\Restart-FleetMiraApi.ps1` ablegen und den DNS-Namen anpassen. Es prüft vorhandene, nicht leere Dateien und anschließend den HTTPS-Dienst. Es ersetzt keine Prüfung des Zertifikat-/Schlüsselpaars vor der Bereitstellung und führt keinen automatischen Rückbau aus.

```powershell
$ErrorActionPreference = 'Stop'
$tlsDirectory = 'C:\ProgramData\FleetMira\TLS'
foreach ($name in @('fleet-chain.pem', 'fleet-key.pem')) {
    $path = Join-Path $tlsDirectory $name
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
        throw "Missing TLS file: $name"
    }
    if ((Get-Item -LiteralPath $path).Length -eq 0) {
        throw "Empty TLS file: $name"
    }
}
Restart-Service -Name 'FleetMiraApi' -ErrorAction Stop
$service = Get-Service -Name 'FleetMiraApi'
$service.WaitForStatus('Running', [TimeSpan]::FromSeconds(60))
$deadline = (Get-Date).AddSeconds(60)
do {
    try {
        $health = Invoke-RestMethod -Uri 'https://fleet.example.com:8443/health/live' -TimeoutSec 10 -ErrorAction Stop
        if ($health.ok -and $health.service -eq 'FleetMiraApi') {
            exit 0
        }
    } catch {
        # Retry startup; normal TLS validation remains enabled.
    }
    Start-Sleep -Seconds 2
} while ((Get-Date) -lt $deadline)
throw 'FleetMiraApi HTTPS health check failed'
```

Im gespeicherten Erneuerungsauftrag nach dem PEM-Export das [Installationsplugin **Script**](https://www.win-acme.com/reference/plugins/installation/script) mit diesem Skript hinterlegen. Einmalig nur Dateien auszustellen oder einen allgemeinen Abschluss-Hook ohne überwachten Fehlerstatus einzutragen genügt nicht. Änderungen am Skript nur Administratoren erlauben; das ACME-Konto führt es mit seinen Dienstrechten aus.

Den Ablauf zuerst im Wartungsfenster mit dem tatsächlichen Aufgabenkonto prüfen: PEM-Export, unveränderte Leserechte, Neustart, HTTPS-Health und App-Anmeldung. Eine lediglich gestartete Aufgabe oder ein normaler Erneuerungslauf ohne fälliges Zertifikat belegt noch keinen erfolgreichen Zertifikatswechsel. ACME-Staging-Zertifikate nur in einer getrennten Testkonfiguration verwenden; Android vertraut ihnen regulär nicht.

Im Betrieb Aufgabenergebnis, Installationsfehler, Ablaufdatum und das **tatsächlich am HTTPS-Endpunkt ausgelieferte Zertifikat** überwachen. Bei Fehlern keine Zertifikatsprüfung abschalten. Ein gesichertes, noch gültiges Zertifikat-/Schlüsselpaar für einen kontrollierten Rückbau vorhalten. Bei getrennter ACME-Verwaltung zusätzlich den sicheren Export beider zusammengehöriger Dateien, ihre Rechte auf dem API-Host und den dortigen Aktivierungsschritt automatisieren.

## Vorhandene Installation aktualisieren

1. Exportieren oder übertragen Sie wichtige vollständige Dateien und überprüfen Sie die Kopien am Ziel.
2. Verwenden Sie ein neueres Paket vom gleichen Bereitsteller, mit derselben Android-Kennung und demselben Signaturschlüssel.
3. Installieren Sie das Paket **über die vorhandene App**. Nicht vorher deinstallieren und nicht den App-Speicher löschen.
4. Prüfen Sie anschließend Profile, Verlauf und Verbindungen.

Der neue Name ersetzt **DTCO Download Android**. Die Android-Kennung `de.eh.dtco` bleibt erhalten. Die Umbenennung selbst setzt Dateien und Einstellungen nicht zurück. Android akzeptiert ein Update nur mit passender Signatur; gleich benannte APKs können unterschiedlich signiert sein. Bei einer Signaturmeldung den Bereitsteller kontaktieren, statt durch Deinstallation ein Update zu erzwingen.

!!! warning "Deinstallation ist keine Aktualisierung"
    Deinstallation oder das Löschen des App-Speichers entfernt private Dateien, Einstellungen und gespeicherte Zugänge. Die Android-Cloudsicherung der App ist deaktiviert. Sichern Sie Originaldateien vorher mit [Export oder Übertragung](sharing.md).

Führen Sie danach den [Schnellstart](quick-start.md) durch. Zugänge richten Sie unter [Server und Einstellungen](settings.md) ein. Ein USB-Kabel oder eine Serveradresse allein bestätigt keine Hardware- beziehungsweise Serverkompatibilität.
