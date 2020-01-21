import sys
import spotipy
import spotipy.util as util

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

# shows a user's playlists (need to be authenticated via oauth)
# def Playlist(PlaylistID):

def show_tracks(results):
    for i, item in enumerate(results['items']):
        track = item['track']
        print(
            "   %d %32.32s %s" %
            (i, track['artists'][0]['name'], track['name']))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print("Whoops, need your username!")
        print("usage: python user_playlists_contents.py [username]")
        sys.exit()

    token = util.prompt_for_user_token(username)

    if token:
        sp = spotipy.Spotify(auth=token)
        playlists = sp.user_playlists(username)
        for playlist in playlists['items']:
            if playlist['owner']['id'] == username:
                print()
                print(playlist['name'])
                print('  total tracks', playlist['tracks']['total'])
                results = sp.playlist(playlist['id'], fields="tracks,next")
                tracks = results['tracks']
                show_tracks(tracks)
                while tracks['next']:
                    tracks = sp.next(tracks)
                    show_tracks(tracks)
    else:
        print("Can't get token for", username)


####################################################################################################

######################################################################################################

# import sys
# import spotipy
# import spotipy.util as util
# # De gebruiker heeft een playlist gekozen voor de kamer. Daarna krijgen wij de ID van die playlist, en kunnen we deze functie aanroepen zodat gebruikers kunnen kijken wat er in de playlist zit.

# def playlist2(PlaylistID):

#     username = 'qck1onpl2n6mlpdkiwt8rajq4'
#     token = util.prompt_for_user_token(username)
#     sp = spotipy.Spotify(auth=token)
#     playlist_id = PlaylistID
#     # results = sp.playlist(playlist_id, fields="tracks,next")
#     # test = sp.playlist_tracks(playlist_id, fields=None, limit=100, offset=0, market=None)
#     # test2 = results['items']
#     sp_playlist = sp.user_playlist_tracks(username, playlist_id)
#     # tracks = sp_playlist['name']
#     for element in sp_playlist:
#         print(element)
#     items = sp_playlist['items']
#     items1 = items[0]
#     print(items1['name'])


# playlist2('4pamLh9cgvJcT7btnB7Uod')
# playlist_tracks = sp.user_playlist_tracks(user, playlist_id, fields=None, limit=100, offset=0, market=None)
#######################################################################################################
# shows a user's playlists (need to be authenticated via oauth)

# usage: python APItest.py [username]
# def playlistInfo(username):

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
# playlistInfo("qck1onpl2n6mlpdkiwt8rajq4") #Deze moet automatisch in de functie worden ingevuld

##########################################################################################
# shows tracks for the given artist

# usage: python APItest.py [artist name]

# from spotipy.oauth2 import SpotifyClientCredentials
# import spotipy
# import sys
# def search(naamartiest):

#     client_credentials_manager = SpotifyClientCredentials()
#     sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
#     results = sp.search(q=naamartiest, limit=20)
#     for number, track in enumerate(results['tracks']['items']):
#         TrackID = track['id']
#         print(' ', number, track['name'], "---The ID of the track is:---", TrackID)

# search("marshmello") # De naam die de gebruikers invoeren, wordt in deze functie geplaatst.
###########################################################################################

# Adds tracks to a playlist

# if len(sys.argv) > 3:
#     username = sys.argv[1]
#     playlist_id = sys.argv[2]
#     track_ids = sys.argv[3:]
# else:
#     print("Usage: %s username playlist_id track_id ..." % (sys.argv[0],))
#     sys.exit()

# scope = 'playlist-modify-public'
# token = util.prompt_for_user_token(username, scope)

# if token:
#     sp = spotipy.Spotify(auth=token)
#     sp.trace = False
#     results = sp.user_playlist_add_tracks(username, playlist_id, track_ids)
#     print(results)
# else:
    # print("Can't get token for", username)

######################################################################################################
# Read a playlist

# from spotipy.oauth2 import SpotifyClientCredentials
# import spotipy
# import json

# client_credentials_manager = SpotifyClientCredentials()
# sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# playlist_id = 'spotify:user:spotifycharts:playlist:37i9dQZEVXbJiZcmkrIHGU'
# results = sp.playlist(playlist_id)
# print(json.dumps(results, indent=4))

# @app.route("/connect", methods=["GET", "POST"])
# @login_required
# def connect():
#     """Connect users to their spotify account"""
#     # Connect pagina aanroepten.
#     if request.method == "POST":
#         if request.form.get() == 25
#     else:
#         return render_template("connect.html")