# Files from DLTNG

A **file source** retrieves existing DLTNG files. A **delivery target** sends files. These configurations remain separate even when they use the same device API key.

## Add a source

Open **Einstellungen → DLTNG-Dateiquellen → Dateiquelle hinzufügen**. Enter a name, device address and device API key. HTTP on port 8888 is the default; optional HTTPS requires a valid certificate. An HTTPS address must match the certificate's server name. **Mobilfunk erlauben** grants mobile-data access separately.

Network discovery can suggest candidates. A result does not replace the correct key or connection verification. An upload-only service does not provide a file source.

## Retrieve files

1. Open **Download → Dateien vom DLTNG** and the required source.
2. Load the file list.
3. Select the complete original files you need.
4. Optionally select configured servers for subsequent forwarding.
5. Start retrieval and inspect job status.
6. Successfully retrieved local files become available for history and sharing.

The queue survives app restarts. USB sessions have priority. Identical existing originals are reused. Provenance and the original filename remain traceable; the DLTNG source file is not deleted.

## Receipt versus forwarding

Successful retrieval to the phone, delivery to a server and confirmed business import are separate steps. Check each state. For an incorrect key or unreachable source, correct access and address first; do not pre-emptively delete files at the source.
