import requests
import urllib.parse
import os
from cs50 import SQL
from random import randint

from flask import redirect, render_template, request, session
from functools import wraps
from threading import Timer
from API import addtracks

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///spotiwy.db")


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/1.0/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("userid") is None:
            return redirect("/homepage")
        return f(*args, **kwargs)
    return decorated_function


def room_required(f):
    """
    Decorate routes to require room.

    http://flask.pocoo.org/docs/1.0/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("roomnumber") is None:
            return redirect("/")
        return f(*args, **kwargs)
    return decorated_function


def generatenumber():

    """generates a random roomnumber"""

    # generate roomnumber
    roomnumber = randint(100000, 999999)

    while db.execute("SELECT * from rooms WHERE roomnumber = :roomnumber", roomnumber = roomnumber):
        roomnumber = randint(100000, 999999)

    return roomnumber



def converter(mseconds):

    """converts miliseconds to song duration"""

    minutes = int(mseconds / 60000)
    seconds = "{:02d}".format(int(mseconds/1000 % 60))
    return str("" + str(minutes) + ":" + str(seconds) + "")



def songtoplaylist():

    """ adds song to spotify playlist"""

    mostliked = db.execute("SELECT MAX(likes) FROM rooms WHERE roomnumber = :roomnumber", roomnumber = session["roomnumber"])
    roomadmin = db.execute("SELECT MAX(userid) FROM rooms WHERE roomnumber = :roomnumber", roomnumber = session["roomnumber"])
    roomadminid = db.execute("SELECT * FROM users WHERE userid = :userid", userid = roomadmin)[0]["spotifykey"]
    playlistid = db.execute("SELECT * FROM rooms WHERE roomnumber = :roomnumber", roomnumber = session["roomnumber"])[0]["playlistid"]

    addtracks(roomadminid,playlistid,mostliked[0]["songid"])



def timer(roomnumber):

    """ recursive code"""

    # if len songs_left < 1
        # stop playing
    # else
        # song to playlist
        # delete song from database
        # timer (time, timer)

def roominfo():

    """Collects information about existing rooms"""

    # Retrieve history from database
    songinfo = db.execute("SELECT song, artist, duration, roomname FROM history")
    room_dict = {}

    # Create dict with history per room
    for song in songinfo:

        # Convert miliseconds to minutes and seconds
        song['duration'] = converter(song['duration'])

        # If the roomnumber exists add song to value
        if song['roomname'] in room_dict:
            room_dict[song['roomname']] = room_dict[song['roomname']] + [song]

        # If roomnumber doesn't exist create dict item
        else:
            room_dict[song['roomname']] = [song]

    return [room_dict, songinfo]