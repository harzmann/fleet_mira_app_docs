# Mobile driving-licence checks

This feature requires a compatible reachable Fleet Mira API service, HTTPS, sign-in and explicitly enabled permissions. It works online. NFC requires a suitable Android device and the RFID/NFC chip already registered in the person's record.

## Open access

Open **Einstellungen → Mobile driving licence check** (shown as **Mobile Führerscheinkontrolle** in German), select the Fleet Mira server and use **Anmelden** to sign in through the browser. Permitted features appear after sign-in. Profile language and region come from the server. Areas outside this page may still display German labels.

For a **self-check**, your user must be explicitly linked to the authorised person and enabled for self-checks. A matching email address is insufficient. **Reviewer checks**, evaluation, protected images and review decisions require additional permissions. Ask the administrator about missing features.

## Perform an NFC check

1. Choose your own check, or a known person as an authorised reviewer.
2. Start the NFC request and hold the registered chip near the phone's NFC antenna.
3. Check the displayed association and confirm.
4. Wait for server acknowledgement. Check history and, where supplied, the next deadline are displayed.

The request is short-lived. If it expires, connectivity fails or a chip does not match, follow the displayed error and start a new request. There is no offline queued check that already counts as successful. An NFC UID alone proves neither the person's identity nor cryptographic document authenticity.

## Optional camera evidence

When enabled, use the image-capture action and photograph front and back through the camera. Use sharp, evenly lit images without glare; all four edges must be visible. Two different sides are required. The current limits are 10 MiB and 24 megapixels per side.

The app removes EXIF data before upload. Check transfer status and retry interrupted uploads rather than assuming completion. Drafts and later evidence have a limited submission window, currently 24 hours. A photo or OCR error does not automatically reverse an acknowledged NFC check.

## Understand image review

The server can recognise text fields and compare them with reference records. The app displays the reference, recognised value, differences and highlighted image regions. Authorised reviewers can record a reasoned decision against that analysis: plausible, deviation, not assessable or recapture.

Automatic country/card-model identification and authenticity approval are not qualified in this build. Data comparison does not prove authenticity; normal photographs cannot reliably assess UV or optically variable security features. This workflow does not use biometric comparisons or external OCR services. Capture and share images and check records only according to your organisation's privacy policy.
