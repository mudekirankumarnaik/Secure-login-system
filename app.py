from flask import Flask, render_template
from flask import request, redirect
from flask import session, url_for

import sqlite3
import bcrypt

app = Flask(__name__)

app.secret_key = "secure_secret_key"

# =====================================================
# DATABASE SETUP
# =====================================================

connection = sqlite3.connect(
    "users.db",
    check_same_thread=False
)

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")

connection.commit()

# =====================================================
# HOME
# =====================================================

@app.route("/")
def home():
    return redirect("/login")

# =====================================================
# REGISTER
# =====================================================

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        # Basic Input Validation
        if len(username) < 3 or len(password) < 5:
            return "Username or Password too short"

        # Password Hashing
        hashed_password = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        )

        try:

            cursor.execute(
                "INSERT INTO users(username, password) VALUES(?, ?)",
                (username, hashed_password)
            )

            connection.commit()

            return redirect("/login")

        except:
            return "User already exists"

    return render_template("register.html")

# =====================================================
# LOGIN
# =====================================================

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        # SQL Injection Protected Query
        cursor.execute(
            "SELECT * FROM users WHERE username=?",
            (username,)
        )

        user = cursor.fetchone()

        if user:

            stored_password = user[2]

            if bcrypt.checkpw(
                password.encode("utf-8"),
                stored_password
            ):

                session["username"] = username

                return redirect("/dashboard")

        return "Invalid Username or Password"

    return render_template("login.html")

# =====================================================
# DASHBOARD
# =====================================================

@app.route("/dashboard")
def dashboard():

    if "username" in session:

        return render_template(
            "dashboard.html",
            username=session["username"]
        )

    return redirect("/login")

# =====================================================
# LOGOUT
# =====================================================

@app.route("/logout")
def logout():

    session.pop("username", None)

    return redirect("/login")

# =====================================================
# RUN APP
# =====================================================

if __name__ == "__main__":
    app.run(debug=True)
