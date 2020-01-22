import pprint
import sys
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

###################################################################################################

# Program to connect Spotify account with spotiwy

# def connect(username):
#     scope = 'user-library-read'
#     token = util.prompt_for_user_token(username, scope)

#     if token:
#         print("Got the token for:", username)
#     else:
#         print("Can't get token for", username)


#     # username = 'qck1onpl2n6mlpdkiwt8rajq4' #placeholder value here
#     client_id = 'a96ff6651252429ca81979ee4a293c4f' #placeholder value here
#     client_secret = '24bacae55a1b481cbed2106862e1e087' #placeholder value here
#     redirect_uri = 'https://www.google.nl/callback/'
#     scope = None


#     user_token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
#     print("The user token is:", user_token)

# connect('qck1onpl2n6mlpdkiwt8rajq4')
######################################################################################################
# Deze functie neemt als argument een PlaylistID en geeft de SongName en bijbehorende ArtistName.
# Hiermee kunnen mensen die een room gejoined zijn kijken welke liedjes er al in de playlist staan.
# Er wordt een list gereturned met daarin dicts met de naam, artiest en id van het lied.

# def playlist(PlaylistID):

#     username = 'qck1onpl2n6mlpdkiwt8rajq4' # De username wordt er automatisch ingezet
#     token = util.prompt_for_user_token(username)
#     sp = spotipy.Spotify(auth=token)
#     results = sp.playlist(playlist_id=PlaylistID, fields="tracks,next")
#     # Het aantal liedjes in de afspeellijst
#     TotalSongs = results['tracks']['total']
#     results2 = results['tracks']
#     PlayList = []
#     for Counter in range(TotalSongs):
#         SongName = results2['items'][Counter]['track']['name']
#         ArtistName = results2['items'][Counter]['track']['album']['artists'][0]['name']
#         SongID = results2['items'][Counter]['track']['id']
#         PlaylistDict = {}
#         PlaylistDict['track'] = SongName
#         PlaylistDict['artist'] = ArtistName
#         PlaylistDict['songid'] = SongID
#         PlayList.append(PlaylistDict)
#     print(PlayList)

#     return PlayList


# playlist('4pamLh9cgvJcT7btnB7Uod') # De playlistID wordt er uiteraard automatisch ingezet.


######################################################################################################
# Deze functie neemt als argument de spotify username en geeft de naam (PlaylistName) en de ID's (PlaylistID) van zijn of haar playlists mee.
# Hiermee kan de maker van een room kijken welke playlists die allemaal heeft.

# def playlistinfo(username):

#     token = util.prompt_for_user_token(username)

#     if token:
#         sp = spotipy.Spotify(auth=token)
#         playlists = sp.user_playlists(username)
#         for playlist in playlists['items']:
#             PlaylistName = playlist['name']
#             print("The name of the playlist is:", PlaylistName)
#             # prints the playlist id
#             PlaylistID = playlist['id']
#             print("The playlist id is:", PlaylistID)
#     else:
#         print("Could not get token for", username)
# playlistinfo("qck1onpl2n6mlpdkiwt8rajq4") #Deze moet automatisch in de functie worden ingevuld

##########################################################################################
# Deze functie neemt 4 argumenten: De string die de gebruiker intypt (De titel van een lied (query)), het aantal nummers die worden opgehaald (limit), de offset en het type. In dit geval een track.
# Het enige wat we nodig hebben van de gebruiker is de string die hij heeft ingetypt. De andere 3 argumenten zetten wij er in.

def searchsong(query, limit, offset, Type):
    username = 'qck1onpl2n6mlpdkiwt8rajq4'
    token = util.prompt_for_user_token(username)

    if token:
        sp = spotipy.Spotify(auth=token)
        playlists = sp.user_playlists(username)
        results = sp.search(query, limit, offset, Type)
        SongList = []
        for number, track in enumerate(results['tracks']['items']):
            SongName = track['name']
            ArtistName = results['tracks']['items'][0]['artists'][0]['name']
            SongID = track['id']
            SongDict = {}
            SongDict['track'] = SongName
            SongDict['artist'] = ArtistName
            SongDict['songid'] = SongID
            SongList.append(SongDict)
        return SongList
    else:
        return None
        # Apology


