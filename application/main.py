from flask import Flask
from flask import render_template
from flask import request
import json

app = Flask("application")


@app.route("/", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        user_id = request.form["identifier"]
        user_access_token = request.form["token"]

        with open("data/authentication.json", "w", encoding="utf-8") as json_file:
            user_data = json.dumps({"user_id": user_id, "user_access_token": user_access_token}, indent=4)
            json_file.write(user_data)

        # an dieser Stelle Code erstellen, welcher scrape.py ausführt, um Daten der jeweils letzten 30 Tage mit der Datenbank abzugleichen
        # try / except verwenden, für den Fall, dass User ID oder Access Token falsch eingegeben werden (try → insights.html, except → index.html)

        return render_template("insights.html")

    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
