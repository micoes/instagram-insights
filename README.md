# Instagram Insights
Instagram Insights ermöglicht die Analyse deiner Instagram Business oder Creator Profile und der deiner Kunden. Mit den Ergebnissen lässt sich die jeweilige Entwicklung nachvollziehen sowie Kennzahlen für den Nachweis deines ROI messen.

![Dashboard](/micoes/prog2/raw/main/application/static/assets/img/graphics/insights.jpg)

## Einführung
Um Einblicke in die Schwächen und Stärken der eigenen Bemühungen zu erhalten, existieren verschiedene Anwendungen von Drittanbieter, dieser Lösungsansatz beinhaltet allerdings auch ein Risiko bezüglich Datenschutz. Da persönliche Zugangsdaten für eine Nutzung verlangt werden, ist das Vertrauen in den Anbieter vorausgesetzt. Neben den monatlichen Kosten, variiert eine Verwendung weiter mit der Anzahl der Nutzer. Dabei bietet Instagram mit der Instagram Graph API für Werbetreibende kostenlos die Möglichkeit, Daten und Statistiken einzusehen sowie Medien zu verwalten. Instagram Insights soll dafür ein Grundgerüst bieten, welches individuell erweiterbar ist.

## Verwendung
Um die Instagram Graph API erfolgreich aufzurufen, ist ein User Access Token sowie eine User ID erforderlich. Im nächsten Abschnitt wird erläutert, wie du diese generierst. Bevor du beginnst, vergewissere dich, dass du über folgende Zugriffe verfügst:

- ein [Instagram Business](https://help.instagram.com/502981923235522) oder ein [Creator Konto](https://help.instagram.com/1158274571010880)
- eine mit diesem Konto verknüpfte [Facebook Unternehmensseite](https://de-de.facebook.com/business/help/473994396650734?id=939256796236247)

### 1. Entwickler-Konto
Besuche die [Developer-Seite](https://developers.facebook.com/docs/development/register/?locale=de_DE#register-as-a-facebook-developer) und folge den Anweisungen um dich als Facebook-Entwickler zu registrieren sowie anschliessend die Applikation zu erstellen. Wähle dabei **Business** als Typ für deine Applikation aus, um die Instagram Graph API verwenden zu können.

### 2. Zugriffsschlüssel
Anschliessend befindest du dich im Dashboard deiner App, füge hier das Facebook Login- sowie das Instagram Graph API-Produkt hinzu. Mit dem [Graph API Explorer](https://developers.facebook.com/tools/explorer/) lässt sich ein Nutzer-Zugriffsschlüssel generieren, nachdem folgende Berechtigungen hinzugefügt wurden:

- pages_show_list
- pages_read_engagement
- public_profile
- instagram_basic
- instagram_manage_comments
- instagram_manage_insights
- instagram_content_publish

Da standardmäßige Nutzer-Zugriffsschlüssel innerhalb von Stunden ablaufen, ersetzen wir den soeben erstellten mit einem langlebigen Nutzer-Zugriffsschlüssel (User Access Token). Dazu benötigst du den erstellten Nutzer-Zugriffsschlüssel, deine App-ID sowie deinen App-Geheimcode. Letztere findest du im Dashboard deiner App unter **Einstellungen/Allgemeines**. Verwende folgende Anweisungen um einen [Langlebigen Zugriffsschlüssel](https://developers.facebook.com/docs/facebook-login/access-tokens/refreshing) zu erstellen.

### 3. Benutzer ID
Besuche wiederum die [Developer-Seite](https://developers.facebook.com/docs/instagram-api/getting-started#4--get-the-user-s-pages) und folge den Anweisungen unter **Get the User's Pages** sowie **Get the Page's Instagram Business Account** um deine Benutzer ID (User ID) zu erhalten.

### 4. Datenabfrage
Instagram Insights wurde in Python 3.9 entwickelt und funktioniert daher möglicherweise nicht mit früheren Versionen. Für eine Verwendung werden ausserdem folgende Pakete benötigt:

- requests
- Flask
  - Jinja2
  - MarkupSafe
  - Werkzeug
  - click
  - colorama
  - itsdangerous

Ausgangspunkt der Applikation bildet **main.py**, welches für eine Verwendung unter http://127.0.0.1:5000/ ausgeführt werden muss. Für eine Datenabfrage via API Call werden zudem jeweils User ID sowie User Access Token benötigt. Um eine wiederholte Eingabe zu vermeiden, besteht die Möglichkeit, diese durch Auswahl von **Remember me** lokal zu speichern. Sofern User ID und User Access Token korrekt eingegeben wurden, wird das Dashboard für eine Auswertung der Metriken anschliessend dargestellt, wobei sich die gewünschte Zeitspanne durch Auswahl von Start- und Enddatum abfragen lässt. Eine detaillierte Abbildung der Logik ist mit dem folgenden Use Case Diagramm gegeben.

![Use Case Diagramm](/micoes/prog2/raw/main/application/static/assets/img/graphics/use-case.svg?sanitize=true)

## Limitation
Gegenüber der, bis im April 2018 verfügbaren, öffentlichen API ist die Instagram Graph API in verschiedenen Bereichen, aus Gründen des Datenschutzes, wesentlich restriktiver. So ist es beispielsweise nicht weiter möglich via API Call auf Profilinformationen von persönlichen Konten zuzugreifen. Insbesondere die Bestimmung von Unfollower wurde dadurch verunmöglicht.

Andererseits ist zu beachten, dass Facebook Inc. grundsätzlich die koordinierte Weltzeit (UTC±0) verwendet, allerdings mit einer Zeitverschiebung von plus sieben Stunden. Ein Unix-Zeitstempel wie "2021-05-15T07:00:00+0000" entspricht nach der Pazifischen Sommerzeit (UTC-7) 00:00 Uhr für das Datum 2021-05-16, nach der Mitteleuropäischen Sommerzeit (UTC+2) allerdings 09:00 Uhr für das Datum 2021-05-16. Im Rahmen des vorliegenden Projekts wurde ein Tagesintervall von beispielsweise "2021-05-15T07:00:00+0000" bis "2021-05-16T07:00:00+0000" daher dem Datum 2021-05-15 zugeordnet.
