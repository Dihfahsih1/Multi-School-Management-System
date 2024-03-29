
import os
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'twq$^$5g%j7=k06fglkifr@r)g8an#kx&!v*3a=_t#2d0r3ogd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'schools.apps.SchoolsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'widget_tweaks',

]

BOOTSTRAP4 = {
    'include_jquery': True,
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'Education.middleware.LoginRequiredMiddleware',
]

ROOT_URLCONF = 'Education.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'Education.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'schools',
        'USER': 'postgres',
        'PASSWORD': 'canon',
        'HOST': 'localhost'
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
LANGUAGES = (
    ('en', _('English')),
    ('ca', _('Catalan')),
    ('fr', _('French')),
    ('es', _('Spanish')),
    ('sw', _('Swahili')),
    ('zh-CN', _('Chinese')),
    ('ar', _('Arabic')),

)

# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

AUTH_USER_MODEL = 'schools.User'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGIN_REDIRECT_URL = '/en-us/schools/index/'
LOGOUT_REDIRECT_URL = '/en-us/schools/login_user/'
LOGIN_URL = '/en-us/schools/login_user/'

LOGIN_EXEMPT_URLS = (
    '/en-us/schools/logout_user/',
    '/en-us/schools/reset-password/',
    '/en-us/schools/reset-password/done/',
    '/en-us/schools/reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/',
    '/en-us/schools/reset-password/complete/',
)

EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025

IMPORT_EXPORT_USE_TRANSACTIONS = True

SESSION_EXPIRE_SECONDS = 1200  # 1200 seconds = 10 minutes

SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True

ADMIN_REDIRECT_URL = '/index/'
