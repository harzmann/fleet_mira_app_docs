# Fuhrpark und Fahrer

Unter **Fuhrpark** wechseln Sie zwischen **Lokal**, **Fahrzeuge**, **Fahrer** und **Fälligkeiten**. Lokale Fahrzeugdaten stammen aus eigenen Downloads; die anderen Ansichten benötigen einen berechtigten Fleet-Mira-Zugang.

## Lokale Fahrzeuge

Nach einem Download erscheinen Fahrzeuge, deren FIN eindeutig erkannt wurde. Suchen Sie nach Kennzeichen oder FIN und öffnen Sie die Fahrzeugdetails. Vorhandene Kilometerstände und Kalibrierdaten werden mit ihrem Datenstand angezeigt. Fehlende Angaben werden nicht geschätzt. Ein Download-Schnappschuss und der aktuelle Fahrzeugbestand können unterschiedliche Stände zeigen.

## Fleet Mira verbinden

1. Legen Sie einen Fleet-Mira-Server unter **Einstellungen → Übertragungsziele** an und melden Sie sich bei Bedarf im Browser an.
2. Öffnen Sie **Einstellungen → Hauptserver und Erinnerungen**.
3. Wählen Sie das aktive Fleet-Mira-Ziel als Hauptserver.
4. Speichern Sie und starten Sie den Abgleich. Anschließend stehen die berechtigten Datensätze im Fuhrpark zur Verfügung.

Nur ein Hauptserver steuert den angezeigten Remote-Fuhrpark. Weitere Datei-Übertragungsziele bleiben davon unabhängig. Fehlende Berechtigungen müssen vom Administrator freigeschaltet werden; Uploadzugang allein reicht nicht für Fuhrpark und Historie.

## Fahrerhistorie

Öffnen Sie einen Fahrer und **Lenk- / Ruhezeiten**. Wählen Sie Von/Bis und bei Bedarf **Zeitraum abgleichen**. Der Zeitraum reicht höchstens bis heute in der Auswertungszeitzone und umfasst maximal 31 Tage. Die Bereiche **Tage**, **Wochen**, **Tätigkeiten**, **Bewertung** und **Quellen** erläutern die vom Server bereitgestellte Historie.

Unbekannte Zeiten sind keine Ruhezeit. Die Ansicht ist historisch und zeigt keinen Live-Restlenkzeitzähler. Bewertungen stammen aus der Serverauswertung.

## Datenstand, Offlinebetrieb und Erinnerungen

Jede Remote-Ansicht zeigt ihren gespeicherten Stand. **Jetzt abgleichen** fordert einen aktuellen vollständigen Stand an; ohne Netz bleibt der bisherige vollständige Stand sichtbar. Automatische Abrufe erfolgen ungefähr alle sechs Stunden, abhängig von Android und der Netzfreigabe. USB-Sitzungen haben Vorrang.

Erinnerungen lassen sich auf der Hauptserverseite einschalten und benötigen Android-Benachrichtigungen. Sie verwenden Serverfälligkeiten und Vorwarnungen; aus mehr als 24 Stunden alten Ständen entstehen keine neuen Erinnerungen. Der Hintergrundlauf ist ab 09:00 UTC vorgesehen und kann von Android verzögert werden. Offline-Cache ist kein Backup und kennt einen serverseitigen Widerruf erst nach erneutem Kontakt. Ein bekannter Rechteentzug, Tokenablauf oder Zugangswechsel kann den Remote-Stand sperren; lokale Originaldateien bleiben erhalten.
