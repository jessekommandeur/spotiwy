# spotiwy
webprogrammeren

**Samenvatting:**
Met onze webapplicatie kunnen gebruikers met een Spotify premium account een ‘room’ aanmaken. 
Deze kamer kan beginnen met een geïmporteerde afspeellijst maar ook als lege lijst zonder nummer. 
Gebruikers kunnen vervolgens eigen nummers  toevoegen aan de lijst. Gebruikers Ook kunnen zij 
elkaars nummers 'liken' waardoor de meest 'gelikede' nummers bovenaan in de lijst komen te staan. 
Het nummer met de meeste likes wordt vervolgens als eerstvolgende afgespeeld. 
Met deze webapplicatie willen we onenigheid over de muziek welke op feestjes kan ontstaat oplossen. 
De applicatie moet moet visueel aantrekkelijk vormgegeven zijn met een gemakkelijk navigeerbare site.

**Feautures**
De features die we in onze webapplicatie willen implementeren zijn: 
- Een registratie systeem, waarmee gebruikers een nieuw account kunnen aanmaken (registreren)
- Een login systeem, waarmee gebruikers met hun gemaakte account kunnen inloggen. 
- Op de registratiepagina komt een knop die verwijst naar de algemene voorwaarden van de site. (optioneel)
- Er is een pagina waar gebruikers hun gebruikersinstellingen kunnen aanpassen. (optioneel)
- Er is een pagina waar gebruikers hun spotify account kunnen koppelen met spotiwy.
- In de host pagina kunnen gebruikers een kamer aanmaken, waarin eventueel al een afspeellijst in gezet kan worden. 
- In de host pagina kan de 'host' tijdens het aanmaken van de kamer een aantal opties selecteren die van toepassing zijn op de afspeellijst die gemaakt zal worden. 
  Deze opties zijn:
	- Alleen de 'host' kan nummers toevoegen.
	- De 'host' kan nummers deleten.
	- De 'host' kan aangeven hoeveel nummers gebruikers per uur aan de afspeellijst kunnen toevoegen. 
- Als de 'host' alle opties heeft geselecteerd en een kamer aanmaakt, wordt er een kamernummer gegenereerd die andere gebruikers kunnen gebruiken om de kamer te 'joinen'. 
- Op de join pagina kunnen gebruikers het kamernummer invullen om de desbetreffende kamer te joinen. 
- Op de admninroom pagina kan de 'host' van de kamer:
	- Het totaal aantal mensen in de kamer bekijken.(optioneel)
	- De afpeellijst met nummers bekijken. 
	- Nummers 'liken', zodat ze hogerop in de afspeellijst komen. 
	- Nummers verwijderen, indien deze optie tijdens het aanmaken van de kamer is geselecteerd. (optioneel)
	- Nummers toevoegen.
	- De afspeellijst stoppen, op pauze zetten en weer laten doorgaan.
	- Wanneer de 'host' de kamer verlaat, wordt de playlist gestopt.
	- Een optie om de playlist op te slaan (optioneel). 
- Op de normalroom pagina kunnen gebruikers die een pagina hebben gejoined:
	- Het totaal aantal mensen in de kamer bekijken.(optioneel)
	- De afpeellijst met nummers bekijken.
	- Nummers 'liken', zodat ze hogerop in de afspeellijst komen.
	- Nummers toevoegen.
	- Kamer verlaten.
	- De gebruikers worden naar de index pagina gestuurd als de 'host' de kamer verlaat.
	- Een optie om de playlist op te slaan (optioneel).
- Er komt een settings pagina, waarop gebruikers hun:
	- Spotify account kunnen veranderen.
	- E-mail kunnen veranderen. 
	- Gebruikersnaam veranderen.
	- Wachtwoorde veranderen.
	- Een profielfoto kunnen toevoeven. (optioneel)
- Er komt een alert in het scherm als de gebruiker bijvoorbeeld een niet bestaand kamernummer invoerd, of als de gebruikersnaam al bezet is. 

**Minimum viable product**

Deze features zijn nodig voor het minimum viable product:
- Inlog/registratie systeem.
- Een homepage, waarop gebruikers uit de volgende opties kunnen kiezen:
	- Host.
	- Join.
	- Playlists bekijken.
	- Koppelen aan spotify account. 
- Een pagina waarin gebruikers een kamer kunnen 'hosten'. 
- Een pagina waarin gebruikers een kamer kunnen 'joinen'.
- Twee pagina's waarin de 'host' en gebruikers die de kamer hebben gejoined, acties op de playlist kunnen uitvoeren. 
- Een koppel pagina, waarin gebruikers hun spotify account kunnen linken. 

**Afhankelijkheden**
Databronnen: 
- Spotify API: https://developer.spotify.com/documentation/web-api/.

Externe componenten:
- Bootstrap

Concurrerende bestaande websites:
- 

Moeilijkste delen: 
- De spotify API gebruiken.
- Gebruikers koppelen aan hun spotify account. 
- De playlist door meerdere mensen die in dezelfde kamer zitten laten aanpassen. 

**Models en Helpers**
- We maken een application.py
- We maken een helpers.py waarin we functies zetten die we in meerdere pagina's nodig gaan hebben.
Dit zijn functies zoals:
	- Een lookup functie, deze functie haalt de gegevens uit de API van spotify. Als we deze functue aanroepen kunnen we bepaalde gegevens uit spotify halen. 
	- Alert(), deze functie zorgt ervoor dat er doormiddel van een javascript een alert in het scherm komt, als een gebruiker bijvoorbeeld een kamercode invult die niet geldig is. 
- We maken per html pagina een .py pagina waarin we de functies zetten die we speciaal voor die pagina nodig hebben.
Dit zijn functies zoals:
	- Login(), deze functie zorgt ervoor dat gebruikers kunnen inloggen met een bestaand account. 
	- Register(), deze functie zorgt ervoor dat nieuwe gebruikers een account kunnen aanmaken. 
	- Settings(), deze functie zorgt ervoor dat gebruikers hun instellingen kunnen aanpassen. (optioneel).
	- Koppelen(), deze functie zorgt ervoor dat gebruikers hun spotify account met spotiwy kunnen koppelen.
	-  Host(), deze functie zorgt ervoor dat gebruikers een nieuwe kamer kunnen aanmaken. 
		- Binnen deze functie is een andere functie nodig die een kamercode genereert. 
	- Join(), deze functie zorgt ervoor dat gebruikers een bestaande kamer kunnen joinen. 
	- Adminroom(), deze functie zorgt ervoor dat de gebruikers de playlist van hun gemaakte kamer kunnen aanpassen.
	- Normalroom(), deze functie zorgt ervoor dat de gebruikers de playlist van de gejoinde kamer kunnen aanpassen. 

**Plugins en Frameworks**

- from flask import Flask, flash, jsonify, redirect, render_template, request, session
- from flask_session import Session
- from tempfile import mkdtemp
- from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
- from werkzeug.security import check_password_hash, generate_password_hash

**CSS Colours**

- Indigo: 	HEX #5C44DE
- Dark Grey: 	HEX #262626
- White:	HEX #FFFFFF
- Spotify Green:HEX #1DB954
- Youtube Red:	HEX #FF0000

**Schetsen**

- Navigatieboom.png
- Adminroom.png
- Host.png
- Index.png
- Join.png
- Koppelen.png
- Layout.png
- Login.png
- Navbar.png
- Nologin.png
- Normalroom.png
- Register.png
- Settings.png
	
