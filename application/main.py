from flask import Flask
from flask import redirect
from flask import url_for
from flask import render_template
from flask import request

import module
import requests
import json
import os.path

app = Flask("application")


@app.route("/", methods=["GET", "POST"])
def login():
    if os.path.exists("data/authentication.json"):
        with open("data/authentication.json", "r") as json_file:
            authentication = json.load(json_file)

        user_access_token = authentication["user_access_token"]
        user_id = authentication["user_id"]

        module.scraping(user_id, user_access_token)

        return redirect(url_for("analysis"))

    else:
        if request.method == "POST":
            user_id = request.form["identifier"]
            user_access_token = request.form["token"]
            remember_me = request.form.get("checkbox")

            try:
                module.scraping(user_id, user_access_token)

                if remember_me == "true":
                    with open("data/authentication.json", "w", encoding="utf-8") as json_file:
                        user_data = json.dumps({"user_id": user_id, "user_access_token": user_access_token}, indent=4)
                        json_file.write(user_data)
                else:
                    pass

                return redirect(url_for("analysis"))

            except requests.exceptions.RequestException as e:
                raise SystemExit(e)
        else:
            return render_template("index.html")


@app.route("/insights", methods=["GET", "POST"])
def analysis():
    with open("data/archive.json", "r") as json_file:
        archive = json.load(json_file)

    if request.method == "POST":
        start_date = request.form["start_date"]
        end_date = request.form["end_date"]

        follower, follower_evolution, impressions, reach = module.filtering(start_date, end_date)

        return render_template("insights.html",
                               username=archive["username"],
                               biography=archive["biography"][:75],
                               follower=follower,
                               follower_evolution=follower_evolution,
                               impressions=impressions,
                               reach=reach)

    else:
        start_date = archive["data"][0]["values"][0]["end_time"]
        end_date = archive["data"][0]["values"][-1]["end_time"]

        follower, follower_evolution, impressions, reach = module.filtering(start_date, end_date)

        return render_template("insights.html",
                               username=archive["username"],
                               biography=archive["biography"][:75],
                               follower=follower,
                               follower_evolution=follower_evolution,
                               impressions=impressions,
                               reach=reach)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
