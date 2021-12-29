# "Where To Go" site project

This is an interactive map of Moscow, where you can view outdoor activities with detailed descriptions and comments.

## Requirements

Python3 should be installed. Use command line utility `cmd.exe` to run Python3 scripts.

## Prerequisites

Use `pip` to install dependencies:
```bash
python -m pip install -r requirements.txt
```

## Installation

1. Create  `.env` file in project directory and define your environment variables:  

**For developer mode:**

DEBUG=True  
SECRET_KEY="django-insecure-secret-key"  
ALLOWED_HOSTS = "127.0.0.1 localhost"  

**For production mode:**

DEBUG=False  
SECRET_KEY="django-insecure-secret-key"  
ALLOWED_HOSTS = "127.0.0.1 localhost yoursite.yourdomain.com"  

**DEBUG** - a boolean that turns on/off debug mode. One of the main features of debug mode is the display of detailed error pages.  
**ALLOWED_HOSTS** - a list of strings representing the host/domain names that this Django site can serve.  
**SECRET_KEY** - a secret key for a particular Django installation. This is used to provide cryptographic signing, and should be set to a unique, unpredictable value.  


2. Migrate the database
```bash
python manage.py migrate
```

3. Create superuser
```bash
python manage.py createsuperuser
```

## Launch the site

```bash
python manage.py runserver
```

Launch the [django admin site](https://delphython.pythonanywhere.com/admin) and fill the database.

Launch the ["Where To Go" project stite](https://delphython.pythonanywhere.com/) and fill the database.

To load place's data from json file run script:
```bash
python manage.py load_place http://your_site/your_json_file.json
```

## Meta

Vitaly Klyukin — [@delphython](https://t.me/delphython) — [delphython@gmail.com](mailto:delphython@gmail.com)

[https://github.com/delphython](https://github.com/delphython/)
