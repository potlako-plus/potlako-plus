"""
Django settings for potlako project.

Generated by 'django-admin startproject' using Django 3.0.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import configparser
import os
import sys

from django.core.management.color import color_style

# from .logging import LOGGING
style = color_style()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

APP_NAME = 'potlako'
SITE_ID = 40

ETC_DIR = os.path.join('/etc/', APP_NAME)

LOGIN_REDIRECT_URL = 'home_url'

INDEX_PAGE = 'potlako-plus.bhp.org.bw:8000'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'o(^0$9zu2w5eby-^x&dd441d(@*#(+($can2uomfq%o(@p-fm+'

# KEY_PATH = os.path.join(ETC_DIR, 'crypto_fields')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', 'potlako-plus.bhp.org.bw', '127.0.0.1']

CONFIG_FILE = f'{APP_NAME}.ini'

CONFIG_PATH = os.path.join(ETC_DIR, CONFIG_FILE)
sys.stdout.write(style.SUCCESS(f'  * Reading config from {CONFIG_FILE}\n'))
config = configparser.ConfigParser()
config.read(CONFIG_PATH)

# EDC SMS configuration
BASE_API_URL = config['edc_sms']['base_api_url']

# email configurations
EMAIL_BACKEND = config['email_conf'].get('email_backend')
EMAIL_HOST = config['email_conf'].get('email_host')
EMAIL_USE_TLS = config['email_conf'].get('email_use_tls')
EMAIL_PORT = config['email_conf'].get('email_port')
EMAIL_HOST_USER = config['email_conf'].get('email_user')
EMAIL_HOST_PASSWORD = config['email_conf'].get('email_host_pwd')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_crypto_fields.apps.AppConfig',
    'django_extensions',
    'simple_history',
    'corsheaders',
    'django_js_reverse',
    'rest_framework',
    'django_q',
    'crispy_forms',
    'rest_framework.authtoken',
    'edc_action_item.apps.AppConfig',
    'edc_call_manager.apps.AppConfig',
    'edc_consent.apps.AppConfig',
    'edc_prn.apps.AppConfig',
    'edc_dashboard.apps.AppConfig',
    'edc_device.apps.AppConfig',
    'edc_lab.apps.AppConfig',
    'edc_locator.apps.AppConfig',
    'edc_reference.apps.AppConfig',
    'edc_metadata_rules.apps.AppConfig',
    'edc_model_admin.apps.AppConfig',
    'edc_navbar.apps.AppConfig',
    'edc_subject_dashboard.apps.AppConfig',
    'edc_label.apps.AppConfig',
    'edc_registration.apps.AppConfig',
    'edc_visit_schedule.apps.AppConfig',
    'edc_timepoint.apps.AppConfig',
    'edc_calendar.apps.AppConfig',
    'potlako_dashboard.apps.AppConfig',
    'potlako_follow.apps.AppConfig',
    'potlako_metadata_rules.apps.AppConfig',
    'potlako_reference.apps.AppConfig',
    'potlako_visit_schedule.apps.AppConfig',
    'potlako_prn.apps.AppConfig',
    'potlako_reports.apps.AppConfig',
    'potlako_subject.apps.AppConfig',
    'potlako.apps.EdcDataManagerAppConfig',
    'potlako.apps.EdcAppointmentAppConfig',
    'potlako.apps.EdcMetadataAppConfig',
    'potlako.apps.EdcBaseAppConfig',
    'potlako.apps.EdcProtocolAppConfig',
    'potlako.apps.EdcVisitTrackingAppConfig',
    'potlako.apps.AppConfig',
    'potlako.apps.EdcSyncAppConfig',
    'potlako.apps.EdcSyncFilesAppConfig',
    'potlako.apps.EdcFacilityAppConfig',
    'potlako.apps.EdcIdentifierAppConfig',
    'potlako.apps.EdcSmsAppConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'edc_dashboard.middleware.DashboardMiddleware',
    'edc_subject_dashboard.middleware.DashboardMiddleware',
]

ROOT_URLCONF = 'potlako.urls'

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

WSGI_APPLICATION = 'potlako.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
mysql_config = configparser.ConfigParser()
mysql_config.read(os.path.join(ETC_DIR, 'mysql.ini'))

HOST = mysql_config['mysql']['host']
DB_USER = mysql_config['mysql']['user']
DB_PASSWORD = mysql_config['mysql']['password']
DB_NAME = mysql_config['mysql']['database']
PORT = mysql_config['mysql']['port']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': HOST,  # Or an IP Address that your DB is hosted on
        'PORT': PORT,
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME':
     'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
     },
    {'NAME':
     'django.contrib.auth.password_validation.MinimumLengthValidator',
     },
    {'NAME':
     'django.contrib.auth.password_validation.CommonPasswordValidator',
     },
    {'NAME':
     'django.contrib.auth.password_validation.NumericPasswordValidator',
     },
]

REST_FRAMEWORK = {
    'PAGE_SIZE': 1,
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
}

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

LANGUAGES = (
    ('tn', 'Setswana'),
    ('en', 'English'),
    ('kck', 'Ikalanga'),
)

DATE_INPUT_FORMATS = ['%d-%m-%Y']

CELLPHONE_REGEX = '^[7]{1}[12345678]{1}[0-9]{6}$'
TELEPHONE_REGEX = '^[2-8]{1}[0-9]{6}$'

TIME_ZONE = 'Africa/Gaborone'

USE_I18N = True

USE_L10N = False

USE_TZ = True

# Django q configurations

Q_CLUSTER = {
    'name': 'edc_sms',
    'retry': 60,
    'orm': 'default',
}

SITE_CODE = '40'
DEFAULT_STUDY_SITE = '40'
REVIEWER_SITE_ID = 41

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'potlako', 'static')

# dashboards
DASHBOARD_URL_NAMES = {
    'subject_listboard_url': 'potlako_dashboard:subject_listboard_url',
    'screening_listboard_url': 'potlako_dashboard:screening_listboard_url',
    'endpoint_listboard_url': 'potlako_dashboard:endpoint_listboard_url',
    'data_manager_listboard_url': 'edc_data_manager:data_manager_listboard_url',
    'contact_listboard_url': 'edc_sms:contact_listboard_url',
    'subject_dashboard_url': 'potlako_dashboard:subject_dashboard_url',
    'potlako_follow_listboard_url': 'potlako_follow:potlako_follow_listboard_url',
    'potlako_navigation_listboard_url': 'potlako_follow:potlako_navigation_listboard_url',
    'potlako_investigation_listboard_url': 'potlako_follow:potlako_investigation_listboard_url',
    'verbal_consent_url': 'potlako_dashboard:verbal_consent_url'
}

LAB_DASHBOARD_URL_NAMES = {}

DASHBOARD_BASE_TEMPLATES = {
    'listboard_base_template': 'potlako/base.html',
    'contact_listboard_template': 'edc_sms/listboard.html',
    'dashboard_base_template': 'potlako/base.html',
    'data_manager_listboard_template': 'edc_data_manager/listboard.html',
    'potlako_follow_listboard_template': 'potlako_follow/follow_listboard.html',
    'potlako_navigation_listboard_template': 'potlako_follow/navigation_listboard.html',
    'potlako_investigation_listboard_template': 'potlako_follow/investigation_fu_listboard.html',
    'screening_listboard_template': 'potlako_dashboard/screening/listboard.html',
    'endpoint_listboard_template': 'potlako_dashboard/endpoint/listboard.html',
    'subject_listboard_template': 'potlako_dashboard/subject/listboard.html',
    'subject_dashboard_template': 'potlako_dashboard/subject/dashboard.html',
}

CRISPY_TEMPLATE_PACK = 'bootstrap3'
GIT_DIR = BASE_DIR

# edc_facility
HOLIDAY_FILE = os.path.join(BASE_DIR, 'holidays.csv')
COUNTRY = 'botswana'

PARENT_REFERENCE_MODEL1 = ''
PARENT_REFERENCE_MODEL2 = ''

COMMUNITIES = config['communities']

DEVICE_ID = config['edc_device'].get('device_id', '99')
DEVICE_ROLE = config['edc_device'].get('role')

EDC_SYNC_SERVER_IP = config['edc_sync'].get('server_ip')
EDC_SYNC_FILES_REMOTE_HOST = config['edc_sync_files'].get('remote_host')
EDC_SYNC_FILES_USER = config['edc_sync_files'].get('sync_user')
EDC_SYNC_FILES_USB_VOLUME = config['edc_sync_files'].get('usb_volume')
