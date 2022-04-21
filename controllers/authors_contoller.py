from flask import Blueprint, render_template, redirect, request
from repositories import author_repository
from models.author import Author

authors_blueprint = Blueprint("authors", __name__)

@authors_blueprint.route("/authors")
def authors():
    authors = author_repository.select_all()
    return render_template("authors/index.html", all_authors = authors)

@authors_blueprint.route("/authors/new", methods=['GET'])
def new_author():
    return render_template("authors/new.html")

@authors_blueprint.route("/authors", methods=['POST'])
def create_author():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    author = Author(first_name, last_name)
    author_repository.save(author)
    return redirect('/authors')

@authors_blueprint.route("/authors/<id>/edit", methods=['GET'])
def edit_author(id):
    author = author_repository.select(id)
    return render_template("authors/edit.html", author = author) 

@authors_blueprint.route("/authors/<id>", methods=['POST'])
def update_author(id):
    first_name = request.form['first_name']   
    last_name = request.form['last_name']
    author = Author(first_name, last_name, id)
    author_repository.update(author)
    return redirect("/authors")