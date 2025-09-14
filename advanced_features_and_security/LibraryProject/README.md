# LibraryProject

This Django project is the initial project setup for the ALX lesson on Django.  

It includes:
- `manage.py` for executing commands like `runserver`
- `settings.py`, `urls.py` within the internal `LibraryProject/` configuration directory

## Next steps (Initial Setup)
- Add apps
- Create views and templates
- Define URL patterns

---

## Custom User Model
The project implements a custom user model (`CustomUser`) in the `bookshelf` app, extending `AbstractUser` with:
- `date_of_birth`
- `profile_photo`

This model is registered in the admin and replaces Django’s default `User`.

---

## Permissions and Groups Setup

### Custom Permissions
The `Book` model defines the following custom permissions:
- `can_view`: Can view book
- `can_create`: Can create book
- `can_edit`: Can edit book
- `can_delete`: Can delete book

### Groups
Use the Django admin to create groups and assign permissions:
- **Viewers** → `can_view`
- **Editors** → `can_view`, `can_create`, `can_edit`
- **Admins** → `can_view`, `can_create`, `can_edit`, `can_delete`

### Enforcing Permissions
In `bookshelf/views.py`, we use the `@permission_required` decorator:
- `book_list` → requires `can_view`
- `book_create` → requires `can_create`
- `book_edit` → requires `can_edit`
- `book_delete` → requires `can_delete`

### Testing
1. Create test users in Django admin.
2. Assign each user to a group (Viewer, Editor, Admin).
3. Log in as each user and try to access the book views.
   - Viewers should only see the book list.
   - Editors can add/edit books.
   - Admins can delete books as well.

# Security Enhancements

## Settings
- `DEBUG = False`, restricted `ALLOWED_HOSTS`
- `SECURE_BROWSER_XSS_FILTER`, `X_FRAME_OPTIONS`, `SECURE_CONTENT_TYPE_NOSNIFF`
- Secure cookies: `CSRF_COOKIE_SECURE`, `SESSION_COOKIE_SECURE`

## Templates
- All forms use `{% csrf_token %}`

## Views
- ORM queries used instead of raw SQL to prevent injection
- Basic input validation on form fields

## Content Security Policy (CSP)
- Configured via `django-csp` middleware
- Restricts scripts, styles, and images to safe sources