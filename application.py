import os
from cs50 import SQL
from tempfile import mkdtemp
from random import randint
from flask_session import Session
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import login_required, apology, generatenumber, room_required, converter, songtoplaylist, roominfo
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


""" START MAIN FUNCTIONS """


@app.route("/", methods=["GET", "POST"])
@login_required
def index():

    """Index page for users"""

    return render_template("index.html")


@app.route("/settings", methods=["GET"])
@login_required
def settings():

    """Settings page for users"""

    return render_template("settings.html")


@app.route("/help", methods=["GET"])
@login_required
def help():

    """Help page for users"""

    return render_template("help.html")


#### NOG COMMENTS DOOR JORIS ########################################################################################
@app.route("/register", methods=["GET", "POST"])
def register():

    """Register user"""

    # User reached route via POST
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

    # User reached route via GET
    else:
        return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    """Log user in"""

    # Forget any user id
    session.clear()

    # User reached route via POST
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

    # User reached route via GET
    else:
        return render_template("login.html")
#### NOG COMMENTS DOOR JORIS ########################################################################################


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

    # User reached route via POST
    if request.method == "POST":

        # Ensure usernames are not same
        if request.form.get("username") == request.form.get("newusername"):
            return apology ("new username cannot be the same as old username", 400)

       # Query database for username
        userinfo = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(userinfo) != 1 or not check_password_hash(userinfo[0]["hash"], request.form.get("password")):
            return apology("invalid password", 400)

        # Change usernamee in database
        db.execute("UPDATE users SET username = :username WHERE userid = :userid", username=request.form.get("username"), userid=session["userid"])

        # Redirect user to homepage
        return redirect("/")

    # User reached route via GET
    else:
        return render_template("username.html")


@app.route("/changepassword", methods=["GET", "POST"])
@login_required
def changepassword():

    """Change password"""

    # User reached route via POST
    if request.method == "POST":

        # Ensure passwords are not identical
        if request.form.get("password") == request.form.get("newpassword"):
            return apology ("password cannot be the same as old password", 400)

        # Ensure new passwords match
        if request.form.get("newpassword") != request.form.get("newpassword2"):
            return apology("new password does noet match", 400)

        # Change password in database
        db.execute("UPDATE users SET hash = :hash WHERE username = :username",
                username=request.form.get("username"),hash=generate_password_hash(request.form.get("newpassword")))

        # Redirect user to homepage
        return redirect("/")

    # User reached route via GET
    else:
        return render_template("password.html")


@app.route("/host", methods=["GET", "POST"])
@login_required
def host():

    """Host a room"""

    # User reached route via POST
    if request.method == "POST":

        # Go to room
        return redirect("/room")

    # User reached route via GET
    else:

        # Create room number
        roomnumber = generatenumber()

        # Query database for admin spotify key
        spotifykey = db.execute("SELECT * FROM users WHERE userid = :userid", userid = session["userid"])[0]["spotifykey"]

        # Create playlist in spotify
        playlistid = createplaylist(spotifykey, "Spotiwy playlist", "This playlist was made with Spotiwy :)")

        # Insert room name into database
        db.execute("INSERT INTO rooms (roomnumber, userid, playlistid) VALUES(:roomnumber, :userid, :playlistid)", userid = session["userid"],
                roomnumber=int(roomnumber), playlistid = playlistid)

        # Remember room of user
        session["roomnumber"] = roomnumber

        # Remember user is admin
        session["admin"] = True

        # TO DO
        # checker.delay()

        return render_template("host.html", roomnumber = roomnumber)


@app.route("/joinroom", methods=["GET", "POST"])
def join():

    """Join a room"""

    # Retrieve roomnumbers
    room_dict = roominfo()[0]
    roomnumbers = [key for key in room_dict.keys()]

    if request.method == "POST":

        # get user input
        userinput =  request.form.get("roomnumber")

        # Ensure room exists
        if db.execute("SELECT * FROM rooms WHERE roomnumber = :roomnumber", roomnumber = userinput):

            # Save current room
            session["roomnumber"] = userinput

            # Redirect to room
            return redirect("/room")

        else:

            # Return user to homepage
            return redirect("/")

    else:

        # Render template with available rooms
        return render_template("joinroom.html", roomnumbers = roomnumbers)


@app.route("/homepage", methods=["GET", "POST"])
def homepage():

    """Landing page"""

    # User reached route via POST
    if request.method == "POST":

        # If room does not exist
        if not db.execute("SELECT roomnumber FROM rooms where roomnumber = :roomnumber", roomnumber = request.form.get("roomnumber")):

            # Return user to homepage
            return render_template("homepage.html", error = "Invalid room")

        # Else, go to room
        else:
            session["roomnumber"] = request.form.get("roomnumber")
            return redirect("/room")

    # User reached route via GET
    else:
        return render_template("homepage.html")

@app.route("/room", methods=["GET", "POST"])
@room_required
def room():

    """Room functions"""

    # Set up back end of room
    playlist = db.execute("SELECT * FROM rooms WHERE songid IS NOT NULL AND roomnumber = :roomnumber", roomnumber = session["roomnumber"])

    # Show room and queue
    return render_template("room.html", roomnumber = session["roomnumber"], playlist = playlist)


@app.route("/leave", methods=["GET"])
@room_required
def leave():

    """User leaves room"""

    # Clear user cookies
    session.clear()

    # Redirect to index
    return redirect("/")


