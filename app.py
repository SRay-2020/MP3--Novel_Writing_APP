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


@app.route("/get_chapters")
def get_chapters():
    chapters = list(mongo.db.chapters.find())
    return render_template("chapters.html", chapters=chapters)


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
        flash("Congratulations, Registration Has Been Successful")
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
    username = mongo.db.users.find_one(
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
            "description": request.form.get("book_description"),
            "created_by": session['user']
        }
        # Check if name in use
        existing_books = mongo.db.books.find_one(
                {"book_name":request.form.get("book_name").lower()})

        if existing_books:
            flash("Name already in use, please enter unique book name")
            return redirect(url_for(add_book))
            # Check if username already exists

        

        mongo.db.books.insert_one(book)
        flash("Book Successfully Added")
        return redirect(url_for("get_books"))

    characters = mongo.db.characters.find().sort("character_name", 1)
    return render_template("add_book.html", characters=characters)

@app.route("/edit_book/<book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    
    if request.method == "POST":
        submitb = {
            "book_name": request.form.get("book_name"),
            "genre": request.form.get("genre_name"),
            "author": request.form.get("author_name"),
            "characters": request.form.getlist("characters_list"),
            "description": request.form.get("book_description"),
            "created_by": session['user']
        }
        mongo.db.books.update({"_id": ObjectId(book_id)}, submitb)
        flash("Book Successfully Edited")


    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    characters = mongo.db.characters.find().sort("character_name", 1)
    return render_template(
        "edit_book.html", book=book, characters=characters)


@app.route("/delete_book/<book_id>")
def delete_book(book_id):
    mongo.db.books.remove({"_id": ObjectId(book_id)})
    flash("Book Successfully Deleted")
    return redirect(url_for("get_books"))


@app.route("/add_chapter", methods=["GET", "POST"])
def add_chapter():
    if request.method == "POST":
        chapter = {
            "chapter_name": request.form.get("chapter_name"),
            "outline": request.form.get("outline_name"),
            "author": request.form.get("author_name"),
            "sequence": request.form.get("sequence_name"),
            "book_name": request.form.get("book_name"),
            "author": session['user']
        }

        mongo.db.chapters.insert_one(chapter)
        flash("Chapter Successfully Added")
        return redirect(url_for("get_chapters"))

    books = mongo.db.books.find().sort("book_name", 1)
    return render_template("add_chapter.html", books=books)


@app.route("/edit_chapter/<chapter_id>", methods=["GET", "POST"])
def edit_chapter(chapter_id):
    
    if request.method == "POST":
        submit = {
            "chapter_name": request.form.get("chapter_name"),
            "outline": request.form.get("outline_name"),
            "author": request.form.get("author_name"),
            "sequence": request.form.get("sequence_name"),
            "book_name": request.form.get("book_name"),
            "author": session['user']
        }

        mongo.db.chapters.update({"_id": ObjectId(chapter_id)}, submit)
        flash("Chapter Successfully Edited")

    books = mongo.db.books.find().sort("book_name", 1)
    chapter = mongo.db.chapters.find_one({"_id": ObjectId(chapter_id)})
    characters = mongo.db.characters.find().sort("character_name", 1)
    return render_template(
        "edit_chapter.html", chapter=chapter, characters=characters, books=books)

@app.route("/delete_chapter/<chapter_id>")
def delete_chapter(chapter_id):
    mongo.db.chapters.remove({"_id": ObjectId(chapter_id)})
    flash("Chapter Successfully Deleted")
    return redirect(url_for("get_chapters"))






if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port = int(os.environ.get("PORT")),
            debug = True)