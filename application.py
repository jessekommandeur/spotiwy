import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import login_required, apology, generatenumber, room_required, converter, songtoplaylist
from random import randint
from API import searchsong, createplaylist, connect, addtracks
import json

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///spotiwy.db")

@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    return render_template("index.html")


@app.route("/settings", methods=["GET"])
@login_required
def settings():
    return render_template("settings.html")

###########################################################
@app.route("/connect", methods=["GET", "POST"])
@login_required
def connect2():

    if request.method == "POST":
        username = request.form.get("usernamespotify")
        print("Username is", username)
        URL = connect(username)
        print( "The url is: ", URL)
        return render_template("connect2.html", URL = URL)

    else:
        return render_template("connect.html")


#     return render_template("connect.html")

@app.route("/connect2", methods=["GET", "POST"])
@login_required
def connect3():

    if request.method == "POST":
        username = request.form.get("usernamespotify")
        client_id = 'a96ff6651252429ca81979ee4a293c4f' #placeholder
        client_secret = '24bacae55a1b481cbed2106862e1e087' #placeholder
        redirect_uri = 'https://www.google.nl/callback/'
        scope = 'user-library-read playlist-modify-public playlist-read-private playlist-modify-private playlist-read-collaborative'
        # bitconnect(username, scope, client_id, client_secret, redirect_uri, cache_path=None)
        connect(username)
        return render_template("connect3.html")

    else:
        return render_template("connect.html")



##########################################################

@app.route("/help", methods=["GET"])
@login_required
def help():
    return render_template("help.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    """Register user"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was created
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was created
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Ensure confirmation password was created
        elif not request.form.get("confirmation"):
            return apology("must provide password", 400)

        # Ensure passwords match
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology ("passwords do not match", 400)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 0:
            return apology("username is already taken", 400)

        # Insert username and password into table users
        db.execute("INSERT INTO users (username, hash) VALUES(:username, :hash)", username=request.form.get("username"),
        hash=generate_password_hash(request.form.get("password")))

        # Redirect user to homepage
        return redirect("/login")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")



@app.route("/login", methods=["GET", "POST"])
def login():

    """Log user in"""

    # Forget any user id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
        username=request.form.get("username"))

        # Ensure username exists and password are correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username or password", 400)

        # Remember which user has logged in
        session["userid"] = rows[0]["userid"]

        # Redirect user to homepage
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")



@app.route("/logout")
def logout():

    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")



@app.route("/changeusername", methods=["GET", "POST"])
@login_required
def changeusername():

    """Change username"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure usernames are not same
        if request.form.get("username") == request.form.get("newusername"):
            return apology ("new username cannot be the same as old username", 400)

       # Query database for username
        userinfo = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))

        # Ensure username exists and password are correct
        if len(userinfo) != 1 or not check_password_hash(userinfo[0]["hash"], request.form.get("password")):
            return apology("invalid password", 400)

        # Change usernamee in database
        db.execute("UPDATE users SET username = :username WHERE userid = :userid", username=request.form.get("username"), userid=session["userid"])

        # Redirect user to homepage
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("username.html")



@app.route("/changepassword", methods=["GET", "POST"])
@login_required
def changepassword():

    """Change password"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure passwords are not same
        if request.form.get("password") == request.form.get("newpassword"):
            return apology ("password cannot be the same as old password", 400)

        # Ensure new password match
        if request.form.get("newpassword") != request.form.get("newpassword2"):
            return apology("new password does noet match ")

        # Change password in database
        db.execute("UPDATE users SET hash = :hash WHERE username = :username", username=request.form.get("username"),
        hash=generate_password_hash(request.form.get("newpassword")))

        # Redirect user to homepage
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("password.html")



