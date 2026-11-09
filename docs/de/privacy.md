# Datenschutz und Speicherung

## Welche Daten vorkommen

Die App verarbeitet je nach verwendeter Funktion DDD-Originaldateien, Kennzeichen und FIN, Fahrer- und Kartendaten, Profile, Zieladressen, Übertragungsbelege, Fuhrpark-/Historienstände und Führerscheinkontrolldaten. Optionale Bildnachweise können sensible Dokumentdaten enthalten. Erfassen Sie nur Daten, für die Sie berechtigt sind.

## Lokale Daten und Zugänge

Originaldateien liegen im privaten App-Bereich. Profile, Metadaten und Aufträge werden lokal gespeichert. Zugänge werden über den geschützten Android-Schlüsselspeicher beziehungsweise die App-Zugangsdatenverwaltung gesichert. Noch nicht gespeicherte Zugangsentwürfe werden nicht als normale Formularzustände in einer Bildschirmdrehungs-Sicherung abgelegt.

Die App ist für ein Unternehmen pro Installation ausgelegt. Remote-Fuhrparkdaten sind ein begrenzter Cache, keine Sicherung: regulär bis zu 30 Tage, höchstens zehn historische Zeiträume und ein begrenztes Nutzdatenbudget. Ein erkannter Zugangs-/Serverwechsel oder Rechteentzug sperrt die zugehörigen Remote-Daten; lokale Originale bleiben erhalten.

## Wenn Daten das Gerät verlassen

Dateien werden an konfigurierte Ziele oder ausdrücklich ausgewählte Exportorte übergeben. Beim E-Mail-Dialog erhält die gewählte Mail-App vorübergehende Leserechte für die ausgewählten Anhänge. Prüfen Sie Empfänger, Ziel und Netzfreigabe. HTTP und einfaches FTP schützen Schlüssel und Inhalte nicht durch Transportverschlüsselung; Fleet Mira verlangt HTTPS.

Die Führerscheinkontrolle überträgt die zur gewählten Kontrolle gehörenden Informationen und gegebenenfalls Bilder an den gewählten Fleet-Mira-Dienst. Bildaufbewahrung und Bereinigung werden serverseitig nach den eingerichteten Regeln verwaltet. Die App verspricht keine automatische Löschung oder rechtliche Freigabe einer Aufbewahrungsdauer.

## Diagnose und Sicherung

Byte-Traces können vollständige Nutzdaten enthalten. Aktivieren Sie sie nur zur gezielten Fehlersuche und teilen Sie sie ausschließlich über den vorgesehenen geschützten Supportweg. Veröffentlichen Sie keine Roh-Traces, Zugangsdaten oder Screenshots mit echten Personen-/Dokumentdaten.

Android-Cloudsicherung ist deaktiviert. Deinstallation oder Speicherlöschung entfernt private App-Daten. Nutzen Sie vor Gerätewechsel die [Export- und Sicherungsschritte](sharing.md). Für verbindliche betriebliche Datenschutz- und Aufbewahrungsregeln ist Ihre Organisation zuständig.
