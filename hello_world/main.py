from flask import Flask
from flask import render_template

app = Flask("Hello")


@app.route('/hello')
def instagram():
    return render_template('index.html', name="Michael")


@app.route("/tescht")
def test():
    return "success"


if __name__ == "__main__":
    app.run(debug=True, port=5000)