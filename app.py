import os
from functools import wraps
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


# app name
@app.errorhandler(404)
# inbuilt function which takes error as parameter
def not_found(e):
    # defining function
    return render_template("404.html")


def login_required(f):
    @wraps(f)
    # https://flask.palletsprojects.com/en/2.0.x/patterns/viewdecorators/#login-required-decorator
    # USER MUST BE LOGGED IN
    def decorated_function(*args, **kwargs):
        if "user" not in session:
            flash("Please Login to view page")
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


@app.route("/")
@app.route("/get_books")
def get_books():
    books = list(mongo.db.books.find())
    notes = list(mongo.db.notes.find().distinct("note_text"))
    return render_template("books.html", books=books, notes=notes)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    chapters = list(mongo.db.chapters.find({"$text": {"$search": query}}))
    notes = list(mongo.db.notes.find().distinct("note_text"))
    return render_template("profile.html", notes=notes, chapters=chapters)


@app.route("/get_chapters")
@login_required
def get_chapters():
    # SORT CHAPTERS BY A-Z SEQUENCE
    # https://www.tutorialspoint.com/mongodb/mongodb_sort_record.htm?fbclid=IwAR0UYkyl4zG_r4a7phaatoSmqkGZSZi41frbj3cbozDqOJp4APY1YKSc7WY
    chapters = list(mongo.db.chapters.find().sort("sequence", 1))
    notes = list(mongo.db.notes.find().distinct("note_text"))
    return render_template("chapters.html", chapters=chapters, notes=notes)


@app.route("/get_notes")
def get_notes():
    notes = list(mongo.db.notes.find().distinct("note_text"))
    return render_template("notepad.html", notes=notes)


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
            "password": generate_password_hash(request.form.get("password"))
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
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Ensure password matches
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # Invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # User not registered
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    # Remove user from session Cookie
    flash("You have been successfully logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/profile/<username>", methods=["GET", "POST"])
@login_required
def profile(username):
    if session['user'] == username:
        # Retrieve user's username from database
        username = mongo.db.users.find_one(
            {"username": session['user']})["username"]
        # Show count of own books and chapters to user
        booknum = mongo.db.books.count({'user': username})
        chapnum = mongo.db.chapters.count({'user': username}),
        # books = list(mongo.db.books.find().sort("book_name", 1)),
        books = list(mongo.db.books.find())
        chapters = list(mongo.db.chapters.find())
        notes = list(mongo.db.notes.find().distinct("note_text"))

        return render_template(
            "profile.html", username=username,
            booknum=booknum, chapnum=chapnum,
            notes=notes, books=books, chapters=chapters)


@app.route("/add_book", methods=["GET", "POST"])
@login_required
def add_book():
    if request.method == "POST":
        # Check if username already exists
        existing_book = mongo.db.books.find_one(
                {"book_name": request.form.get("book_name")})

        if existing_book:
            flash("Name already in use, please enter unique book name")
            return redirect(url_for("add_book"))

        book = {
            "book_name": request.form.get("book_name"),
            "genre": request.form.get("genre_name"),
            "author": request.form.get("author_name"),
            "description": request.form.get("book_description"),
            "created_by": session['user']
        }
        mongo.db.books.insert_one(book)

        flash("Book Successfully Added")
        return redirect(url_for("get_books"))

    notes = list(mongo.db.notes.find().distinct("note_text"))
    return render_template("add_book.html", notes=notes)


@app.route("/edit_book/<book_id>", methods=["GET", "POST"])
@login_required
def edit_book(book_id):

    if request.method == "POST":
        submitb = {
            "book_name": request.form.get("book_name"),
            "genre": request.form.get("genre_name"),
            "author": request.form.get("author_name"),
            "description": request.form.get("book_description"),
            "created_by": session['user']
        }
        mongo.db.books.update({"_id": ObjectId(book_id)}, submitb)
        flash("Book Successfully Edited")

    notes = list(mongo.db.notes.find().distinct("note_text"))
    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    return render_template(
        "edit_book.html", book=book, notes=notes)


@app.route("/delete_book/<book_id>")
@login_required
def delete_book(book_id):
    mongo.db.books.remove({"_id": ObjectId(book_id)})
    flash("Book Successfully Deleted")
    return redirect(url_for("get_books"))


@app.route("/add_chapter", methods=["GET", "POST"])
@login_required
def add_chapter():
    if request.method == "POST":
        chapter = {
            "chapter_name": request.form.get("chapter_name"),
            "outline": request.form.get("outline_name"),
            "sequence": request.form.get("sequence_name"),
            "book_name": request.form.get("book_name"),
            "author": session['user']
        }

        mongo.db.chapters.insert_one(chapter)
        flash("Chapter Successfully Added")
        return redirect(url_for("get_chapters"))

    books = mongo.db.books.find().sort("book_name", 1)
    notes = list(mongo.db.notes.find().distinct("note_text"))
    return render_template("add_chapter.html", books=books, notes=notes)


@app.route("/edit_chapter/<chapter_id>", methods=["GET", "POST"])
@login_required
def edit_chapter(chapter_id):

    if request.method == "POST":
        submit = {
            "chapter_name": request.form.get("chapter_name"),
            "outline": request.form.get("outline_name"),
            "sequence": request.form.get("sequence_name"),
            "book_name": request.form.get("book_name"),
            "author": session['user']
        }

        mongo.db.chapters.update({"_id": ObjectId(chapter_id)}, submit)
        flash("Chapter Successfully Edited")

    books = mongo.db.books.find().sort("book_name", 1)
    chapter = mongo.db.chapters.find_one({"_id": ObjectId(chapter_id)})
    notes = list(mongo.db.notes.find().distinct("note_text"))
    return render_template(
        "edit_chapter.html", chapter=chapter, books=books,
        notes=notes)


@app.route("/delete_chapter/<chapter_id>")
@login_required
def delete_chapter(chapter_id):
    mongo.db.chapters.remove({"_id": ObjectId(chapter_id)})
    flash("Chapter Successfully Deleted")
    return redirect(url_for("get_chapters"))


@app.route("/add_note", methods=["GET", "POST"])
@login_required
def add_note():
    if request.method == "POST":
        note = {
            "note_text": request.form.get("note_text"),
            "author": session['user']
        }

        mongo.db.notes.insert_one(note)

        flash("Note Successfully Added")
        return redirect(url_for("get_notes"))

    notes = list(mongo.db.notes.find_one(
        {"author": session['user']}).distinct("note_text"))
    return render_template("notepad.html", notes=notes)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
