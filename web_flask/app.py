# save this as app.py
from flask import Flask, request, render_template
from markupsafe import escape

app = Flask(__name__)

SPORTS = ["Basketball", "Soccer", "Ultimate Frisbee"]

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", sports=SPORTS)


@app.route("/register", methods=["POST"])
def register():
    if not request.form.get("name") or request.form.get("sport") not in SPORTS:
        return render_template("failure.html")
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True)
