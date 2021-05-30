from flask import Flask
from flask import redirect
from flask import url_for
from flask import render_template
from flask import request

import scrape
import json
import os.path

app = Flask("application")


@app.route("/", methods=["GET", "POST"])
def login():
    if os.path.exists("data/authentication.json"):
        with open("data/authentication.json", "r") as json_file:
            access = json.load(json_file)

        user_access_token = access["user_access_token"]
        user_id = access["user_id"]

        scrape.instagram(user_id, user_access_token)

        return redirect(url_for("analysis"))

    else:
        if request.method == "POST":
            user_id = request.form["identifier"]
            user_access_token = request.form["token"]
            remember_me = request.form.get("checkbox")  # BadRequestKeyError mit request.form["checkbox"], wenn nicht angewählt → Unterschiede?

            try:
                scrape.instagram(user_id, user_access_token)

                if remember_me == "true":
                    with open("data/authentication.json", "w", encoding="utf-8") as json_file:
                        user_data = json.dumps({"user_id": user_id, "user_access_token": user_access_token}, indent=4)
                        json_file.write(user_data)
                else:
                    pass

                return redirect(url_for("analysis"))

            except TypeError:  # Falscheingabe von ID und/oder Token wird nicht erkannt → Fehler aufgrund?
                print("Ihre Eingabe konnte nicht verarbeitet werden.")
        else:
            return render_template("index.html")


@app.route("/insights")
def analysis():
    print("Hi Analysis!")
    return render_template("insights.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
