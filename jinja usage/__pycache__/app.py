from flask import Flask,render_template, request

app=Flask(__name__)

@app.route("/")
def profile():
    subjects=['maths','chemistry','physics']
    return render_template("profile.html",
    name="Priyanshu",
    is_topper=True,
    subjects=subjects
    )

if __name__ == "__main__":
    app.run(debug=True)