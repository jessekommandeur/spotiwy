@app.route("/connect", methods=["GET", "POST"])
@login_required
def connect2():

    """"""

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