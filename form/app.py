from flask import Flask,render_template, request

app=Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/submit",methods=["POST"])
def submit():
    username=request.form.get("username")
    password=request.form.get("password")

    # if username=="priyanshu" and password=="123":
    #     return render_template("welcome.html")
    # else:
    #     return "Invalid login"
    valid_user={"priyanshu":"123","john":"456","alice":"789"}
    if username in valid_user and password==valid_user[username]:
        return render_template("welcome.html", username=username)
    else:
        return "Invalid login"

if __name__=="__main__":
    app.run(debug=True)