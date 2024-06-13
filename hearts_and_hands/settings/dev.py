from .base import BASE_DIR

DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db/dev.sqlite3',
    }
}


DOMAIN = "http://127.0.0.1:8000"
SECRET_KEY = 'django-insecure-%j6(p4+my8+$9akwa-%_n$o$q6zg&akgxl03#rucde!*-i-$-c'
