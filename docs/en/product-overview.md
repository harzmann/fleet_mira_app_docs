# Product overview

Fleet Mira App is intended for drivers, fleet staff and authorised reviewers. Each installation represents one fleet or company. A Fleet Mira server is not required for local USB downloads.

## Features

- **Read a tachograph:** USB-RS-232 connection, selectable profiles, activities, events, technical information and optional driver card and detailed speed.
- **Keep original files locally:** Complete DDD files stay on Android and can be exported or handed to an email app.
- **Search history:** Registration, VIN, driver names, card numbers, date range and separate download and transfer states.
- **Transfer files:** Multiple targets per profile, Wi-Fi by default, durable jobs and traceable acknowledgements.
- **Retrieve DLTNG files:** Download existing originals and optionally forward them to configured targets.
- **Connect Fleet Mira:** Authorised vehicles and drivers, server deadlines, saved offline snapshots and historical activities.
- **Mobile licence checks:** Enabled online NFC checks, optional camera evidence, data comparison and authorised manual image review.
- **Phones and tablets:** Blue Material 3 interface, light/dark/system appearance, icons and adaptive navigation.

## Requirements

| Task | Additional requirements |
|---|---|
| USB download | Android 10 or newer, USB host/OTG, real RS-232 adapter, matching cable and permitted card access |
| DLTNG file retrieval | Reachable compatible device and its device API key |
| Fleet Mira fleet access | Compatible API service, HTTPS and enabled account |
| NFC check | NFC-capable device, registered chip, enabled person and user permissions |
| Image evidence | Camera app and an enabled server workflow |

## Limits

The app does not calculate its own statutory download deadlines, driving-time infringements or live remaining driving times. Deadlines and evaluations come from Fleet Mira and display their data age. File receipt alone does not confirm a completed business import. The app does not perform its own cryptographic signature verification.

Direct Bluetooth downloads, full translation of the download/settings interface and automatic licence authenticity verification are outside this build's released capabilities. See [version and limitations](release-notes.md) for development and acceptance boundaries.
