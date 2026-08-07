# FLASK_APP=portfolio/server.py FLASK_DEBUG=1 flask run

import os
from flask import Flask, request, render_template, redirect, url_for, abort

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/<string:page_name>")
def render_page(page_name):
    template_path = os.path.join(app.root_path, app.template_folder, page_name)
    if os.path.exists(template_path):
        return render_template(page_name)
    abort(404)


@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        print(data)
        # return render_template("thankyou.html")
        return redirect(url_for("render_page", page_name="thankyou.html"))
    else:
        return "Something went wrong. Please try again."