@app.route("/host", methods=["GET", "POST"])
@login_required
def host():

    """Host a room"""

    if request.method == "POST":

        # go to room
        return redirect("/room")

    # User reached route via GET (as by clicking a link or via redirect)
    else:

        # create room number
        roomnumber = generatenumber()

        # Query database for user spotify key
        spotifykey = db.execute("SELECT * FROM users WHERE userid = :userid", userid = session["userid"])[0]["spotifykey"]

        # Create playlist
        playlistid = createplaylist(spotifykey, "Spotiwy playlist", "This playlist was made with Spotiwy :)")

        # insert roomname into database
        db.execute("INSERT INTO rooms (roomnumber, userid, playlistid) VALUES(:roomnumber, :userid, :playlistid)", userid = session["userid"],
        roomnumber=int(roomnumber), playlistid = playlistid)

        # give
        session["roomnumber"] = roomnumber

        # give admin tag
        session["admin"] = True

        return render_template("host.html", roomnumber = roomnumber)

@app.route("/joinroom", methods=["GET", "POST"])
def join():

    """Join a room"""

    if request.method == "POST":

        # get user input
        userinput =  request.form.get("roomnumber")

        if db.execute("SELECT * FROM rooms WHERE roomnumber = :roomnumber", roomnumber = userinput):

            # ensure user enters 6 digit number
            if not len(request.form.get("roomnumber")) == 6:
                return apology("should enter 6 digit number", 400)

            # ensure user enters digits only
            if not request.form.get("roomnumber").isdigit():
                return apology("should enter digits only number", 400)

            session["roomnumber"] = userinput

            # go to room
            return redirect("/room")
                # TODO
                # redirect to matching room

        else:
            # APOLOGY
            return redirect("/")

    else:
        return render_template("joinroom.html")


@app.route("/homepage", methods=["GET", "POST"])
def homepage():

    if request.method == "POST":
        if not db.execute("SELECT roomnumber FROM rooms where roomnumber = :roomnumber", roomnumber = request.form.get("roomnumber")):
            return render_template("homepage.html", error = "Invalid room")
        else:
            session["roomnumber"] = request.form.get("roomnumber")
            # go to room
            return redirect("/room")

    else:
        # User reached route via GET (as by clicking a link or via redirect)
        return render_template("homepage.html")

@app.route("/room", methods=["GET", "POST"])
@room_required
def room():

    """room functions"""

    playlist = db.execute("SELECT * FROM rooms WHERE songid IS NOT NULL AND roomnumber = :roomnumber", roomnumber = session["roomnumber"])

    roomnumber = session["roomnumber"]

    return render_template("room.html", roomnumber = session["roomnumber"], playlist = playlist, )



@app.route("/leave", methods=["GET"])
@room_required
def leave():

    """user leaves room"""

    # clear visitors cookies
    session.clear()

    return redirect("/")

@app.route("/like", methods=["GET"])
@room_required
def like():

    """like a song"""

    likes = db.execute("SELECT * FROM rooms WHERE roomnumber = :roomnumber AND songid = :songid", roomnumber = session["roomnumber"], songid = 1)

    db.execute("UPDATE rooms SET likes = :likes WHERE roomname = :roomname AND songid = :songid", likes = likes + 1,
    roomname = session["roomname"], songid = 1)

# @app.route("/bin", methods=["GET"])
# @login_required
# @room_required
# def bin():

#     """remove song from list"""

#     db.execute("DELETE FROM rooms WHERE songid = :songid AND roomname = :roomname",  roomname = session["roomname"] , songid =  )



