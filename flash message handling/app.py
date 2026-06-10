from flask import Flask, render_template, request, flash,url_for, redirect

app=Flask(__name__)
app.secret_key="my-secret-key"

@app.route("/")
def form():
    if request.method=="POST":
        name=request.form.get("name")
        if not name:
            flash("Name is required!", "error")
            return redirect(url_for("form")) 
        flash(f"Thanks, {name}! your feedback was saved")
        return render_template("thankyou.html")
    return render_template("form.html")

@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")