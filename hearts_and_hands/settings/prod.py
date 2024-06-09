from .base import BASE_DIR
from decouple import config

DEBUG = True
ALLOWED_HOSTS = ["3hf.ngo", "www.3hf.ngo",]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db/prod.sqlite3',
    }
}
DOMAIN = config("DOMAIN")
SECRET_KEY = config("SECRET_KEY")
