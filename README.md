# Storefront

A simple Django project that demonstrates a small storefront API with products, tags, and likes. The project is split into multiple apps (`store`, `tags`, `likes`, `playground`) and uses SQLite for local development.

## Overview

- `store`: product and related domain models
- `tags`: tagging support for products
- `likes`: user-like interactions
- `playground`: simple demo routes

## Run locally

1) Create the virtual environment and install dependencies

```
pipenv install
```

2) Activate the environment

```
pipenv shell
```

3) Run migrations

```
python manage.py migrate
```

4) Start the dev server

```
python manage.py runserver
```

Then open http://127.0.0.1:8000/ in your browser.