# Creative Culture - Project Management System - Code-writing task
 - Python3 - 3.9
 - Django - 3.2.3
 - djangorestframework
 - SQLite
 
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