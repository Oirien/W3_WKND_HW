from flask import render_template, Blueprint, request, redirect
from models.book_list import *

books_blueprint = Blueprint("Books", __name__)

@books_blueprint.route('/')
def home():
    return redirect('/home')

@books_blueprint.route("/home")
def index():
    return render_template("index.jinja", title="Edinburgh Central Library", books=books)

@books_blueprint.route("/catalogue")
def catalogue():
    return render_template("catalogue.jinja", title="Enjoy our book catalogue", books=books)

@books_blueprint.route("/catalogue", methods=['post'])
def add_book_to_catalogue():
        book_title = request.form("title_of_book")
        book_author = request.form("author_of_book")
        book_genre = request.form("genre_of_book")
        