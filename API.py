import sys
import spotipy
import spotipy.util as util

from spotipy.oauth2 import SpotifyClientCredentials

"""API FUNCTIONS"""

# You can connect to the Spotify API by using this function.
def connect(username):

    """Takes 1 argument: Spotify username"""

    # Spotify developer tokens
    client_id = 'a96ff6651252429ca81979ee4a293c4f'
    client_secret = '24bacae55a1b481cbed2106862e1e087'
    redirect_uri = 'https://www.google.nl/callback/'

    # Scopes user has to give permission for
    scope = 'user-library-read playlist-modify-public playlist-read-private playlist-modify-private playlist-read-collaborative user-top-read'

    # This function generates link to a page where user can connect a spotify account
    token = util.prompt_for_user_token(username, scope)

    # Gives feedback about token status
    if token:
        print("Got the token for:", username)
    else:
        print("Can't get token for", username)

    # Saves user token
    user_token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
    print("The user token is:", user_token)

# Executes function with spotify username
connect("5q4hjdki3dulvsse9giqoxixt")


def createplaylist(username, playlist_name, playlist_description):

    """CREATE NEW SPOTIFY PLAYLIST"""

    token = util.prompt_for_user_token(username)

    # Ensures user has valid token
    if token:
        sp = spotipy.Spotify(auth=token)
        sp.trace = False

        # Creates new playlist on spotify account
        playlists = sp.user_playlist_create(username, playlist_name, description=playlist_description)
        return playlists['id']

    else:
        print("Can't get token for", username)


def searchsong(query, limit, offset, Type):

    """SEARCH FOR SONG IN SPOTIFY"""

    username = 'qck1onpl2n6mlpdkiwt8rajq4' #5q4hjdki3dulvsse9giqoxixt

    token = util.prompt_for_user_token(username)

    # Returns dictionary with song info
    if token:
        sp = spotipy.Spotify(auth=token)
        results = sp.search(query, limit, offset, Type)

        # create list to store song info
        songlist = []

        # Loop through results and get song info
        for number, track in enumerate(results['tracks']['items']):
            songname = track['name']
            artistname = results['tracks']['items'][0]['artists'][0]['name']
            songid = track['id']
            songduration = track['duration_ms']

            # Add song info to dictionary
            songdict = {}
            songdict['track'] = songname
            songdict['artist'] = artistname
            songdict['songid'] = songid
            songdict['duration'] = songduration

            # Place dictionary with 4 keys into list
            songlist.append(songdict)

        return songlist

    else:
        return None


def addtracks(username,playlist_id,track_ids):

    """ADD SONGS TO SPOTIFY PLAYLIST"""

    token = util.prompt_for_user_token(username)

    # Ensures user has valid token
    if token:
        sp = spotipy.Spotify(auth=token)
        sp.trace = False

        # Place song id into list
        tracklist = []
        tracklist.append(track_ids)

        # Add the given song to a users playlist
        results = sp.user_playlist_add_tracks(user=username, playlist_id=playlist_id, tracks=tracklist)
    else:
        print("Can't get token for", username)


def removetracks(username, playlist_id, track_ids):

    """REMOVE TRACK FROM SPOTIFY PLAYLIST"""

    token = util.prompt_for_user_token(username)

    # Ensures user has valid token
    if token:

        # Add number by converting into list
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        tracklist = []
        tracklist.append(track_ids)

        # Remove song from users playlist
        results = sp.user_playlist_remove_all_occurrences_of_tracks(user=username, playlist_id=playlist_id, tracks=tracklist)

    else:
        print("Can't get token for", username)