import os
from dotenv import load_dotenv
load_dotenv()

DATABASES = {
    "default":{
        "ENGINE":"django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER":os.getenv("DB_USER"),
        "PASSWORD":os.getenv("DB_PASSWORD"),
        "HOST":"localhost",
        "PORT":"5433",
    }
}

INSTALLED_APPS = ["django_app"]

SECRET_KEY = 'django-insecure-hybrid-fastapi-django-key'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'