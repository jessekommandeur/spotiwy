import sys
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

# This function takes 1 argument: The spotify username.
# You can connect to the Spotify API by using this function.
def connect(username):

    client_id = 'a96ff6651252429ca81979ee4a293c4f'
    client_secret = '24bacae55a1b481cbed2106862e1e087'
    redirect_uri = 'https://www.google.nl/callback/'

    scope = 'user-library-read playlist-modify-public playlist-read-private playlist-modify-private playlist-read-collaborative user-top-read'
    # This spotipy function will generate a link to a page in which you can connect a spotify account to the webapplication
    token = util.prompt_for_user_token(username, scope)

    if token:
        print("Got the token for:", username)
    else:
        print("Can't get token for", username)

    user_token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
    print("The user token is:", user_token)

# This will execute the function with the spotify username '5q4hjdki3dulvsse9giqoxixt' which is the Webprogrammeren IK account
connect("5q4hjdki3dulvsse9giqoxixt")


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


# Adds tracks to a Spotify playlist
# This function takes 3 arguments: The Spotify username, the playlist ID and the track ID of the song that will be added
def addtracks(username,playlist_id,track_ids):

    token = util.prompt_for_user_token(username)

    if token:
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        # Placing the track id into a list, since for some reason the function doesn't work when you don't
        TrackList = []
        TrackList.append(track_ids)
        # This spotipy function will add the given song to a users playlist
        results = sp.user_playlist_add_tracks(user=username, playlist_id=playlist_id, tracks=TrackList)
    else:
        print("Can't get token for", username)


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


# Creates a new Spotify playlist
# This function takes 3 arguments: The Spotify username, the name of the playlist that will be made and a short description of the playlist
def createplaylist(username, playlist_name, playlist_description):

    token = util.prompt_for_user_token(username)

    if token:
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        # This spotipy function will create a new playlist on the given users account
        playlists = sp.user_playlist_create(username, playlist_name, description=playlist_description)
        return playlists['id']

    else:
        print("Can't get token for", username)
