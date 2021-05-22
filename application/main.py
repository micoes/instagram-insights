from flask import Flask
from flask import render_template

app = Flask("Analytics")


@app.route("/sign-in")
def instagram():
    return render_template("index.html", name="Michael")


@app.route("/analytics")
def test():
    return "success"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
