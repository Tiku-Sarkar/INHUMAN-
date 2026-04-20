from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/programs")
def programs():
    return render_template("programs.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/login")
def login():
    return "please login first"

is_logged = False
@app.route("/buy/<products>")
def buy(products):
    if not is_logged:
        return redirect("/login")
    
    return f"you bought this {products}"


if __name__ == "__main__":
    app.run(debug=True)