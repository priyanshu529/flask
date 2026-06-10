from flask import Flask,request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, this is my first app"

@app.route("/about")
def about():
    return "This is the about page of my first app"

@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        return "Form submitted successfully!"
    else:
        return "you are only viewing the form"