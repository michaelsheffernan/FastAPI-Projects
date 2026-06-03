# FastAPI Projects
A collection of backend API projects built with FastAPI and Pydantic. Each project demonstrates REST API design, data validation, and HTTP request handling.

# Projects

Books API
A fully functional REST API for a book database, built while learning FastAPI fundamentals.
Endpoints:

GET /books — return all books
GET /books/{book_id} — return book by ID
GET /books/ — filter books by rating (query parameter)
GET /books/publish/ — filter books by published date (query parameter)
POST /create-book — create a new book
PUT /books/update_book — update an existing book
DELETE /books/{book_id} — delete a book by ID

Technical details:

Separate Book class and BookRequest Pydantic model — clean separation between data storage and API input validation
Field validation with min/max length, gt/lt constraints
Path and Query parameters with validation
HTTP status codes throughout (200, 201, 204, 404)
Custom OpenAPI schema examples

Research Paper Database
A research paper management API with a partial HTML and JavaScript frontend.
Endpoints:

GET /papers — return all papers
GET /papers/{author}/ — search by author (path parameter)
GET /papers/publish/ — search by publish date (query parameter)
POST /create_paper — create a new paper
PUT /papers/update_paper — update an existing paper

Frontend:

Single page HTML and CSS application with show/hide sections
JavaScript fetch() calls connecting to FastAPI endpoints
Dark theme UI with forms for create, update, and search operations
*NOTE: front-end is incomplete and must be updated.

Technical details:

Pydantic BaseModel with field validation
Paper class separate from PaperRequest model
Error handling with HTTPException and 404 responses

Concepts Covered

REST API design and HTTP methods
Pydantic data validation and BaseModel
Path parameters, Query parameters, and request bodies
HTTP status codes and error handling
Connecting a JavaScript frontend to a Python backend via fetch()
FastAPI automatic OpenAPI documentation

# How to Run
bashpip install fastapi uvicorn pydantic
uvicorn books2:app --reload
uvicorn "Research Paper":app --reload
