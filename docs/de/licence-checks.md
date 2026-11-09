# Mobile Führerscheinkontrolle

Diese Funktion benötigt einen kompatiblen, erreichbaren Fleet-Mira-API-Dienst, HTTPS, eine Anmeldung und ausdrücklich freigeschaltete Benutzerrechte. Sie arbeitet online. NFC setzt ein geeignetes Android-Gerät und den bereits im Personendatensatz registrierten RFID-/NFC-Chip voraus.

## Zugang öffnen

Öffnen Sie **Einstellungen → Mobile Führerscheinkontrolle** (vor der Anmeldung gegebenenfalls **Mobile driving licence check**), wählen Sie den Fleet-Mira-Server und melden Sie sich über **Anmelden** im Browser an. Nach der Anmeldung werden die erlaubten Funktionen angezeigt. Profilsprache und Region stammen vom Server. Die Hauptbereiche außerhalb dieser Seite können weiterhin deutsche Beschriftungen verwenden.

Für eine **Selbstkontrolle** muss Ihr Benutzer ausdrücklich der berechtigten Person zugeordnet und für Selbstkontrolle freigegeben sein. Eine gleiche E-Mail-Adresse reicht nicht. **Prüferkontrollen**, Auswertung, geschützte Bilder und Prüferentscheidungen benötigen zusätzliche Rechte. Wenden Sie sich bei fehlenden Funktionen an den Administrator.

## NFC-Kontrolle durchführen

1. Wählen Sie die eigene Kontrolle oder als berechtigter Prüfer eine bekannte Person.
2. Starten Sie die NFC-Anforderung und halten Sie den registrierten Chip an die NFC-Lesestelle des Telefons.
3. Prüfen Sie die angezeigte Zuordnung und bestätigen Sie die Kontrolle.
4. Warten Sie auf die Serverbestätigung. Kontrollhistorie und gegebenenfalls nächste Fälligkeit werden angezeigt.

Die Anforderung ist kurzlebig. Bei Ablauf, Netzabbruch oder einem nicht passenden Chip den angezeigten Fehler beachten und eine neue Anforderung starten. Es gibt keine Offline-Vormerkung, die bereits als erfolgreiche Kontrolle gilt. Eine NFC-UID allein beweist weder die Identität der Person noch kryptografisch die Echtheit des Dokuments.

## Optionale Kameranachweise

Wenn freigeschaltet, wählen Sie **Bilder aufnehmen** und fotografieren Vorder- und Rückseite über die Kamera. Nutzen Sie scharfe, gleichmäßig beleuchtete Bilder ohne Spiegelung; alle vier Ränder müssen sichtbar sein. Zwei unterschiedliche Seiten sind erforderlich. Pro Seite sind maximal 10 MiB und 24 Megapixel vorgesehen.

Die App bereinigt EXIF-Daten vor der Übertragung. Prüfen Sie den Übertragungsstatus und wiederholen Sie eine unterbrochene Übertragung, statt sie als abgeschlossen anzusehen. Entwürfe/Nachreichung sind zeitlich begrenzt; der aktuelle Ablauf sieht 24 Stunden vor. Ein Foto- oder OCR-Fehler hebt eine bereits bestätigte NFC-Kontrolle nicht automatisch auf.

## Bildprüfung verstehen

Der Server kann Textfelder erkennen und mit Stammdaten vergleichen. Die App zeigt Referenz, erkannten Wert, Abweichungen und markierte Bildbereiche. Berechtigte Prüfer können zur konkreten Analyse eine begründete Entscheidung speichern, etwa plausibel, Abweichung, nicht beurteilbar oder Neuaufnahme.

Automatische Länder-/Kartenmodellzuordnung und Echtheitsfreigabe sind in diesem Stand nicht qualifiziert. Ein Datenabgleich bestätigt keine Echtheit; UV- und optisch variable Sicherheitsmerkmale lassen sich aus normalen Fotos nicht zuverlässig prüfen. Es werden keine biometrischen Vergleiche und keine externen OCR-Dienste für diesen Ablauf verwendet. Bilder und Kontrolldaten nur nach Ihrer betrieblichen Datenschutzregelung erfassen und teilen.
