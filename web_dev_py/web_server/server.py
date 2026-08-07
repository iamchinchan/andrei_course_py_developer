# FLASK_APP=web_dev_py/web_server/server.py FLASK_DEBUG=1 flask run

from flask import Flask, render_template, send_from_directory, url_for

app = Flask(__name__)
print(app)
print(f"{app.name}")
print(f"__name__ is {__name__}")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/<username>/<int:post_id>")
def post(username=None, post_id=None):
    return render_template("user_post.html", name=username, post_id=post_id)


@app.route("/blog")
def blog():
    return "This is a simple blog!"


@app.route("/favicon.ico")
def favicon():
    return "😀"


# @app.route("/about")
# def about():
#     return render_template("about.html")


@app.route("/bio")
def about():
    return render_template("about.html")


@app.route("/test_url")
def test_url():
    # Demonstrating url_for for static files and routes
    static_url = url_for("static", filename="style.css")
    about_url = url_for("about")
    return f"Static File URL: {static_url} <br> About Route URL: {about_url}"


@app.route("/company/about")
def Companyabout():
    return render_template("about.html")
