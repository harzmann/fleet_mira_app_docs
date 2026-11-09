# Fleet and drivers

In **Fuhrpark**, switch between **Lokal**, **Fahrzeuge**, **Fahrer** and **Fälligkeiten**. Local vehicle information comes from your downloads; the other views require authorised Fleet Mira access.

## Local vehicles

After a download, vehicles with an unambiguous VIN appear here. Search registration or VIN and open vehicle details. Available odometer and calibration information includes its data age. Missing information is not estimated. A download snapshot may differ from the current vehicle record.

## Connect Fleet Mira

1. Add a Fleet Mira server under **Einstellungen → Übertragungsziele** and sign in through the browser if needed.
2. Open **Einstellungen → Hauptserver und Erinnerungen**.
3. Select the active Fleet Mira target as the primary server.
4. Save and refresh. Authorised records then become available in the fleet.

One primary server supplies the remote fleet. Other file-delivery targets remain independent. An administrator must grant missing permissions; upload access alone does not enable fleet records and history.

## Driver history

Open a driver and **Lenk- / Ruhezeiten**. Select From/To and, when needed, **Zeitraum abgleichen**. The period ends no later than today in the evaluation time zone and covers at most 31 days. **Tage**, **Wochen**, **Tätigkeiten**, **Bewertung** and **Quellen** explain the server-provided history.

Unknown time is not rest time. This is historical information, not a live remaining-driving-time counter. Assessments come from server evaluation.

## Data age, offline use and reminders

Each remote view shows its saved snapshot. **Jetzt abgleichen** requests a new complete snapshot; offline, the previous complete one remains visible. Automatic retrieval runs approximately every six hours, subject to Android scheduling and network permissions. USB sessions have priority.

Enable reminders on the primary-server page and allow Android notifications. They use server deadlines and advance notices; snapshots older than 24 hours do not produce new reminders. The background run is scheduled from 09:00 UTC and Android may delay it. Offline cache is not a backup and cannot know about a server revocation until reconnection. Known loss of rights, token expiry or an access change may block remote data; local originals remain.

## Tablet views

These landscape tablet captures use synthetic demonstration data. Click or tap an image to inspect it at its original size.

The area selector opens local records, server vehicles, drivers and deadlines. This example shows local vehicle records.

**Light**

![Fleet Mira App – Tablet – fleet – Light](assets/screenshots/tablet/light-fleet.png)

**Dark**

![Fleet Mira App – Tablet – fleet – Dark](assets/screenshots/tablet/dark-fleet.png)
