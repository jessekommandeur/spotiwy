import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import login_required, apology, generatenumber
from random import randint
from API import searchsong

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

        # create room number
        roomnumber = randint(100000, 999999)
        while db.execute("SELECT * from rooms WHERE roomnumber = :roomnumber", roomnumber = roomnumber):
            roomnumber = randint(100000, 999999)

        # insert roomname into database
        db.execute("INSERT INTO rooms (roomnumber, userid) VALUES(:roomnumber, :userid)", userid = session["userid"],
        roomnumber=int(roomnumber))

        # TODO
        # Create room settings
        # give admin tag

        session["roomnumber"] = roomnumber

        # go to room
        return redirect("/room")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("host.html")



# @app.route("/room", methods=["GET", "POST"])
# @login_required
# def admin():

#     """Admin room"""

#     if request.method == "POST":



@app.route("/homepage", methods=["GET", "POST"])
def joinroom():

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
            return True #redirect("/room.html", roomnumber = userinput)
                # TODO
                # redirect to matching room

        else:
            return apology("this room currently does not exist.")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("homepage.html")

@app.route("/room", methods=["GET", "POST"])
def room():

    """room functions"""

    roomnumber = db.execute("SELECT roomnumber FROM rooms WHERE userid = :userid", userid = session["userid"])

    return render_template("room.html")



@app.route("/disband", methods=["GET"])
@login_required
def disband():

    """admin disband room"""

    #disbands and deletes room
    db.execute("DELETE FROM rooms WHERE userid = :userid", userid = session["userid"])

    # clear room cookies and log user out
    session.clear()

    return redirect("/")

@app.route("/disband", methods=["GET"])
def leave():

    """ user leaves room"""

    # clear visitors cookies
    session.clear()

    return redirect("/")

# @app.route("/like", methods=["GET"])
# def like():

#     """ like a song"""

#     likes = ("SELECT * FROM rooms WHERE roomnumber = :roomnumber AND songid = :songid", roomnumber = session["roomnumber"], songid =  )

#     db.execute("UPDATE rooms SET likes = :likes WHERE roomname = :roomname AND songid = :songid", likes = likes + 1,
#     roomname = session["roomname"], songid = )

# @app.route("/bin", methods=["GET"])
# def remove():

#     """remove song from list"""

#     db.execute("DELETE FROM rooms WHERE songid = :songid AND roomname = :roomname",  roomname = session["roomname"] , songid = )



@app.route("/add", methods=["GET", "POST"])
def add():

    """add new song to list"""

    if request.method == "POST":

        # get song information from spotify
        songinfo = searchsong(request.form.get("song"), 1, 0, "track")


        # store song information in database
        db.execute("INSERT INTO rooms (roomnumber, song, songid, artist, likes, userid) VALUES(:roomnumber, :song, :songid, :artist, :likes, :userid)",
        roomnumber = session["roomnumber"], song = songinfo[0]["track"], songid = songinfo[0]["songid"], artist = songinfo[0]["artist"], likes = 1,
        userid = session["userid"])

        return redirect("/room")

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

# @app.route("/searchdrpdwn", methods=["GET"])
# def drpdwn():

#     rel_songs = searchsong(request.args.get("song"), 5, 0, "track")
#     print(rel_songs)

