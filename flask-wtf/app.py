from flask import Flask, render_template, request, flash,url_for, redirect
from form import Registration

app=Flask(__name__)
app.secret_key="my-secret-key"

@app.route("/",methods=["GET", "POST"])
def register():
    form=Registration()
    if form.validate_on_submit():
        name=form.name.data
        email=form.email.data
        flash(f"Thanks for registering, {name}!")
        return redirect(url_for("success"))
    return render_template("register.html", form=form)

@app.route("/success")
def success():
    return render_template("success.html")