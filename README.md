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

```bash
DEBUG=True  
SECRET_KEY="django-insecure-secret-key"  
ALLOWED_HOSTS = "127.0.0.1 localhost"
```  

**For production mode:**

```bash
DEBUG=False  
SECRET_KEY="django-insecure-secret-key"  
ALLOWED_HOSTS = "127.0.0.1 localhost yoursite.yourdomain.com"
```  

**DEBUG** - a boolean that turns on/off debug mode. One of the main features of debug mode is the display of detailed error pages. For production mode you should set it to `False`, for developer mode - `True`. The default in `settings.py` is `True`:
```bash
DEBUG = bool(strtobool(os.getenv("DEBUG", True)))
```
**ALLOWED_HOSTS** - a list of strings representing the host/domain names that this Django site can serve. For developer mode you should add your local ip addresses, for production mode you should add your production server ip address or dns name. All strings should be separated by spaces as shown above.  
**SECRET_KEY** - a secret key for a particular Django installation. This is used to provide cryptographic signing, and should be set to a unique, unpredictable value. The default in `settings.py` is `get_random_secret_key` - Django generating SECRET_KEY function, if `SECRET_KEY` is not present in `.env` file:
```bash
SECRET_KEY = os.getenv("SECRET_KEY", get_random_secret_key)
```  


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

JSON file in the example above should be in this format:
```sh
{
    "title": "Экскурсионный проект «Россия»",
    "imgs": [
        "https://url_to_your_image/1.jpg",
        "https://url_to_your_image/2.jpg",
        "https://url_to_your_image/3.jpg",
    ],
    "description_short": "Хотите увидеть Россию?",
    "description_long": "<p>Экскурсионный проект «Россия» проводит экскурсии по России ...</p>",
    "coordinates": {
        "lat": 55.753676,
        "lng": 37.641111
    }
}
```
JSON file is the data source with detailed information about the location, where  
`title` - title of the location;  
`imgs` - list of the location's images urls;  
`description_short` - short description of the location;  
`description_long` - long description of the location;  
`coordinates` - GPS coordinates of the location.  

## Meta

Vitaly Klyukin — [@delphython](https://t.me/delphython) — [delphython@gmail.com](mailto:delphython@gmail.com)

[https://github.com/delphython](https://github.com/delphython/)
