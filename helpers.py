import requests
import urllib.parse
import os
from cs50 import SQL
from random import randint

from flask import redirect, render_template, request, session
from functools import wraps

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


def generatenumber():

    """generates a random roomnumber"""

    # generate roomnumber
    roomnumber = randint(100000, 999999)

    while db.execute("SELECT * from rooms WHERE roomnumber = :roomnumber", roomnumber = roomnumber):
        roomnumber = randint(100000, 999999)

    return roomnumber

# def numbercheck(roomname):

    # """checks is user input is valid"""

    # # Ensure user enters 6 digit number
    # if not len(request.form.get("roomnumber")) == 6:
    #     return apology("should enter 6 digit number", 400)

    # # Ensure user enters digits only
    # if not request.form.get("roomnumber").isdigit():
    #     return apology("should enter digits only number", 400)

    # if not db.execute("SELECT * FROM rooms WHERE roomnumber = :roomnumber", roomnumber = roomnumber):
    #     return apology("room does not exist", 400)