searchsong("Tramontane", 10, 0, 'track')
##########################################################################################
# Deze functie neemt als argument een naam van een artiest en geeft de TrackName en TrackID.
# Hiermee kunnen gebruikers liedjes opzoeken om toe te voegen aan de afspeellijst.

# def search(naamartiest):

#     client_credentials_manager = SpotifyClientCredentials()
#     sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
#     results = sp.search(q=naamartiest, limit=20)
#     for number, track in enumerate(results['tracks']['items']):
#         TrackName = track['name']
#         TrackID = track['id']
#         print(' ', number, TrackName, "---The ID of the track is:---", TrackID)

# search("Marshmello") # De artiestennaam die de gebruikers invoeren, wordt in deze functie geplaatst.
###########################################################################################
# Adds tracks to a playlist
# Deze functie neemt 3 argumenten, de spotify username, het playlist ID en de track ID van het lied dat je wil toevoegen.

# def addtracks(username,playlist_id,track_ids):

#     token = util.prompt_for_user_token(username)

#     if token:
#         sp = spotipy.Spotify(auth=token)
#         sp.trace = False
#         TrackList = []
#         TrackList.append(track_ids)
#         results = sp.user_playlist_add_tracks(user=username, playlist_id=playlist_id, tracks=TrackList)
#         print(results)
#     else:
#         print("Can't get token for", username)

# addtracks('qck1onpl2n6mlpdkiwt8rajq4','0HnIK5tpE5AC567tb0WnRg','14sOS5L36385FJ3OL8hew4') # Voegt het nummer Happy Now van Kygo toe aan TestPlaylist

####################################################################################################
# Removes tracks from a playlist.
# Deze functie neemt 3 argumenten, de spotify username, het playlist ID en de track ID van het lied dat je wil verwijderen.

# def removetracks(username, playlist_id, track_ids):

#     token = util.prompt_for_user_token(username)

#     if token:
#         sp = spotipy.Spotify(auth=token)
#         sp.trace = False
#         TrackList = []
#         TrackList.append(track_ids)
#         results = sp.user_playlist_remove_all_occurrences_of_tracks(user=username, playlist_id=playlist_id, tracks=TrackList)
#         print(results)
#     else:
#         print("Can't get token for", username)

# removetracks('qck1onpl2n6mlpdkiwt8rajq4','0HnIK5tpE5AC567tb0WnRg','14sOS5L36385FJ3OL8hew4') # Verwijdert het nummer Happy Now van Kygo uit TestPlaylist
####################################################################################################

# Create a new playlist
# Deze functie neemt drie argumenten: De spotify username van de gebruiker, de naam van de playlist die je wil aanmaken en een korte beschrijving van de playlist.

# def createplaylist(username, playlist_name, playlist_description):

#     scope = "playlist-modify-public"
#     token = util.prompt_for_user_token(username, scope)

#     if token:
#         sp = spotipy.Spotify(auth=token)
#         sp.trace = False
#         playlists = sp.user_playlist_create(username, playlist_name, description=playlist_description)
#         pprint.pprint(playlists)
#     else:
#         print("Can't get token for", username)

# createplaylist('qck1onpl2n6mlpdkiwt8rajq4', 'TestPlaylist', 'Een test playlist')

################################################################################################3
# @app.route("/connect", methods=["GET", "POST"])
# @login_required
# def connect():
#     """Connect users to their spotify account"""
#     # Connect pagina aanroepten.
#     if request.method == "POST":
#         if request.form.get() == 25
#     else:
#         return render_template("connect.html")