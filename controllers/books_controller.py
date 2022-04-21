from flask import Flask, Blueprint, render_template, redirect, request
from controllers.authors_contoller import new_author
from repositories import book_repository, author_repository
from models.book import Book
from models.author import Author

books_blueprint = Blueprint("books", __name__)

# RESTful CRUD Routes

# INDEX
# GET '/books'
@books_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", all_books = books)

# NEW
# GET '/books/new'
@books_blueprint.route("/books/new", methods=['GET'])
def new_book():
    # author = author_repository.select_all()
    return render_template("books/new.html", all_authors = author_repository.select_all())


# CREATE
# POST '/books'
@books_blueprint.route("/books", methods=['POST'])
def create_book():
        title = request.form['title']
        all_authors = author_repository.select_all()
        author_first_name = request.form['author_first_name']
        author_last_name = request.form['author_last_name']
        new_author = Author(author_first_name, author_last_name)
        author_status = False
        for author in all_authors:
            if author.first_name == new_author.first_name and author.last_name == new_author.last_name:
                new_author = author
                author_status = True
        if author_status == False:
            author_repository.save(new_author)
        year = request.form['year']
        book = Book(title, new_author, year)
        book_repository.save(book)
        return redirect('/books')


# SHOW
# GET '/books/<id>'
@books_blueprint.route("/books/<id>", methods=['GET'])
def show_book(id):
    book = book_repository.select(id)
    return render_template("books/show.html", book = book)

# EDIT
# GET '/tasks/<id>/edit'
@books_blueprint.route("/books/<id>/edit", methods=['GET'])
def edit_book(id):
    book = book_repository.select(id)
    authors = author_repository.select_all()
    return render_template("books/edit.html", book = book, all_authors = authors) 

# UPDATE
# PUT '/books/<id>'
@books_blueprint.route("/books/<id>", methods=['POST'])
def update_book(id):
    title = request.form['title']
    all_authors = author_repository.select_all()
    author_first_name = request.form['author_first_name']
    author_last_name = request.form['author_last_name']
    new_author = Author(author_first_name, author_last_name)
    author_status = False
    for author in all_authors:
        if author.first_name == new_author.first_name and author.last_name == new_author.last_name:
            new_author = author
            author_status = True
    if author_status == False:
        author_repository.save(new_author)    
    year = request.form['year']
    book = Book(title, new_author, year, id)
    book_repository.update(book)
    return redirect("/books")



# DELETE
# DELETE '/books/<id>'
@books_blueprint.route("/books/<id>/delete", methods=['POST'])
def delete_book(id):
    book_repository.delete(id)
    return redirect('/books')