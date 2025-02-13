# -*- coding: utf-8 -*-
# Django settings for mysite project.
# chi xel hamasha girifti mi?
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'django',                      # Or path to database file if using sqlite3.
        'USER': 'postgres',                      # Not used with sqlite3.
        'PASSWORD': 'postgres',                  # Not used with sqlite3.
        'HOST': '192.168.7.225',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',
        
    }
}


        #NAME': 'django',                      # Or path to database file if using sqlite3.
        #'USER': 'postgres',                      # Not used with sqlite3.
        #'PASSWORD': 'postgres',                  # Not used with sqlite3.
        #'HOST': '192.168.7.225',  
        
        #'NAME': 'django_db',                      # Or path to database file if using sqlite3.
        #'USER': 'django_user',                      # Not used with sqlite3.
        #'PASSWORD': 'django',                  # Not used with sqlite3.
        #'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Moscow'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ru-RU'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
#MEDIA_ROOT = r'D:\WORK\PYTHON\mysite\src\mysite\proc\media'
#STATIC_ROOT = r'D:/WORK/PYTHON/mysite/src/mysite/proc/static/'
MEDIA_ROOT = r'D:\WORK\PYTHON\proc\src\mysite\proc\media'
STATIC_ROOT = r'D:/WORK/PYTHON/proc/src/mysite/proc/static/'
 

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
STATIC_URL  = r'/static/'
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '3*0y6b09ale$0loyzcdeilr_g1aqfhm+ful+5-z(seu7l8dedk'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'mysite.middleware.RequireLogin.RequireLoginMiddleware',
)

LOGIN_REQUIRED_URLS = (
        r'/proc/(.*)$', 
        r'/proc/(.*)$',
    )

LOGIN_REQUIRED_URLS_EXCEPTIONS = (
        r'/proc/accounts(.*)$',
        r'/proc/static/css(.*)$',
        
    )

LOGIN_URL='/proc/accounts/login/'

ROOT_URLCONF = 'mysite.urls'
SESSION_EXPIRE_AT_BROWSER_CLOSE=True
SESSION_COOKIE_AGE = 600

TEMPLATE_DIRS = (
    #"D:/work/python/proc/src/mysite/proc/templates",
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'mysite.proc',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',    
    'django.contrib.messages.context_processors.messages',
    'django.contrib.auth.context_processors.auth',
    #'mysite.context_processors.user',
)

#from django.contrib.auth.context_processors.auth
