# "Where To Go" site project

This is an interactive map of Moscow, where you can view outdoor activities with detailed descriptions and comments.

## Requirements

Operating system: Microsoft Windows 7 or higher. Python3 should be installed. Use command line utility `cmd.exe` to run Python3 scripts.

## Prerequisites

Use `pip` to install dependencies:
```bash
python -m pip install -r requirements.txt
```

## Installation

1.Create  `.env` file in project directory and define your environment variables:
**For developer mode:**

DEBUG=True

**For production mode:**

DEBUG=False
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
SECURE_HSTS_SECONDS=60
SECRET_KEY="you-secret_key"
SECURE_HSTS_INCLUDE_SUBDOMAINS=True
SECURE_HSTS_PRELOAD=True

2. Migrate the database
```bash
python manage.py migrate
```

3. Create superuser
```bash
python manage.py createsuperuser
```

## Launch the app

```bash
python manage.py runserver
```

Launch the [django admin site](https://127.0.0.1:8000/admin) and fill the database.

Launch the ["Where To Go" project stite](https://127.0.0.1:8000/) and fill the database.


## Meta

Vitaly Klyukin — [@delphython](https://t.me/delphython) — [delphython@gmail.com](mailto:delphython@gmail.com)

[https://github.com/delphython](https://github.com/delphython/)