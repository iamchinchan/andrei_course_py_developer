from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/<string:page_name>")
def render_page(page_name):
    return render_template(page_name)


@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        print(data)
        # return render_template("thankyou.html")
        return redirect(url_for("render_page", page_name="thankyou.html"))
    else:
        return "Something went wrong. Please try again."
