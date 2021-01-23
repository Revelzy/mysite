import flask
from flask import Flask


app = Flask(__name__, static_url_path='/static')


@app.route('/')
def main():
    return flask.render_template("main.html")


@app.route('/about')
def about():
    return flask.render_template("about.html")


@app.route('/licenses')
def licenses():
    return flask.render_template("licenses.html")


@app.route('/terms')
def terms():
    return flask.render_template("terms.html")


@app.route('/privacy')
def privacy():
    return flask.render_template("privacy.html")
    

if __name__ == '__main__':
	app.run(debug = True)