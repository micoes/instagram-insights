from flask import Flask
from flask import render_template
from flask import request

app = Flask("application")


@app.route("/", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        user_id = request.form["identifier"]
        user_access_token = request.form["token"]
        print(user_id)
        print(user_access_token)

        return render_template("insights.html")

    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
