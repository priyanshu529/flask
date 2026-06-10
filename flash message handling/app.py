from flask import Flask, render_template, request, flash,url_for, redirect

app=Flask(__name__)
app.secret_key="my-secret-key"

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method=="POST":
        name=request.form.get("name")
        message=request.form.get("message")
        if not name:
            flash("Name is required!", "error")
            return redirect(url_for("form")) 
        flash(f"Thanks, {name}! your feedback was saved")
        return redirect(url_for("thankyou", name=name, message=message))
    return render_template("form.html")

@app.route("/thankyou")
def thankyou():
    name = request.args.get("name")
    message = request.args.get("message")
    return render_template("thankyou.html", name=name, message=message)