from pathlib import Path
import environ
import os

BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env(DEBUG=(bool, False), SECRET_KEY=(str, ""))
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

SECRET_KEY = env("SECRET_KEY")

DEBUG = env("DEBUG")
CORS_ALLOW_ALL_ORIGINS = True
ALLOWED_HOSTS = ["*"]
INSTALLED_APPS = [
    "corsheaders",
    #
    "grappelli",
    #
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "drf_yasg",
    #
    "django_app",
    "rest_framework",
]

MIDDLEWARE = [
    # глухой телефон - передача request из рук в руки
    "django_app.middleware.CustomCorsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    #
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "django_settings.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates", BASE_DIR / "frontend"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                #
                "django_app.context_processors.user_count",
            ],
        },
    },
]

WSGI_APPLICATION = "django_settings.wsgi.application"

if DEBUG:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        },
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "django_db",
            "USER": "django_usr",
            "PASSWORD": "Qwerty!1234$",
            "HOST": "127.0.0.1",
            "PORT": "5432",
        }
    }


if DEBUG:
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
            "LOCATION": "django_ram_cache_table",
        },
        "database_cache": {
            "BACKEND": "django.core.cache.backends.db.DatabaseCache",
            "LOCATION": "django_cache_table",
            "TIMEOUT": "120",
            "OPTIONS": {
                "MAX_ENTIES": 200,
            },
        },
    }
else:
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.redis.RedisCache",
            "LOCATION": "redis://127.0.0.1:6379",
        },
        "database_cache": {
            "BACKEND": "django.core.cache.backends.db.DatabaseCache",
            "LOCATION": "django_cache_table",
            "TIMEOUT": "120",
            "OPTIONS": {
                "MAX_ENTIES": 200,
            },
        },
    }


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "ru"
TIME_ZONE = "Etc/GMT-5"
USE_I18N = True
USE_TZ = True


STATIC_URL = "static/"
if not DEBUG:
    STATIC_ROOT = Path(BASE_DIR / "static")  # todo ENABLE FOR COLLECT STATIC
STATICFILES_DIRS = [
    Path(BASE_DIR / "static_external"),
    Path(BASE_DIR / "frontend/build/static"),
]

if DEBUG:
    STATICFILES_DIRS += (Path(BASE_DIR / "static"),)  # todo DISABLE FOR COLLECT STATIC

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {"DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.AllowAny"]}

# todo CELERY
CELERY_TIMEZONE = "Asia/Almaty"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 20 * 60
CELERY_BROKER_URL = "redis://localhost:6379"
# CELERY_BROKER_URL = "amqp://myuser:mypassword@localhost:5672/myvhost"
CELERY_RESULT_BACKEND = "redis://localhost:6379"
# 10 per/sec * 10 = 100 * 60 == 600 connection to db (timeout -> break)
# todo CELERY
