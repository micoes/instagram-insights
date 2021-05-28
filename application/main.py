from flask import Flask
from flask import render_template
from flask import request

import scrape
import json

app = Flask("application")


@app.route("/", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        user_id = request.form["identifier"]
        user_access_token = request.form["token"]

        # an dieser Stelle einfügen, dass authentication.json nur erstellt wird, wenn "Remember me" angewählt wurde → if, else
        with open("data/authentication.json", "w", encoding="utf-8") as json_file:
            user_data = json.dumps({"user_id": user_id, "user_access_token": user_access_token}, indent=4)
            json_file.write(user_data)

        try:
            scrape.initial(user_id, user_access_token)
            return render_template("insights.html")
        except:
            return render_template("index.html")

    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
