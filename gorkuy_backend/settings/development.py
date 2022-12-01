from .base import BASE_DIR

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
DATABASES = {
    'sqlite3': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'postgresql':{
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'gorkuy',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

DEFAULT_DATABASE = 'sqlite3'
DATABASES['default'] = DATABASES[DEFAULT_DATABASE] 