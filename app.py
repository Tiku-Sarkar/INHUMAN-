from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = "your_secret_key"

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
    session['user'] = "test_user"
    return "please login first"

is_logged = False
@app.route("/buy/<products>")
def buy(products):
    if 'user' not in  session:
        return redirect("/login")
    
    return f"you bought this {products}"


@app.route("/signin", methods = ["POST","GET"])
def signup():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        return f"received {name} {email}"
    
    return render_template("signin.html")


if __name__ == "__main__":
    app.run(debug=True)