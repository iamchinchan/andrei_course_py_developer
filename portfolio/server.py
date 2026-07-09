from flask import Flask, request, render_template, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/<string:page_name>")
def render_page(page_name):
    return render_template(page_name)
