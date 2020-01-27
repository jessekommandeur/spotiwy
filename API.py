import pprint
import sys
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy import oauth2

###################################################################################################
def prompt_for_user_token2(username, scope, client_id,
    client_secret, redirect_uri, cache_path=None):
    ''' prompts the user to login if necessary and returns
        the user token suitable for use with the spotipy.Spotify
        constructor
        Parameters:
         - username - the Spotify username
         - scope - the desired scope of the request
         - client_id - the client id of your app
         - client_secret - the client secret of your app
         - redirect_uri - the redirect URI of your app
         - cache_path - path to location to save tokens
    '''

    cache_path = cache_path or ".cache-" + username
    sp_oauth = oauth2.SpotifyOAuth('b775ac73bb0e4a4e9189d3e6c1821c32', '6327175ca5894985be59ab4f8882e983', 'https://www.google.nl/callback/',
        scope = scope, cache_path=cache_path)


    token_info = sp_oauth.get_cached_token()

    if not token_info:
        print('''
            User authentication requires interaction with your
            web browser. Once you enter your credentials and
            give authorization, you will be redirected to
            a url.  Paste that url you were directed to to
            complete the authorization.
        ''')
        auth_url = sp_oauth.get_authorize_url()
        import webbrowser
        return auth_url

###################################################################################################
def connect(username):

    # username = 'qck1onpl2n6mlpdkiwt8rajq4' #placeholder
    client_id = 'a96ff6651252429ca81979ee4a293c4f' #placeholder
    client_secret = '24bacae55a1b481cbed2106862e1e087' #placeholder
    redirect_uri = 'https://www.google.nl/callback/'
    scope =None

    URL = prompt_for_user_token2(username, 'user-library-read', client_id, client_secret, redirect_uri)
    print("De URL is: ", URL)
    # scope = 'user-library-read playlist-modify-public playlist-read-private playlist-modify-private playlist-read-collaborative'
    # token = util.prompt_for_user_token(username, scope)

    # if token:
    #     print("Got the token for:", username)
    # else:
    #     print("Can't get token for", username)

    # user_token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
    # print("The user token is:", user_token)

    return URL

# connect("5q4hjdki3dulvsse9giqoxixt")
#######################################################################################################
def bitconnect(username, scope, client_id,
    client_secret, redirect_uri, cache_path=None):
    ''' prompts the user to login if necessary and returns
        the user token suitable for use with the spotipy.Spotify
        constructor
        Parameters:
         - username - the Spotify username
         - scope - the desired scope of the request
         - client_id - the client id of your app
         - client_secret - the client secret of your app
         - redirect_uri - the redirect URI of your app
         - cache_path - path to location to save tokens
    '''

    cache_path = cache_path or ".cache-" + username
    sp_oauth = oauth2.SpotifyOAuth('b775ac73bb0e4a4e9189d3e6c1821c32', '6327175ca5894985be59ab4f8882e983', 'https://www.google.nl/callback/',
        scope = scope, cache_path=cache_path)


    token_info = sp_oauth.get_cached_token()

    if not token_info:
        print('''
            User authentication requires interaction with your
            web browser. Once you enter your credentials and
            give authorization, you will be redirected to
            a url.  Paste that url you were directed to to
            complete the authorization.
        ''')
        auth_url = sp_oauth.get_authorize_url()
        try:
            import webbrowser
            webbrowser.open(auth_url)
            print("Opened %s in your browser" % auth_url)
        except BaseException:
            print("Please navigate here: %s" % auth_url)

        print()
        print()
        try:
            response = raw_input("Enter the URL you were redirected to: ")
        except NameError:
            response = input("Enter the URL you were redirected to: ")

        print()
        print()

        code = sp_oauth.parse_response_code(response)
        token_info = sp_oauth.get_access_token(code)
    # Auth'ed API request
    if token_info:
        return token_info['access_token']
    else:
        return None


# bitconnect('o2dznr7gbgsjrz727dcy9pn46' , 'user-library-read playlist-modify-public playlist-read-private playlist-modify-private playlist-read-collaborative', 'a96ff6651252429ca81979ee4a293c4f', '24bacae55a1b481cbed2106862e1e087', 'https://www.google.nl/callback/', None)
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
# This function takes 4 arguments: The string that consists of the input of the user (The title of the song)(query), the amount of numbers that will be returned(limit), the offset and the type. In our case we use 'track', since we want to be able to search by song name.

def searchsong(query, limit, offset, Type):
    username = 'qck1onpl2n6mlpdkiwt8rajq4'
    token = util.prompt_for_user_token(username)

    if token:
        sp = spotipy.Spotify(auth=token)
        results = sp.search(query, limit, offset, Type)
        # The sp.search() function returns a giant dictionary with all the song information in it
        SongList = []
        # Loop through the results to pick out the information we need
        for number, track in enumerate(results['tracks']['items']):
            SongName = track['name']
            ArtistName = results['tracks']['items'][0]['artists'][0]['name']
            SongID = track['id']
            SongDuration = track['duration_ms']
            # Place the song name, artist name, song id and song duration into a dictionary
            SongDict = {}
            SongDict['track'] = SongName
            SongDict['artist'] = ArtistName
            SongDict['songid'] = SongID
            SongDict['duration'] = SongDuration
            # Place the dict with those 4 keys into a list
            SongList.append(SongDict)
        print(SongList)
        return SongList
    else:
        return None


# searchsong("Dance Monkey", 3, 0, 'track')
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
# Adds tracks to a Spotify playlist
# This function takes 3 arguments: The Spotify username, the playlist ID and the track ID of the song that will be added

def addtracks(username,playlist_id,track_ids):

    token = util.prompt_for_user_token(username)

    if token:
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        # Placing the track id into a list, since for some reason the function doesn't work when you don't.
        TrackList = []
        TrackList.append(track_ids)
        # This spotipy function will add the given song to a users playlist
        results = sp.user_playlist_add_tracks(user=username, playlist_id=playlist_id, tracks=TrackList)
    else:
        print("Can't get token for", username)

# addtracks('qck1onpl2n6mlpdkiwt8rajq4','0HnIK5tpE5AC567tb0WnRg','14sOS5L36385FJ3OL8hew4') # Voegt het nummer Happy Now van Kygo toe aan TestPlaylist

####################################################################################################
# Removes tracks from a playlist
# This function takes 3 arguments: The Spotify username, the playlist ID and the track ID of the song that will be added

def removetracks(username, playlist_id, track_ids):

    token = util.prompt_for_user_token(username)

    if token:
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        TrackList = []
        TrackList.append(track_ids)
        # This spotipy function will remove the given song from a users playlist
        results = sp.user_playlist_remove_all_occurrences_of_tracks(user=username, playlist_id=playlist_id, tracks=TrackList)
    else:
        print("Can't get token for", username)

# removetracks('qck1onpl2n6mlpdkiwt8rajq4','0HnIK5tpE5AC567tb0WnRg','14sOS5L36385FJ3OL8hew4') # Verwijdert het nummer Happy Now van Kygo uit TestPlaylist
####################################################################################################
# Creates a new Spotify playlist
# This function takes 3 arguments: The Spotify username, the name of the playlist that will be made and a short description of the playlist

def createplaylist(username, playlist_name, playlist_description):

    token = util.prompt_for_user_token(username)

    if token:
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        playlists = sp.user_playlist_create(username, playlist_name, description=playlist_description)
        return playlists['id']

    else:
        print("Can't get token for", username)

# createplaylist('qck1onpl2n6mlpdkiwt8rajq4', 'dhejdgh', 'Een test playlist')

################################################################################################3