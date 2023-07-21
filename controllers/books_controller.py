from flask import render_template, Blueprint, request, redirect, jsonify
from models.book_list import *
from models.book import *

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
        book_title = request.form["title_of_book"]
        book_author = request.form["author_of_book"]
        book_genre = request.form["genre_of_book"]
        book_description = request.form["description"]
        book_id = len(books) + 1
        new_book = Book(book_title, book_author, book_genre, book_description, book_id)
        add_new_book(new_book)
        return redirect('/catalogue')

@books_blueprint.route("/catalogue/<int:book_id>", methods=['post', 'get'])
def book_detail(book_id):
     for book in books:
        if book.id == book_id:
            return render_template("book.jinja", title="book.title", books=books, book=book)
        
@books_blueprint.route("/catalogue/<int:book_id>/check", methods=['post', 'get'])
def check_out(book_id):
    book_checked_out = request.form.get("check_out")
    for book in books:
        if book.id == book_id:
            if book_checked_out == "on":
                book.check_out()
                return redirect('/catalogue')
    return redirect('/catalogue') 
        
@books_blueprint.route('/catalogue/delete', methods= ['POST'])
def remove_book():
        book_title = request.form['title']
        for book in books:
            if book_title == book.title:
                books.pop(books.index(book))
        return redirect('/catalogue')