@app.route("/like", methods=["GET"])
@room_required
def like():

    """Like a song"""

    # Query amount of likes
    likes = db.execute("SELECT * FROM rooms WHERE roomnumber = :roomnumber AND songid = :songid", roomnumber = session["roomnumber"], songid = 1)

    # Update likes to likes + 1
    db.execute("UPDATE rooms SET likes = :likes WHERE roomname = :roomname AND songid = :songid",
            likes = likes + 1, roomname = session["roomname"], songid = 1)


#### NOG MAKEN ########################################################################################
# @app.route("/bin", methods=["GET"])
# @login_required
# @room_required
# def bin():

#     """remove song from list"""

#     db.execute("DELETE FROM rooms WHERE songid = :songid AND roomname = :roomname",  roomname = session["roomname"] , songid =  )
#### NOG MAKEN ########################################################################################


@app.route("/add", methods=["GET", "POST"])
@room_required
def add():

    """Add new song to queue"""

    # User reached route via POST
    if request.method == "POST":

        # Get song info from spotify
        songinfo = searchsong(request.form.get("song"), 1, 0, "track")

        # If no song is found
        if len(songinfo) != 0:
            # TODO

            # store song information in database
            db.execute("INSERT INTO rooms (roomnumber, song, songid, artist, likes, duration, playing) VALUES(:roomnumber, :song, :songid, :artist, :likes, :duration, :playing)",
                    roomnumber = session["roomnumber"], song = songinfo[0]["track"], songid = songinfo[0]["songid"], artist = songinfo[0]["artist"],
                    likes = 1, duration = converter(songinfo[0]["duration"]), playing = "no")

            # Add song to queue
            rows = db.execute("SELECT * FROM rooms WHERE roomnumber = :roomnumber", roomnumber = session["roomnumber"])
            roomnumber = session["roomnumber"]

            mostliked = db.execute("SELECT * FROM rooms WHERE roomnumber = :roomnumber", roomnumber = session["roomnumber"])
            mostliked = {song["songid"] : song["likes"] for song in mostliked if song["likes"] != None}
            roomadmin = db.execute("SELECT * FROM rooms WHERE roomnumber = :roomnumber", roomnumber = session["roomnumber"])[0]["userid"]
            roomadminid = db.execute("SELECT * FROM users WHERE userid = :userid", userid = roomadmin)[0]["spotifykey"]
            playlistid = db.execute("SELECT * FROM rooms WHERE roomnumber = :roomnumber", roomnumber = session["roomnumber"])[0]["playlistid"]
            addtracks(roomadminid,playlistid,max(mostliked))

            # Go to room
            return redirect("/room")

        # User can try again (TODO)
        return redirect("/add")

    # User reached route via GET
    else:
        return render_template("add.html")


@app.route("/availability", methods=["GET"])
def availability():

    """Checks if username is available, in json format"""

    # Query database for username
    rows = db.execute("SELECT * FROM users WHERE username = :username",
            username=request.args.get("username"))

    # If available, return True
    if len(rows) < 1:
        return jsonify(True)

    # Else, return False
    else:
        return jsonify(False)


@app.route("/disband", methods=["GET", "POST"])
@login_required
@room_required
def disband():

    """Admin disbands room"""

    # User reached route via POST
    if request.method == "POST":

        # Insert queue into history
        db.execute(" INSERT INTO history(song, artist, duration)  SELECT song, artist, duration FROM rooms WHERE roomname = :roomname AND userid = :userid",
        roomname = session["roomnumber"], userid = session["userid"])


        # Deletes room from database
        db.execute("DELETE FROM rooms WHERE userid = :userid", userid = session["userid"])

        # Clear user cookies
        session.clear()

    # Go to index
    return redirect("/")


@app.route("/history", methods=["GET", "POST"])
def history():

    """displays previous playlists"""

    # Retrieve history
    room_dict, songinfo = roominfo()[0], roominfo()[1]

    # Render playlist with added variable
    if request.method == "POST":
        return render_template("playlist.html", roomnumber = int(request.form.get("roomnumber")), room_dict = room_dict)

    # Return search menu with roomnumbers
    else:
        roomnumbers = [key for key in room_dict.keys()]
        return render_template("history.html", room_dict = room_dict, roomnumbers=roomnumbers)


@app.route("/passwordcheck", methods=["GET"])
def passwordcheck():
    """Checks if password and username are valid"""

    # Receive username
    password = request.args.get("password")
    username = request.args.get("username")

    # Ensure password has input
    if not password:
        return jsonify(False)

    # Retrieve data for username
    rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.args.get("username"))

    # Ensure username exists
    if len(rows) < 1:
        return jsonify(False)

    # Ensure password matches
    elif not check_password_hash(rows[0]["hash"], request.args.get("password")):
        return jsonify(False)

    else:
        return jsonify(True)

@app.route("/usernamecheck", methods=["GET"])
def usernamecheck():

    """Return true if username exists, else false, in JSON format"""

    # Receive username
    username = request.args.get("username")

    # Ensure input
    if not request.args.get("username"):
        return jsonify(False)

    # Return if username is unique
    elif not db.execute("SELECT * FROM users WHERE username = :username", username=username):
        return jsonify(False)
    else:
        return jsonify(True)


@app.route("/searchdrpdwn", methods=["GET"])
def dropdown():

    # Get top 5 spotify songs
    songs = searchsong(request.args.get("song"), 5, 0, "track")

    return json.dumps(songs)

@app.route("/terms")
def terms():

    """displays terms & conditions"""

    return render_template("terms.html")