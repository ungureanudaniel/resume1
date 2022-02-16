import os
import django_heroku
from decouple import config
import dj_database_url
from dotenv import load_dotenv




load_dotenv(verbose=True)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')
PRODUCTION = os.getenv('PRODUCTION')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG')

ALLOWED_HOSTS = ['aquatic-squirrel-brneqgx1m8wsjboge7sjq7hq.herokudns.com.', 'www.danielungureanuresume.site', 'danielungureanuresume.site']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'resumeapp',
    'storages',
]
SITE_ID = 1
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myresumeproject1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'myresumeproject1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': os.getenv('DATABASE_NAME'),

        'USER': os.getenv('DATABASE_USER'),

        'PASSWORD': os.getenv('DATABASE_PASSWORD'),

        'HOST': os.getenv('DATABASE_HOST'),

        'PORT': os.getenv('DATABASE_PORT'),
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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

#------------------AWS SETTINGS ---------------------------------------

if PRODUCTION == True:
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
    AWS_QUERYSTRING_AUTH = False

    AWS_S3_CUSTOM_DOMAIN='%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    AWS_S3_OBJECT_PARAMETERS = {
         'CacheControl': 'max-age=86400',
    }
    AWS_S3_FILE_OVERWRITE = False
    AWS_DEFAULT_ACL = 'public-read'
    AWS_LOCATION = 'static'
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'),
    ]
    STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
    AWS_S3_URL = '//s3.amazonaws.com/%s' % AWS_STORAGE_BUCKET_NAME
else:
    STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

    STATIC_URL = '/static/'
    # STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static')
    ]
    STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

#-----------------FILE STORAGE ----------------------------------------
DEFAULT_FILE_STORAGE = 'myresumeproject1.storages.MediaStore'





#----------------------------------------------------------------------


# STATIC_URL = '/static/'
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static'),
# ]

#----------------------MEDIA SETTINGS ----------------------------------
# MEDIA_URL = "media/"
# MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

#---------------------- SEND EMAIL SETTINGS ----------------------------
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_USE_TLS')
EMAIL_USE_TLS = os.getenv('EMAIL_PORT')
EMAIL_USE_SSL = os.getenv('EMAIL_USE_SSL')

CRISPY_TEMPLATE_PACK = 'bootstrap4'

django_heroku.settings(locals(), staticfiles=False)
