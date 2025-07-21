# Copilot Instructions for AI Agents

## Project Overview
- This is a Django monorepo containing several apps: `store`, `likes`, `tag`, `playground`, and `playground_app`.
- The main Django project configuration is in `storefront/` (settings, URLs, WSGI/ASGI entrypoints).
- Each app has its own `models.py`, `views.py`, `admin.py`, `migrations/`, and optional `templates/`.
- The project uses a `Pipfile` for dependency management and a single `db.sqlite3` for development.

## Key Patterns & Conventions
- **App Structure:** Each app is self-contained. Add new features by creating or updating models, views, and migrations within the relevant app.
- **Generic Relations:** The `likes` app uses Django's `GenericForeignKey` for the `LikedItem` model, allowing likes to be attached to any model.
- **Templates:** Place HTML templates in the `templates/` directory within each app (e.g., `playground_app/templates/hello.html`).
- **URL Routing:** App-specific URLs are defined in each app (e.g., `playground_app/urls.py`) and included in the main `storefront/urls.py`.
- **Admin Registration:** Register models for the Django admin in each app's `admin.py`.

## Developer Workflows
- **Install dependencies:**
  ```powershell
  pip install pipenv
  pipenv install
  ```
- **Run development server:**
  ```powershell
  pipenv run python manage.py runserver
  ```
- **Apply migrations:**
  ```powershell
  pipenv run python manage.py makemigrations
  pipenv run python manage.py migrate
  ```
- **Run tests:**
  ```powershell
  pipenv run python manage.py test
  ```

## Integration Points
- **User Model:** Uses Django's built-in `User` model for authentication and relations (see `likes/models.py`).
- **Content Types:** Uses Django's `ContentType` framework for generic relations.

## Examples
- To add a new feature, create a model in the relevant app, register it in `admin.py`, create a migration, and update views/templates as needed.
- To add a new app, use `python manage.py startapp <appname>` and include it in `storefront/settings.py`.

## References
- Main project config: `storefront/settings.py`, `storefront/urls.py`
- Example generic relation: `likes/models.py`
- Example template: `playground_app/templates/hello.html`

---

If any section is unclear or incomplete, please provide feedback for further refinement.
