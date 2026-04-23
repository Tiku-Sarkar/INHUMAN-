from flask import Flask, render_template, redirect, session, request
from flask_mysqldb import MySQL
from werkzeug.security import check_password_hash, generate_password_hash

# creating the app obejct
app = Flask(__name__)
app.secret_key = "your_secret_key"


# creating the main rout
@app.route("/")
def home():
    return render_template("home.html")

# /creating the route for about page
@app.route("/about")
def about():
    return render_template("about.html")


# creating the route for programs page
@app.route("/programs")
def programs():
    return render_template("programs.html")


# creating the route for programs page
@app.route("/contact")
def contact():
    return render_template("contact.html")

# @app.route("/login")
# def login():
#     session['user'] = "test_user"
#     return "please login first"

# creating the route for buying page
is_logged = False
@app.route("/buy/<products>")
def buy(products):
    if 'user' not in  session:
        return redirect("/login")
    
    return f"you bought this {products}"

# creating route for signin page
@app.route("/signin", methods = ["POST","GET"])
def signup():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        hashed_password = generate_password_hash(password)
        cur = mysql.connection.cursor()

        cur.execute(
            "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
            (name, email, hashed_password)
        )

        mysql.connection.commit()
        cur.close()

        return "User registered successfully!"
    
    return render_template("signin.html")




# creating route for login page

@app.route("/login", methods = ["POST","GET"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cur.fetchone()
        if user:
            stored_password = user[3]  # password column

            if check_password_hash(stored_password, password):
                session['user'] = user[0]  # store user id
                return "Login successful!"
            else:
                return "Wrong password"
        else:
            return "User not found"

    return render_template("login.html")

# route for testing database
@app.route('/test-db')
def test_db():
    cur = mysql.connection.cursor()
    cur.execute("SELECT 1")
    return "Database connected!"


# getting configuration from database
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'sp_id*_4_d2y'
app.config['MYSQL_DB'] = 'inhuman'

mysql = MySQL(app)

if __name__ == "__main__":
    app.run(debug=True)