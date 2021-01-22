import flask
from flask import Flask


app = Flask(__name__)


@app.route('/me')
def me():
    return "КУХТА"


@app.route('/')
def main():
    return flask.render_template("main.html")


@app.route('/kozinov')
def kozinov():
    return "istorichka lubit Kozinova"


if __name__ == '__main__':
	app.run(debug = True)