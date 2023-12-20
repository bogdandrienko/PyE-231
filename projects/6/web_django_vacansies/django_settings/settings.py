"""
django_settings/settings.py - все настройки проекта django
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-w4h6l+a2=r*0$#@+0360^y8+0lx@)y3&@in&=kup3i!+5$nh9="

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_app",
    "django_profiles",
]

MIDDLEWARE = [
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
        # массив, который отвечает за пути с html-файлами
        "DIRS": [
            BASE_DIR / "templates",
            # BASE_DIR/'frontend/public',  # react - js library
            # BASE_DIR/'frontend/build',  # vue - js framework
        ],
        # шаблоны, могут находится в приложениях
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "django_settings.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

"""
# postgresql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # psycopg2
        'NAME': 'dbname',
        'USER': 'dbuser',
        'PASSWORD': 'dbpassword',
        'HOST': '127.0.0.1',  # localhost
        'PORT': '5432',
    }
}
"""

CACHES = {
    # Кэш в оперативной памяти
    # + скорость
    # - дорого, нельзя вынести на другой сервер
    # TODO - ВЫСОКО ПРИОРИТЕТНЫЕ ДАННЫЕ (домашняя страница)
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    },
    # Кэш в базе данных
    # + дешево
    # - средняя скорость, находится там же, где и основная база
    # вычисления(computing) - у учеников есть много критериев, оценки, успеваемость... Клас.руку нужно час высчитывать лучшего ученика. Лучший - Нурдаулет.
    # TODO - НИЗКО ПРИОРИТЕТНЫЕ ДАННЫЕ (страница с контактами)
    "special": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "cache_table",
        "TIMEOUT": "120",
        "OPTIONS": {
            # "MAX_ENTIES": 200,
        },
    },
    # Внешний кэш
    # + масштабируемость
    # - сложнее
    # 'extra': {
    #     'BACKEND': 'django_redis.cache.RedisCache',
    #     'LOCATION': env("REDIS_LOCATION")',
    #     'TIMEOUT': '240',
    #     'OPTIONS': {
    #         # "MAX_ENTIES": 200,
    #         "PASSWORD": "12345qwertY!"
    #     }
    # }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = [
    Path(BASE_DIR, "static"),
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
