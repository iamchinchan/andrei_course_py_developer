from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/<username>/<int:post_id>")
def post(username=None, post_id=None):
    return render_template("index.html", name=username, post_id=post_id)


@app.route("/blog")
def blog():
    return "This is a simple blog!"


@app.route("/favicon.ico")
def favicon():
    return "😀"


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/company/about")
def Companyabout():
    return render_template("about.html")
