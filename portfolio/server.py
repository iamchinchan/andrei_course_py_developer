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


def write_to_database(data):
    db_path = os.path.join(app.root_path, "database.txt")
    file_exists = os.path.exists(db_path) and os.path.getsize(db_path) > 0

    with open(db_path, mode="a", encoding="utf-8") as database:
        if not file_exists:
            database.write("Name,Email,Subject,Message\n")

        name = data.get("name", "").strip()
        email = data.get("email", "")
        subject = data.get("subject", "")
        message = data.get("message", "")
        database.write(f'"{name}","{email}","{subject}","{message}"\n')

    return name or "Visitor"


@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            name = write_to_database(data)
            print(data)
            return redirect(
                url_for("render_page", page_name="thankyou.html", name=name)
            )
        except Exception as err:
            print(f"Error saving to database: {err}")
            return "Did not save to database"
    else:
        return "Something went wrong. Please try again."
