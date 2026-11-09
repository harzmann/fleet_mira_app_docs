# Dateien vom DLTNG

Eine **Dateiquelle** dient dem Abrufen vorhandener DLTNG-Dateien. Ein **Übertragungsziel** dient dem Senden von Dateien. Beide Konfigurationen bleiben getrennt, auch wenn derselbe Geräte-API-Schlüssel verwendet wird.

## Quelle anlegen

Öffnen Sie **Einstellungen → DLTNG-Dateiquellen → Dateiquelle hinzufügen**. Vergeben Sie einen Namen und übernehmen Sie Geräteadresse und Geräte-API-Schlüssel. Standard ist HTTP mit Port 8888; HTTPS ist optional und benötigt ein gültiges Zertifikat. Der Name in der Adresse muss bei HTTPS zum Zertifikat passen. Das Feld **Mobilfunk erlauben** ist eine gesonderte Freigabe.

Eine Netzwerksuche kann Kandidaten für die Einrichtung liefern. Ein Suchtreffer ersetzt weder den richtigen Schlüssel noch die Prüfung der Verbindung. Ein reiner Uploaddienst reicht für die Dateiquelle nicht aus.

## Dateien übernehmen

1. Öffnen Sie **Download → Dateien vom DLTNG** und die gewünschte Quelle.
2. Laden Sie die Dateiliste.
3. Markieren Sie die gewünschten vollständigen Originaldateien.
4. Wählen Sie optional konfigurierte Serverziele für die anschließende Weiterleitung.
5. Starten Sie die Übernahme und prüfen Sie den Auftragsstatus.
6. Nach erfolgreicher Übernahme stehen die lokalen Dateien für Verlauf und Weitergabe bereit.

Die Warteschlange bleibt über App-Neustarts erhalten. USB-Sitzungen haben Vorrang. Inhaltsgleiche vorhandene Originale werden wiederverwendet. Herkunft und ursprünglicher Dateiname bleiben nachvollziehbar; die Quelldatei auf dem DLTNG wird nicht gelöscht.

## Empfang und Weiterleitung unterscheiden

Erfolgreiche Übernahme auf das Telefon, Versand an einen Server und bestätigter Fachimport sind unterschiedliche Schritte. Prüfen Sie jeden Status separat. Bei falschem Schlüssel oder einer nicht erreichbaren Quelle zuerst Zugang und Adresse korrigieren; Dateien nicht vorsorglich am Quellgerät löschen.
