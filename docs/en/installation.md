# Installation and updates

## Download APK – 0.6.0-dev

[Download Fleet Mira App 0.6.0-dev](https://github.com/harzmann/fleet_mira_app_docs/releases/download/v0.6.0-dev/fleet-mira-app-0.6.0-dev-debug.apk){ .md-button .md-button--primary }

[Release notes](https://github.com/harzmann/fleet_mira_app_docs/releases/tag/v0.6.0-dev) · [SHA256SUMS.txt](https://github.com/harzmann/fleet_mira_app_docs/releases/download/v0.6.0-dev/SHA256SUMS.txt)

This is a **debug-signed development build** for Android 10 or newer, version code **9**. It is published as a GitHub prerelease, not production or hardware approval. APK size: 70048790 bytes.

### Verify SHA-256

File: `fleet-mira-app-0.6.0-dev-debug.apk`

```text
dfd22147d574b52f8b414bf8ffc7ff1ba5e260cb152fa0c832be670bdc93f62f
```

After downloading, verify the complete SHA-256 checksum. For example, in Windows PowerShell:

```powershell
Get-FileHash -Algorithm SHA256 -LiteralPath '.\fleet-mira-app-0.6.0-dev-debug.apk'
```

On Linux:

```sh
sha256sum 'fleet-mira-app-0.6.0-dev-debug.apk'
```

On macOS:

```sh
shasum -a 256 'fleet-mira-app-0.6.0-dev-debug.apk'
```

Compare the complete value with the one above or `SHA256SUMS.txt`. Hexadecimal letter case does not matter. If it differs, do not install the file; download it again from the release. The checksum confirms file identity; updates additionally require a matching APK signature.

## Prepare

You need Android 10 or newer and enough free storage for the app and DDD files. USB downloads require USB host/OTG support. Network features require reachable services. Have the server address and administrator-provided access details ready when using those features.

Use the GitHub prerelease linked above only within your agreed testing/development process, or use a package explicitly approved for your organisation.

IT teams can configure internal Fleet Mira servers without installing an additional CA on tablets by following [Public server certificates](#public-server-certificate).

## First installation from an APK

1. Download or transfer the supplied APK to Android.
2. Open the file. If Android asks, temporarily allow the file manager or browser to **install apps from this source**. Exact wording varies by manufacturer.
3. Check the name **Fleet Mira App** and complete installation.
4. Open the app. Allow notifications if you want to see download status and enabled reminders.
5. Disable the file manager/browser's installation permission when no longer needed.
6. Under **Einstellungen → Darstellung**, choose **System**, **Hell** (light) or **Dunkel** (dark).

Android requests USB permission when an adapter is used. Refusing it prevents that download but does not alter existing files. Optional image evidence opens an installed camera app. NFC is needed only for the corresponding check function.

## Public certificates for internal Fleet Mira servers { #public-server-certificate }

This section is for the organisation's IT team. An internal Fleet Mira server can use a certificate issued by a public CA recognised by the target devices. Tablets then need no additional customer CA. The server remains accessible only through the internal network or the intended VPN connection.

### 1. Prepare the DNS name and DNS-01

Use a name under a registered domain controlled by the organisation. Replace all example values below:

| Setting | Example |
| --- | --- |
| Name in certificate and app | `fleet.example.com` |
| Internal DNS record | `fleet.example.com → 192.168.10.20` |
| HTTPS address | `https://fleet.example.com:8443` |
| Public ACME proof | TXT at `_acme-challenge.fleet.example.com` |

With **DNS-01**, the ACME client proves control of the name using a temporary TXT record in **public authoritative DNS**. A record in internal DNS alone is insufficient. Internal name resolution separately provides the private server address. No inbound Internet access to ports 80, 443 or 8443 is required for this validation. The ACME machine needs outbound access to the CA, DNS-provider API and required DNS resolution. [Let's Encrypt DNS-01](https://letsencrypt.org/docs/challenge-types/#dns-01-challenge)

For unattended renewal, use an automated DNS API and a compatible ACME plugin. Manually entering TXT values does not automate renewal. Restrict API permissions to the required zone or challenge where possible; IT can delegate the challenge through CNAME or NS to a dedicated validation zone. [DNS delegation and separate validation](https://letsencrypt.org/docs/challenge-types/#dns-01-challenge)

### 2. Issue the certificate on Windows

One possible implementation uses **win-acme**, a separately configured tool that is not bundled with the Fleet Mira installer:

1. Install the approved client from the [official win-acme site](https://www.win-acme.com/manual/getting-started) in a permanent protected directory, such as `C:\Program Files\win-acme`. Any additional DNS plugin must match the client version and its plugin-capable distribution.
2. Prepare a new empty directory, `C:\ProgramData\FleetMira\TLS`. Review inheritance and existing access in NTFS security: administrators and the ACME task account need write access; the actual FleetMiraApi service account needs read and directory access. Do not grant general users access to private keys. Protect scripts and ACME credentials too.
3. Run `wacs.exe` as administrator and choose certificate creation with **full options**. Enter the domain manually; an IIS binding is not required. Explicitly select **DNS-01** and the DNS-provider plugin. Default HTTP-01 validation is unsuitable for this procedure. [Full options](https://www.win-acme.com/manual/advanced-use/)
4. Select **PEM files** storage, the TLS directory and the fixed filename prefix `fleet`. Export the PEM key without an interactive password, because FleetMiraApi cannot prompt to unlock it. File permissions protect the key.
5. Do not configure automatic service restart during initial issuance. First configure and verify the API as described below; then add the installation step in section 4 to the renewal.

With this prefix, [PEM storage](https://www.win-acme.com/reference/plugins/store/pemfiles) creates `fleet-chain.pem` (server certificate with intermediate certificates) and `fleet-key.pem` (matching private key), among other files. Use the chain file for the API, not `fleet-chain-only.pem`. Importing only into the Windows certificate store or supplying only a PFX file does not replace these PEM files.

### 3. Configure FleetMiraApi

In the **Enterprise client → Administration → Communication and integrations → API configuration**, save:

| Field | Example |
| --- | --- |
| URL | `https://fleet.example.com:8443` |
| Server / bind address | `0.0.0.0` or the intended local interface |
| Port | `8443` |
| Certificate | `C:\ProgramData\FleetMira\TLS\fleet-chain.pem` |
| Private key | `C:\ProgramData\FleetMira\TLS\fleet-key.pem` |

Paths refer to the **API server**, even when the Enterprise client runs elsewhere. Check the service account in Windows service properties; a standard installation may use `NT SERVICE\FleetMiraApi`. Certificate name, DNS, URL, port and firewall access for the intended internal client networks must agree.

After **Save**, select the correct instance under **API service** and choose **Reload**. The service first checks that the certificate and key can be loaded. Open `https://fleet.example.com:8443/health/live` on the server and a tablet without certificate warnings. Change the app's Fleet Mira target to the same DNS name; create a new target if address editing is blocked. Reselect the main server if necessary, sign in again and synchronise the fleet. Do not substitute the private IP address when the certificate covers only the DNS name.

### 4. Automatic renewal and activation

The [win-acme scheduled task](https://www.win-acme.com/manual/automatic-renewal) periodically checks saved renewals. Verify the task, execution account, permissions and failure notifications. The account needs unattended access to the DNS API, ACME configuration and PEM directory. With split DNS, DNS pre-validation must be able to reach the public challenge zone.

**Replacing PEM files alone does not activate the new certificate in the running listener.** After a successful export to the same configured paths, the API service must reload. For unattended Windows operation, the ACME installation step can restart `FleetMiraApi`. This briefly interrupts the API and requires appropriate service permissions; the worker and PostgreSQL need not restart.

Save this example as `C:\ProgramData\FleetMira\Scripts\Restart-FleetMiraApi.ps1` and adapt the DNS name. It checks for existing non-empty files and then verifies HTTPS health. It does not replace certificate/key-pair verification before deployment and does not perform automatic rollback.

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

Configure the [**Script** installation plugin](https://www.win-acme.com/reference/plugins/installation/script) in the saved renewal to execute this script after PEM export. Issuing files only once, or using a general completion hook without monitored failure status, is insufficient. Only administrators should be able to modify the script, which runs with the ACME account's service permissions.

First verify the full procedure during a maintenance window under the actual task account: PEM export, retained read permissions, restart, HTTPS health and app login. Merely starting a task, or running renewal when no certificate is due, does not demonstrate a successful certificate change. Use ACME staging certificates only in a separate test configuration; Android does not normally trust them.

Monitor task results, installation errors, expiry and the certificate **actually served by the HTTPS endpoint**. Do not disable certificate checks after a failure. Retain a protected, still-valid certificate/key pair for controlled rollback. If ACME runs on a separate management machine, also automate secure deployment of both matching files, their permissions on the API host and activation on that host.

## Update an existing installation

1. Export or transfer important complete files and verify the destination copies.
2. Use a newer package from the same distributor, with the same Android identifier and signing key.
3. Install it **over the existing app**. Do not uninstall first or clear app storage.
4. Check profiles, history and connections afterwards.

The new name replaces **DTCO Download Android**. Android identifier `de.eh.dtco` remains unchanged. Renaming alone does not reset files or preferences. Android requires a matching update signature; similarly named APKs can have different signatures. Contact the distributor about a signature error instead of forcing an update by uninstalling.

!!! warning "Uninstalling is not updating"
    Uninstalling or clearing app storage removes private files, preferences and saved credentials. Android cloud backup is disabled. Back up original files first using [export or transfer](sharing.md).

Next, follow [quick start](quick-start.md) and configure [servers and settings](settings.md). A cable or server address alone does not establish hardware or server compatibility.