@app.route("/add", methods=["GET", "POST"])
@room_required
def add():

    """add new song to list"""

    if request.method == "POST":

        # get song information from spotify
        songinfo = searchsong(request.form.get("song"), 1, 0, "track")

        if len(songinfo) != 0:
            # APOLOGY

            # store song information in database
            db.execute("INSERT INTO rooms (roomnumber, song, songid, artist, likes, duration) VALUES(:roomnumber, :song, :songid, :artist, :likes, :duration)",
            roomnumber = session["roomnumber"], song = songinfo[0]["track"], songid = songinfo[0]["songid"], artist = songinfo[0]["artist"], likes = 1, duration = songinfo[0]["duration"])

            # query songs
            rows = db.execute("SELECT * FROM rooms WHERE roomnumber = :roomnumber", roomnumber = session["roomnumber"])
            roomnumber = session["roomnumber"]

            mostliked = db.execute("SELECT * FROM rooms WHERE roomnumber = :roomnumber", roomnumber = session["roomnumber"])
            mostliked = {song["songid"] : song["likes"] for song in mostliked if song["likes"] != None}
            roomadmin = db.execute("SELECT * FROM rooms WHERE roomnumber = :roomnumber", roomnumber = session["roomnumber"])[0]["userid"]
            roomadminid = db.execute("SELECT * FROM users WHERE userid = :userid", userid = roomadmin)[0]["spotifykey"]
            playlistid = db.execute("SELECT * FROM rooms WHERE roomnumber = :roomnumber", roomnumber = session["roomnumber"])[0]["playlistid"]
            addtracks(roomadminid,playlistid,max(mostliked))

            return redirect("/room")

        return redirect("/add")

    else:
        return render_template("add.html")



@app.route("/usercheck", methods=["GET"])
def usercheck():

    """Return true if username available, else false, in JSON format"""

    # Receive username
    username = request.args.get("username")

    # Check if user name is unique
    rows = db.execute("SELECT * FROM users WHERE username = :username",
                      username=request.args.get("username"))
    if not rows:
        return jsonify(True)
    else:
        return jsonify(False)

# <<<<<<< HEAD
# @app.route("/searchdrpdwn", methods=["GET"])
# def drpdwn():

#     print("test")
#     songs = searchsong(request.args.get("song"), 5, 0, "track")
#     return jsonify(songs)


@app.route("/disband", methods=["GET", "POST"])
@login_required
@room_required
def disband():

    """admin disband room"""

    if request.method == "POST":

        # store playlist data into history
        db.execute(" INSERT INTO history(song, artist, duration)  SELECT song, artist, duration FROM rooms WHERE roomname = :roomname AND userid = :userid",
        roomname = session["roomnumber"], userid = session["userid"])


        # disbands and deletes room(data) from database
        db.execute("DELETE FROM rooms WHERE userid = :userid", userid = session["userid"])

        # clear room cookies and log user out
        session.clear()

    return redirect("/")



@app.route("/history", methods=["GET", "POST"])
def history():

    """displays previous playlists"""

    songinfo = db.execute("SELECT song, artist, duration, roomname FROM history")
    room_dict = {}
    for song in songinfo:
        song['duration'] = converter(song['duration'])
        if song['roomname'] in room_dict:
            room_dict[song['roomname']] = room_dict[song['roomname']] + [song]
        else:
            room_dict[song['roomname']] = [song]

    if request.method == "POST":
        return render_template("playlist.html", roomnumber = int(request.form.get("roomnumber")), room_dict = room_dict)
    else:
        roomnumbers = [key for key in room_dict.keys()]
        return render_template("history.html", room_dict = room_dict, roomnumbers=roomnumbers)


@app.route("/passwordcheck", methods=["GET"])
def passwordcheck():
    """Return true if username available, else false, in JSON format"""

    # Receive username
    password = request.args.get("password")

    if not password:
        return jsonify(False)

    rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.args.get("username"))

    if not check_password_hash(rows[0]["hash"], request.args.get("password")):
        return jsonify(False)
    else:
        return jsonify(True)

@app.route("/usernamecheck", methods=["GET"])
def usernamecheck():
    """Return true if username exists, else false, in JSON format"""

    # Receive username
    username = request.args.get("username")
    print("test")
    if not request.args.get("username"):
        return jsonify(False)
    elif not db.execute("SELECT * FROM users WHERE username = :username", username=username):
        return jsonify(False)
    else:
        return jsonify(True)


@app.route("/searchdrpdwn", methods=["GET"])
def dropdown():

    print("test")
    songs = searchsong(request.args.get("song"), 5, 0, "track")

    return json.dumps(songs)

@app.route("/terms")
def terms():

    """displays terms & conditions"""

    return render_template("terms.html")