# Servers and settings

On phones, the bottom entry is **Optionen**; the page itself is **Einstellungen**. Appearance, connections and device/support are separate groups.

## Configure a delivery target

1. Open **Übertragungsziele → Server hinzufügen**.
2. Enter a name and choose Fleet Mira, DLTNG, FTPS, SFTP or explicitly FTP.
3. Enter address, port, directory and access details exactly as provided by your administrator. Required fields depend on the protocol.
4. Choose whether mobile data is allowed; Wi-Fi is the default.
5. Save and select the target in the relevant [profiles](profiles.md).

Significant address/protocol changes may be blocked for previously used targets to preserve receipt attribution. Create a new target in that case. **Deaktivieren** prevents further normal use of a target; inspect existing jobs separately.

## Sign in to Fleet Mira

First save a valid Fleet Mira target with an HTTPS address. Sign-in opens a protected browser window. Sign in there and return through the offered app callback. Restart cancelled or expired sign-ins. The app manages and refreshes the resulting tokens automatically. A manually supplied integration token can be used separately where supported by the server configuration.

Uploads, fleet access, driver history and licence checks require their respective server permissions. The app cannot grant them. Select **Hauptserver und Erinnerungen** separately for fleet views; see [fleet](fleet.md).

## Protocol and trust

Fleet Mira requires HTTPS with a valid certificate chain and matching server name. Have IT verify the expected SFTP host key. FTPS and SFTP protect the connection; plain FTP does not.

DLTNG uses the device API key, separate from Fleet Mira access. Its default is HTTP on port 8888, with optional HTTPS. HTTP transmits keys and data unencrypted; choose protocol and network according to your organisation's policy. A certificate error is not bypassed by disabling verification or automatically falling back to HTTP.

## Discovery and diagnostics

**Geräte im Netzwerk** searches for DLTNG/Fleet Mira announcements. A result is a candidate, not proof of trust; older devices may not advertise. Manual setup remains available.

**Diagnose** provides app version, log messages and an optional byte trace for the next download. Traces may contain original payloads. Enable and share them only deliberately, following [privacy and storage](privacy.md).
