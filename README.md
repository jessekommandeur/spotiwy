![screenshot webapplicatie](/static/homepage.png "homepage")

# webprogrammeren IK
- Productnaam: **Spotiwy**
- Team: **10**


**Teamleden:**
- Koen Berenschot: vooral application.py, html, css
- Jonne Hoek spaans: vooral JavaScript functies, html, css
- Jesse Kommandeur: vooral application.py, html, css
- Thomas Meijer: vooral API.py, html, css

## Productvideo Spotiwy: https://www.youtube.com/watch?v=oDY37yoT9V0

## Samenvatting
Met onze webapplicatie kunnen gebruikers met een Spotify account een 'room' joinen zonder account óf hosten na het aanmaken van een account.
Gebruikers kunnen vervolgens eigen nummers toevoegen aan de kamer. Daarnaast kunnen gebruikers nummers die door anderen toegevoegd
zijn liken en kan de host nummers verwijderen. Met deze webapplicatie willen we onenigheid over muziek op bijvoorbeeld feestjes oplossen.
Na afloop van een feestje kan men de afspeellijst terugvinden via de history functie.


## Opmerkekingen voor de lezer
- Alle bestanden staan in de git repository branch 'master'.
- In **application.py** staan de functies die ervoor zorgen dat alle features op onze website functioneren.
- In **API.py** staan functies die de koppeling met spotify mogelijk maakt.
- In **helpers.py** staan hulpfuncties voor application.py
- In **README.md** staat uiteraard de read me.
- In **API_handleiding.txt** wordt beschreven hoe je de API koppelt wanneer je de website voor het eerst gebruikt.
- In de map static staan:
    - De afbeeldingen van de webapplicatie.
    - De lettertypen van de webapplicatie.
    - **Styles.css** voor styling van de pagina.
    - **Stylesheet.css** voor het configureren van lettertypen.
- In de map templates staan:
    - Alle **HTML** pagina's.
    - op sommige pagina's staat JavaScript.


## Minimum viable product
Deze features van de MVP zijn:
- Inlog/registratie systeem.
- Pagina waarin gebruikers een kamer kunnen 'hosten'.
- Pagina waarin gebruikers een kamer kunnen 'joinen'
- Pagina waarin de 'host' en gebruikers die de kamer hebben gejoined, acties op de playlist kunnen uitvoeren.
- Afspeellijsten terug kunnen vinden.
- Homepage waarop gebruikers uit de volgende opties kunnen kiezen:
	- Host.
	- Join.
	- History.


## Key feautures
De belangrijkste features die we uiteindelijk geïmplementeerd hebben zijn:
- Een registratie systeem waarmee gebruikers een account kunnen aanmaken.
- Een login systeem waarmee gebruikers met een bestaand account kunnen inloggen.
- Een host pagina waar ingelogde gebruikers een kamer kunnen aanmaken.
- Het genereren van kamers met bijbehorende kamernummers.
- Het joinen van een kamer op basis van het kamernummer.
- Nummers toevoegen en de afspeellijst bekijken.
- Het opslaan van kamergeschiedenis en kunnen opzoeken.


## Extra features
De extra features die we uiteindelijk geïmplementeerd hebben zijn:
- Alerts in JavaScript.
- Terms & Conditions.
- Een help pagina.
- Gebruikers die ingelogd zijn kunnen nummers liken.
- De host kan nummers verwijderen.
- Wanneer de 'host' de kamer verlaat, wordt de kamer verwijderd.
- Gebruikers kunnen de kamer verlaten.
- Een settings pagina, waarop gebruikers:
	- Gebruikersnaam kunnen veranderen.
	- Wachtwoord kunnen veranderen.


## Main functions
functies application.py

### Directions:
- index(): verwijst gebruikers naar index pagina.
- settings(): verwijst gebruikers naar settings pagina.
- help(): verwijst gebruikers naar de help pagina.
- terms(): verwijst gebruikers naar de terms & conditions.

### account:
- register(): zorgt ervoor dat nieuwe gebruikers een account kunnen aanmaken.
- login(): zorgt ervoor dat gebruikers met een account kunnen inloggen.
- logout(): zorgt ervoor dat gebruikers kunnen uitloggen.
- changeusername(): zorgt ervoor dat gebruikers naam kunnen veranderen.
- changepassword(): zorgt ervoor dat gebruikers wachtwoord kunnen veranderen.

### room setup:
- host(): zorgt ervoor dat gebruikers een room kunnen aanmaken.
- joinroom(): zorgt ervoor dat gebruikers een bestaande kamer kunnen joinen.
- homepage(): zorgt ervoor dat gebruikers die eeen onjuist kamernummer worden doorverwezen.

### room:
- room(): zorgt ervoor dat de Spotify nummers worden weergegeven op de room pagina.
- like(): zorgt ervoor dat ingelogde gebruikers nummers kunnen liken.
- bin(): zorgt ervoor dat de host van een kamer nummers kan verwijderen.
- add(): zorgt ervoor dat gebruikers nummers aan de playlist kunnen toevoegen.
- leave(): zorgt ervoor dat gebruikers een kamer kunnen verlaten.
- disband(): zorgt ervoor dat de host de kamer kan ontkoppelen.
- dropdown(): zorgt dat gebruikers uit meerdere nummers of playlists kunnen kiezen.

### extras:
- history(): zorgt ervoor dat alles wordt opgeslagen en op de history pagina wordt weergegeven.

### checks:
- availability(): controleert of een gebruikersnaam al in gebruik is.
- passwordcheck(): gaat na of de twee ingevoerde wachtwoorden overeenkomen.
- usernamecheck(): gaat na of de gebruikersnaam beschikbaar is.


## Helper functions
functies helpers.py

### cookies:
- login_required(): controleert of gebruiker is ingelogd met een bestaand account.
- room_required(): controleert of een gebruiker momenteel in een room zitten.

### convert and generate:
- converter(): converteert miliseconden naar aantal minuten en seconden.
- generatenumber(): genereert een nieuw kamernummer.

### collect and send info:
- songtoplaylist(): voegt nummers toe aan een bestaande spotify playlist.
- roominfo(): verzameld informatie over bestaande kamers.


## API functions
functies API.py

- connect(): zorgt ervoor dat de API gekoppeld wordt als de webapplicatie voor de eerste keer wordt gerund.
- createplaylist(): maakt playlist aan in spotify.
- searchsong(): zoekt via de s API nummers in spotify op.
- addtracks(): voegt nummers aan spotify playlist toe.
- removetracks(): verwijderd nummers uit spotify playlist.

## Database
Tables van applicatie
- users: slaat data van ingelogde gebruikers op.
- rooms: slaat data van een kamer op.
- history: slaat data van een kamer op als deze verwijderd is.

## Plugins and frameworks
- Flask: run application
- Flask_session: cookies
- Tempfile: temporary files
- Werkzeug.exceptions: erros
- Werkzeug.security: passwords
- Bootstrapper: header
- Spotipy: API
- SQL: data


## CSS colours
- Indigo: HEX #5C44DE
- Dark Grey: HEX #222222
- White: HEX #FFFFFF


## Languages
- Python
- JavaScript
- SQL
- HTML/CSS (markup)
