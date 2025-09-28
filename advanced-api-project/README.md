### API Endpoints (Generic Views)

- `GET /api/books/` → List all books (public)
- `GET /api/books/<id>/` → Retrieve single book (public)
- `POST /api/books/create/` → Create a new book (authenticated only)
- `PUT /api/books/<id>/update/` → Update a book (authenticated only)
- `DELETE /api/books/<id>/delete/` → Delete a book (authenticated only)

Permissions:
- Public users: can view books.
- Authenticated users: can create, update, and delete.