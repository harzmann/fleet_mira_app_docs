# Privacy and storage

## Data processed

Depending on features used, the app processes original DDD files, registrations and VINs, driver/card information, profiles, target addresses, receipts, fleet/history snapshots and licence-check records. Optional image evidence can contain sensitive document information. Process only data you are authorised to handle.

## Local data and access

Originals are stored in private app storage. Profiles, metadata and jobs are stored locally. Credentials are protected through Android's protected key storage and the app's credential vault. Unsaved credential drafts are not written as ordinary form state to the rotation state bundle.

Each installation represents one company. Remote fleet data is bounded cache, not backup: normally up to 30 days, at most ten historical periods and a limited payload budget. A known access/server change or revocation blocks associated remote data; local originals remain.

## When data leaves the device

Files are handed to configured servers or explicitly chosen export locations. Email handoff gives the selected mail app temporary read access to selected attachments. Check recipients, destination and network permissions. HTTP and plain FTP do not transport-encrypt keys and content; Fleet Mira requires HTTPS.

Licence checks send information for the selected check and optional images to the chosen Fleet Mira service. Image retention and cleanup follow server-side configuration. The app does not promise automatic deletion or legal approval of a retention period.

## Diagnostics and backup

Byte traces can contain full payloads. Enable them only for targeted troubleshooting and share them through the intended protected support channel. Do not publish raw traces, credentials or screenshots containing real person/document information.

Android cloud backup is disabled. Uninstalling or clearing storage removes private app data. Follow [export and backup](sharing.md) before replacing a device. Your organisation defines its binding privacy and retention rules.
