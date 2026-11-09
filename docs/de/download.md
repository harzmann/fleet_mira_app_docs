# Fahrtenschreiber auslesen

## Anschluss vorbereiten

Verwenden Sie einen geeigneten OTG-/USB-Anschluss, einen echten USB-RS-232-Adapter und das für Ihren Fahrtenschreiber passende Kabel. Ein USB-TTL-UART ist kein RS-232-Adapter. Die erforderliche Zugangsberechtigung und Kartenbelegung müssen für den jeweiligen Download vorliegen. Lassen Sie einen ungeklärten Kabelaufbau durch die zuständige Fachperson prüfen.

## Download durchführen

1. Öffnen Sie **Download** und schließen Sie den Adapter an.
2. Wählen Sie bei mehreren Adaptern den richtigen Anschluss.
3. Wählen Sie ein [Downloadprofil](profiles.md). Die Zusammenfassung zeigt Datenarten und Ziele.
4. Mit **Download-Einstellungen bearbeiten** können Sie das Profil vorher anpassen.
5. Starten Sie mit **Download starten** und erteilen Sie Android die USB-Freigabe.
6. Beobachten Sie Phase, Datenmenge und Laufzeit. Der Fortschrittsbalken ist kein garantierter Prozentwert für den Gesamtumfang.
7. Prüfen Sie nach Abschluss den Vorgang im **Verlauf**.

Die lokale Originaldatei wird erst nach vollständigem Empfang als vollständig bereitgestellt. Verweigerte zusätzliche Daten können einen Hinweis erzeugen. Eine Teil-Datei ist kein vollständiger Download.

## Abbrechen und erneut versuchen

**Download abbrechen** beendet den laufenden Versuch oder die ausstehende USB-Freigabe. Prüfen Sie danach den Verlauf. Bereits vollständig gespeicherte Dateien bleiben erhalten; fehlgeschlagene beziehungsweise unvollständige Anteile benötigen einen neuen Download. Ziehen Sie den Adapter während eines regulären Downloads nicht ab.

Die App verwendet einen Android-Downloadservice und kann mit ausgeschaltetem Bildschirm weiterarbeiten. Prüfen Sie dennoch das tatsächliche Abschlussergebnis. Netzwerkübertragungen warten auf das Ende der USB-Sitzung; die lokale Originaldatei bleibt erhalten.

## Ergebnis beurteilen

**Abgeschlossen** beschreibt den lokalen Download. Hinweise, fehlende Daten und Fehler sind separat sichtbar. Für die anschließende Übertragung ist der jeweilige Serverstatus maßgeblich; siehe [Verlauf](history.md). Ein erfolgreicher Softwaretest bestätigt nicht automatisch jedes Telefon-, Adapter-, Kabel- und Fahrtenschreibermodell.
