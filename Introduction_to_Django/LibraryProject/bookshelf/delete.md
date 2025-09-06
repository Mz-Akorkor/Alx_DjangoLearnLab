```python
from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()
# Expected output:
# (1, {'bookshelf.Book': 1})

# Confirm deletion
Book.objects.all()
# Expected output:
# <QuerySet []>