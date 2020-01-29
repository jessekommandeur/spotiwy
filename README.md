![screenshot webapplicatie](/static/homepage.png "homepage")

# webprogrammeren IK
- Productnaam: **Spotiwy**
- Team: **10**


**Teamleden:**
- Koen Berenschot: vooral application.py, html, css
- Jonne Hoek spaans: vooral JavaScript functies, html, css
- Jesse Kommandeur: vooral application.py, html, css
- Thomas Meijer: vooral API.py, html, css


## Samenvatting
Met onze webapplicatie kunnen gebruikers met een Spotify account een 'room' joinen óf hosten na het aanmaken van een account.
Gebruikers kunnen vervolgens eigen nummers toevoegen aan de kamer. Daarnaast kunnen gebruikers nummers die door anderen toegevoegd
zijn liken en kan de host nummers verwijderen. Met deze webapplicatie willen we onenigheid over muziek op bijvoorbeeld feestjes oplossen.
Na afloop van een feestje kan men eventueel de afspeellijst terugvinden via de history functie. De applicatie is visueel aantrekkelijk
vormgegeven met een gemakkelijk navigeerbare site.


## Opmerkekingen voor de lezer
- Alle bestanden staan in de git repository branch 'master'.
- In application.py staan de functies die ervoor zorgen dat alle features op onze website functioneren.
- In API.py staan functies die de koppeling met spotify mogelijk maakt.
- In helpers.py staan hulpfuncties voor application.py
- In README.md staat uiteraard de read me.
- In HANDLEIDING.txt wordt beschreven hoe de API gekoppeld kan worden wanneer je de website voor de eerste keer wilt runnen.
- In de map static staan:
    - De afbeeldingen van de webapplicatie.
    - De lettertypen van de webapplicatie.
    - Styles.css voor styling van de pagina.
    - Stylesheet.css voor het configureren van lettertypen.
- In de map templates staan:
    - Alle HTML pagina's.
    - op sommige pagina's staat JavaScript.


## Minimum viable product
Deze features van de MVP zijn:
- Inlog/registratie systeem.
- Pagina waarin gebruikers een kamer kunnen 'hosten'.
- Pagina waarin gebruikers een kamer kunnen 'joinen'
- Pagina waarin de 'host' en gebruikers die de kamer hebben gejoined, acties op de playlist kunnen uitvoeren.
-Homepage waarop gebruikers uit de volgende opties kunnen kiezen:
	- Host.
	- Join.
	- Playlists bekijken.


## Key Feautures
De belangrijkste features die we uiteindelijk geïmplementeerd hebben zijn:
- Een registratie systeem waarmee gebruikers een account kunnen aanmaken.
- Een login systeem waarmee gebruikers met een bestaand account kunnen inloggen.
- Een host pagina waar ingelogde gebruikers een kamer kunnen aanmaken.
- Er worden verschillende kamers met bijbehorende kamernummers gegenereerd.
- Gebruikers kunnen een kamer joinen op basis van het kamernummer.
- Gebruikers kunnen een nummer aan een kamer toevoegen en de afspeellijst bekijken.
- De geschiedenis van een kamer wordt opgeslagen en kan bekeken worden.


## Extra Features
De extra features die we uiteindelijk geïmplementeerd hebben zijn:
- Alerts in JavaScript
- Terms & Conditions
- Gebruikers kunnen een nummer liken
- De host kan nummer verwijderen
- Wanneer de 'host' de kamer verlaat, wordt de kamer verwijderd.
- Gebruikers kunnen de kamer verlaten
- Op de host pagina kan host van de room de volgende kameropties toevoegen:
	- De 'host' kan nummers deleten.
	- Maximaal aantal nummers dat gebruiker kan toevoegen.
- Een settings pagina, waarop gebruikers:
	- Gebruikersnaam kunnen veranderen.
	- Wachtwoord kunnen veranderen veranderen.
- Een help pagina.


## Main functions
functies application.py

### navigatie:
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
- like(): zorgt ervoor dat gebruikers nummers kunnen liken.
- bin(): zorgt ervoor dat de host van een kamer nummers kan verwijderen.
- add(): zorgt ervoor dat gebruikers nummers aan de playlist kunnen toevoegen.
- leave(): zorgt ervoor dat gebruikers een kamer kunnen verlaten.
- disband(): zorgt ervoor dat de host de kamer kan ontkoppelen.
- dropdown(): zorgt dat gebruikers uit meerdere nummers of playlists kunnen kiezen.

### extra's:
- history(): zorgt ervoor dat alles wordt opgeslagen en op de history pagina wordt weergegeven.

### cotrole:
- availability(): controleert of een gebruikersnaam al in gebruik is.
- passwordcheck(): gaat na of de twee ingevoerde wachtwoorden overeenkomen.
- usernamecheck(): gaat na of de gebruikersnaam beschikbaar is.


## Helper functions
functies helpers.py

### cookies:
- login_required(): controleert of gebruiker is ingelogd met een bestaand account.
- room_required(): controleert of een gebruiker momenteel in een room zitten.

### coverteren en genereren:
- converter(): converteert miliseconden naar aantal minuten en seconden.
- generatenumber(): genereert een nieuw kamernummer.

### toevoegen en verzamelen:
- songtoplaylist(): voegt nummers toe aan een bestaande spotify playlist.
- roominfo(): verzameld informatie over bestaande kamers.


## API functions
functies API.py

- createplaylist(): maakt playlist aan in spotify.
- searchsong(): zoekt via de s API nummers in spotify op.
- addtracks(): voegt nummers aan spotify playlist toe.
- removetracks(): verwijderd nummers uit spotify playlist.

## Database
Tables van applicatie
- users: slaat data van ingelogde gebruikers op.
- rooms: slaat data van een kamer op.
- history: slaat data van een kamer op als deze verwijdert is.

## Plugins en Frameworks
- Flask
- Flask_session
- Tempfile
- Werkzeug.exceptions:
- Werkzeug.security: passwords
- Bootstrapper: header
- Spotipy: API
- SQL: data


## CSS Colours
- Indigo: HEX #5C44DE
- Dark Grey: HEX #222222
- White: HEX #FFFFFF


## Languages
- Python
- JavaScript
- SQL
- HTML/CSS (markup)