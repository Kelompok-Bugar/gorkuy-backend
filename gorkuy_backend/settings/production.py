from .base import BASE_DIR
import dj_database_url
import os

DATABASE_URL = os.getenv("DATABASE_URL")
CSRF_TRUSTED_ORIGINS = ['https://https://gorkuy.up.railway.app/']
# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
DATABASES = {
    'default': dj_database_url.config(default=DATABASE_URL, conn_max_age=1800)
}
