from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", number=1)

@app.route("/goodbye")
def goodbye():
    return "Goodbye!"

@app.route("/again")
def again():
    return "again"