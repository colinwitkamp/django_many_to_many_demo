# Creative Culture - Project Management System - Code-writing task
 - Python3 - 3.9
 - Django - 3.2.3
 - djangorestframework
 - SQLite
## Task

```
a) There are two models in the system: the author model and the book model. A book can have multiple authors and an author can have multiple books. How to use the ORM to display a list of authors with indications of his last ten books?


b) Write a CRUD API for the book and author models: in the author model API, you need to add a route with a list of his books, and when you get the author by ID (detail view), you need to display a list of 10 of his latest books.


c) Create a search using the author's parameters (year of birth, full name, book title).
```

## Get Started
 - $ pipenv install
 - $ pipenv run python3 manage.py runserver

## Endpoints
 - POST /api/authors/
    `{ name, birth_year }`
 - GET /api/authors/
 - GET /api/authors/:pk/
 - PUT /api/authors/:pk/
    { name, birth_year }
 - DELETE /api/authors/:pk/


 - POST /api/books/
    `{ title, authors: [pk], published_at }`
 - GET /api/books/?`author_name`=...&`author_birth_year`=...&`title`=...
 - GET /api/books/:pk/
  
 - PUT /api/authors/:pk/
    `{ title, authors, published_at }`
 - DELETE /api/authors/:pk/