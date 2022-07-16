import os
from dotenv import load_dotenv
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!#y+jr)c0jd!h))mt=w@a07k5cmx47ls*#0hssnteiie*xod+5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#
load_dotenv('.env')
REST_API_URL = os.environ.get('REST_API_URL')
DB_DATABASE = os.environ.get('DB_DATABASE')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
REST_API_BEARER_TOKEN = os.environ.get('REST_API_BEARER_TOKEN')
CORS_ORIGIN_WHITELIST_ENV = os.environ.get('CORS_ORIGIN_WHITELIST_ENV')

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS_ENV').split()

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #
    'rest_framework',
    'corsheaders',
    'django_filters',
    'active_link',

    #
    'aboutus.apps.AboutusConfig',
    'accounts.apps.AccountsConfig',
    'api.apps.ApiConfig',
    'calories.apps.CaloriesConfig',
    'challenges.apps.ChallengesConfig',
    'dashboard.apps.DashboardConfig',
    'exports.apps.ExportsConfig',
    'goals.apps.GoalsConfig',
    'history.apps.HistoryConfig',
    'leaderboards.apps.LeaderboardsConfig',
    'pomodoros.apps.PomodorosConfig',
    'profiles.apps.ProfilesConfig',
    'steps.apps.StepsConfig',
    'water_intake.apps.WaterIntakeConfig',
    'weights.apps.WeightsConfig',
    'xps.apps.XpsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    #
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gesund_projekt.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [os.path.join(BASE_DIR, 'templates')],

        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'gesund_projekt.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    # 'default': {
    #   'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': {
        'ENGINE': 'mysql.connector.django',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': DB_DATABASE,
        'USER': DB_USER,
        'PASSWORD': DB_PASS,
        'OPTIONS': {
            'autocommit': True,
            'sql_mode': 'traditional',
        }
    }
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        # 'rest_framework.renderers.JSONRenderer',
        # 'rest_framework.permissions.AllowAny',
        # 'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.IsAdminUser',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
    ]
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#
# CORS_ORIGIN_WHITELIST = (
#     'http://localhost:8000',
#     'http://127.0.0.1:8000',
# )

CORS_ORIGIN_WHITELIST = CORS_ORIGIN_WHITELIST_ENV.split()

LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = 'login'

# EMAIL
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')
# EMAIL_USE_TLS = True
EMAIL_USE_SSL = True
