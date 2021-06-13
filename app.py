import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

@app.route("/")
@app.route("/get_books")
def get_books():
    books = list(mongo.db.books.find())
    return render_template("books.html", books=books)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Check Username Already in use
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("User already exists - Please select unique Username")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password" : generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # Put User into session using Cookie
        session["user"] = request.form.get("username").lower()
        flash("Congratulations, Registration Has Been Sucessful")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Check if username already exists
        existing_user = mongo.db.users.find_one(
            {"username":request.form.get("username").lower()})

        if existing_user:
            # match password to hash
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
                        
            else:
                # Password does not match stored
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else: 
            # Username not registered
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    # Remove user from session Cookie
    flash("You have been successfully logged out")
    session.pop("user")
    return redirect(url_for("login"))



@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Retrieve users username from database
    usernamme = mongo.db.users.find_one(
        {"username": session['user']})["username"]
    return render_template("profile.html", username=username)


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        book = {
            "book_name": request.form.get("book_name"),
            "genre": request.form.get("genre_name"),
            "author": request.form.get("author_name"),
            "characters": request.form.getlist("characters_list"),
            # "created_by": session['user']
        }
        mongo.db.books.insert_one(book)
        flash("Book Successfully Added")
        return redirect(url_for("get_books"))

    characters = mongo.db.characters.find().sort("character_name", 1)
    return render_template("add_book.html", characters=characters)



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port = int(os.environ.get("PORT")),
            debug = True)