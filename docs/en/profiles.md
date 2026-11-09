# Download profiles

Profiles save data types, activity period, optional driver-card settings and transfer targets. One profile is marked as the default and is preferred when selecting a profile.

## Starter profiles

| Profile | Purpose |
|---|---|
| **Fahrzeug kompakt** | Compact vehicle download |
| **Fahrzeug und Fahrerkarte** | Vehicle and driver card, slot 2 by default |
| **Vollständig** | Includes detailed speed and driver card |

Check the displayed summary: profiles may have been edited after creation.

## Create or edit

Open **Profile → Profil erstellen** or **Bearbeiten**. Enter a name and choose:

1. **Fahrzeug:** activities, events/faults and detailed speed. Overview and technical data are additionally read when access permits.
2. **Fahrer:** driver card and the matching slot.
3. **Aktivitätszeitraum:** **Seit letztem Download** (since last download), **Gesamter Zeitraum** (all) or **Zeitraum** (custom From/To).
4. **Download-Einstellungen:** optional fast baud negotiation and default selection.
5. **Übertragungsziele:** existing targets or local storage only.

**Speichern** saves your choices. End must not precede start. **Seit letztem Download** uses locally proven contiguous activity coverage for that VIN, with day overlap; technical-only or card-only downloads do not advance that boundary.

## Other actions

Use **Aktionen** to **Duplizieren** (duplicate), **Als Standard** (make default) or **Löschen** (delete). The current default profile cannot be deleted. Deleting another profile does not delete existing downloads. Editing a profile does not rewrite earlier files or acknowledgements.
