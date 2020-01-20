import sys
import spotipy
import spotipy.util as util

# scope = 'user-library-read'

# if len(sys.argv) > 1:
#     username = sys.argv[1]
# else:
#     print("Usage: %s username" % (sys.argv[0],))
#     sys.exit()

# token = util.prompt_for_user_token(username, scope)

# if token:
#     sp = spotipy.Spotify(auth=token)
#     results = sp.current_user_saved_tracks()
#     for item in results['items']:
#         track = item['track']
#         print(track['name'] + ' - ' + track['artists'][0]['name'])
# else:
#     print("Can't get token for", username)

# import spotipy
# import spotipy.util as util


# username = 'o2dznr7gbgsjrz727dcy9pn46' #placeholder value here
# client_id = 'a96ff6651252429ca81979ee4a293c4f' #placeholder value here
# client_secret = '24bacae55a1b481cbed2106862e1e087' #placeholder value here
# redirect_uri = 'http://localhost:8888/callback/'
# scope = None


# user_token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
# print(user_token)

import sys
import spotipy
import spotipy.util as util

# Shows the contents of every playlist owned by a user:
# def show_tracks(tracks):
#     for i, item in enumerate(tracks['items']):
#         track = item['track']
#         NaamLied = track['name']
#         print("The name of the song is: ", NaamLied )
#         NaamArtiest = (track['artists'][0]['name'])
#         print("The name of the artist(s) is/are: ", NaamArtiest)

# if __name__ == '__main__':
#     if len(sys.argv) > 1:
#         username = sys.argv[1] # De gebruikers van spotiwy geven de usernames op dus deze regel moet nog veranderd worden.
#     else:
#         print("Whoops, need your username!")
#         print("usage: APItest.py [username]")
#         sys.exit()

#     token = util.prompt_for_user_token(username)

#     if token:
#         sp = spotipy.Spotify(auth=token)
#         playlists = sp.user_playlists(username)
#         for playlist in playlists['items']:
#             if playlist['owner']['id'] == username:
#                 PlaylistName = playlist['name']
#                 print("The name of the playlist is:", PlaylistName)
#                 NummersInPlaylist = playlist['tracks']['total']
#                 print ("The total number of tracks in the list is:", NummersInPlaylist)
#                 results = sp.user_playlist(username, playlist['id'], fields="tracks,next")
#                 tracks = results['tracks']
#                 show_tracks(tracks)
#                 while tracks['next']:
#                     tracks = sp.next(tracks)
#                     show_tracks(tracks)
#     else:
#         print("Can't get token for", username)

####################################################################################################
# shows a user's playlists (need to be authenticated via oauth)

# usage: python APItest.py [username]

# if len(sys.argv) > 1:
#     username = sys.argv[1]
# else:
#     print("Whoops, need your username!")
#     print("usage: python user_playlists.py [username]")
#     sys.exit()

# token = util.prompt_for_user_token(username)

# if token:
#     sp = spotipy.Spotify(auth=token)
#     playlists = sp.user_playlists(username)
#     for playlist in playlists['items']:
#         print("The name of the playlist is:", playlist['name'])
#         # prints the playlist id
#         PlayListID = playlist['id']
#         print("The playlist id is:", playlist['id'])
# else:
#     print("Can't get token for", username)

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