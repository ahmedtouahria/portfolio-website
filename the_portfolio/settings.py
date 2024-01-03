import os
from pathlib import Path
from decouple import config,Csv
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY =config("SECRET_KEY")
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False if config("DEBUG",False) == "False" else True

ALLOWED_HOSTS = config("ALLOWED_HOSTS",cast=Csv())


CSRF_TRUSTED_ORIGINS = [f"http://{host}" for host in ALLOWED_HOSTS] + [f"https://{host}" for host in ALLOWED_HOSTS]

FILE_UPLOAD_MAX_MEMORY_SIZE = 25 * 1024 * 1024  # 25 MB in bytes

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portfolio',
    'constance',
    'constance.backends.database',
    "autoslug",
    "ckeditor"
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'the_portfolio.urls'

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

WSGI_APPLICATION = 'the_portfolio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'


CONSTANCE_ADDITIONAL_FIELDS = {
    'image_field': ['django.forms.ImageField', {}],
    'file_field': ['django.forms.FileField', {}],

    'api_field': ['django.forms.JSONField', {
    }],
    'email_field': ['django.forms.EmailField', {}],
}

CONSTANCE_CONFIG = {
    'name': ('Creative', 'Nom de votre entreprise'),
    'CV': ('', 'Your CV',"file_field"),

    'job_title': ('Scrum Master & Backend developer', 'Nom de votre emploie'),
    'hero_message': ('Hi, I’m Nilsa Brown and I am creative web & app developer who dream making the world better place by creating captivating products.', 'Hero message' ),
    'description': ('Description', "pas la peine d'expliquer"),
    'meta_description': ('', "Description pour les moteurs de recherches"),
    'logo': ("", "Le logo de l'entreprise", 'image_field'),
    'theme_color': ('#8dc04d', "couleur du theme"),
    'brand_url': ('https://www.creators.cc', "URL du site"),
    'about_image': ("", "L'image de la page à propos", 'image_field'),
    'mail': ('creative@creative.com', 'votre mail pro'),
    'phone': ('+213770000000', 'votre N° de téléphone pro'),
    'Adresse': ('Algeria', "pas la peine d'expliquer aussi"),
    'Google_analytics_id': ('12345678', "l'identifiant de la vue analytics"),
    'Google_analytics_tag': ('UA-xxxxxxxx-1', "Tag de la balise"),
    'Google_analytics_credentials': ('{json}', "Votre clés d'API", 'api_field'),
    'fav_icon': ('', "L'icone du site web", 'image_field'),
    'hero_image': ('', "Hero Image", 'image_field'),
    'footer_image': ('', "Footer Image", 'image_field'),
    'team_Portfolio': (False, "Is this a team portfolio ?"),
    'contact_info': (True, "Show contact info ?"),
    'contact_iframe': ("""<iframe src="" width="640" height="583" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>""", "Show contact info ?"),
}

CONSTANCE_CONFIG_FIELDSETS = {
    'Informations génerales': ('team_Portfolio', "CV",'contact_info', 'hero_image', 'name','hero_message', 'footer_image', 'job_title', 'description', 'logo', 'about_image', 'theme_color', 'mail', 'Adresse', 'phone', 'brand_url', 'meta_description', 'fav_icon'),
    'Dashboard informations': ('contact_iframe', 'Google_analytics_tag', 'Google_analytics_id', 'Google_analytics_credentials'),
}


# Media
MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')
MEDIA_URL = '/media/'
STATIC_URL = 'static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "the_portfolio/static"),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

