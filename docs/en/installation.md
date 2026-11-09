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

## First installation from an APK

1. Download or transfer the supplied APK to Android.
2. Open the file. If Android asks, temporarily allow the file manager or browser to **install apps from this source**. Exact wording varies by manufacturer.
3. Check the name **Fleet Mira App** and complete installation.
4. Open the app. Allow notifications if you want to see download status and enabled reminders.
5. Disable the file manager/browser's installation permission when no longer needed.
6. Under **Einstellungen → Darstellung**, choose **System**, **Hell** (light) or **Dunkel** (dark).

Android requests USB permission when an adapter is used. Refusing it prevents that download but does not alter existing files. Optional image evidence opens an installed camera app. NFC is needed only for the corresponding check function.

## Update an existing installation

1. Export or transfer important complete files and verify the destination copies.
2. Use a newer package from the same distributor, with the same Android identifier and signing key.
3. Install it **over the existing app**. Do not uninstall first or clear app storage.
4. Check profiles, history and connections afterwards.

The new name replaces **DTCO Download Android**. Android identifier `de.eh.dtco` remains unchanged. Renaming alone does not reset files or preferences. Android requires a matching update signature; similarly named APKs can have different signatures. Contact the distributor about a signature error instead of forcing an update by uninstalling.

!!! warning "Uninstalling is not updating"
    Uninstalling or clearing app storage removes private files, preferences and saved credentials. Android cloud backup is disabled. Back up original files first using [export or transfer](sharing.md).

Next, follow [quick start](quick-start.md) and configure [servers and settings](settings.md). A cable or server address alone does not establish hardware or server compatibility.
