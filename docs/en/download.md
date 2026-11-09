# Tachograph downloads

## Prepare the connection

Use a suitable OTG/USB connection, a real USB-RS-232 adapter and a cable matching your tachograph. A USB-TTL-UART is not an RS-232 adapter. You need the access rights and card arrangement required for the chosen download. Have an uncertain cable arrangement checked by the responsible specialist.

## Download

1. Open **Download** and attach the adapter.
2. If several adapters are present, select the correct one.
3. Select a [download profile](profiles.md). Its summary shows data types and targets.
4. Use **Download-Einstellungen bearbeiten** to adjust the profile first if necessary.
5. Tap **Download starten** and grant Android USB permission.
6. Monitor phase, received data and elapsed time. The progress bar is not a guaranteed percentage of the complete dataset.
7. Check the entry in **Verlauf** afterwards.

An original file becomes available as complete only after full reception. Refused supplementary data can produce a notice. A partial file is not a complete download.

## Cancel and retry

**Download abbrechen** cancels the attempt or pending USB permission. Check history afterwards. Already complete files remain; failed or incomplete parts require a new download. Do not detach the adapter during a normal download.

The app uses an Android download service and can continue with the screen off. Still check the actual completion result. Network transfers wait until the USB session finishes; the local original stays on the device.

## Interpret the result

**Abgeschlossen** describes the local download. Notices, missing data and errors appear separately. Subsequent delivery is governed by the individual server status; see [history](history.md). A successful software test does not automatically qualify every phone, adapter, cable and tachograph model.
