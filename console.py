from models.book import Book
from models.author import Author
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

author1 = Author("Mark", "Twain")
author_repository.save(author1)

author2 = Author("Harper", "Lee")
author_repository.save(author2)

book1 = Book("The Adventures of Tom Sawyer", author1, 1876)
book_repository.save(book1)
book2 = Book("Adventures of Huckleberry Finn", author1, 1884)
book_repository.save(book2)
book3 = Book("To Kill a Mockingbird", author2, 1960)
book_repository.save(book3)
