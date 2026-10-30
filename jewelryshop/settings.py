

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from .env file
try:
    from dotenv import load_dotenv
    load_dotenv(os.path.join(BASE_DIR, '.env'))
except ImportError:
    pass

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    'SECRET_KEY',
    'django-insecure-3%y3laftm62q0zaj+s7#p-xqq9(&#q+)s8)p-&#&bz*0$!xu$0'
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'True').lower() in ('true', '1', 'yes')

ALLOWED_HOSTS = [
    host.strip()
    for host in os.environ.get('ALLOWED_HOSTS', '127.0.0.1,localhost,*').split(',')
    if host.strip()
]

# CSRF Trusted Origins for HTTPS hosting (e.g., Render, Railway, custom domain)
CSRF_TRUSTED_ORIGINS = [
    origin.strip()
    for origin in os.environ.get(
        'CSRF_TRUSTED_ORIGINS',
        'http://127.0.0.1,http://localhost'
    ).split(',')
    if origin.strip()
]



SITE_ID = 2

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # allauth apps
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    # your apps
    'django.contrib.humanize',
    'store',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'jewelryshop.urls'

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
                'store.context_preprocessors.store_menu',
                'store.context_preprocessors.cart_menu',
            ],
        },
    },
]

WSGI_APPLICATION = 'jewelryshop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASE_URL = os.environ.get('DATABASE_URL')
if DATABASE_URL:
    try:
        import dj_database_url
        DATABASES = {
            'default': dj_database_url.config(
                default=DATABASE_URL,
                conn_max_age=600,
                conn_health_checks=True,
            )
        }
    except Exception:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'jewelryshop/static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# WhiteNoise storage: compresses files and gives them unique hashes for aggressive caching
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Settings for Media
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.environ.get("EMAIL_HOST", "smtp.gmail.com")
EMAIL_USE_TLS = os.environ.get("EMAIL_USE_TLS", "True").lower() in ('true', '1', 'yes')
EMAIL_PORT = int(os.environ.get("EMAIL_PORT", 587))
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", "glamourgolden19@gmail.com")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", "zrpt qblw hrvx rfmr")
DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL", f"Golden Glamour <{EMAIL_HOST_USER}>")


# settings.py
RAZORPAY_KEY_ID = os.environ.get("RAZORPAY_KEY_ID", "rzp_test_ZLHlbIEvNDs44C")
RAZORPAY_KEY_SECRET = os.environ.get("RAZORPAY_KEY_SECRET", "r4BR7No10ORLNRM7o5eOKWuj")


JAZZMIN_SETTINGS = {
    # Branding
    "site_brand": "Golden Glamour",
    "welcome_sign": "Welcome to the Golden Glamour Admin Panel",
    "copyright": "Golden Glamour © 2025",

    # Top navigation
    "topmenu_links": [
        {"name": "Dashboard", "url": "admin:index", "permissions": ["auth.view_user"], "icon": "fas fa-chart-pie"},
        {"app": "auth"},
        {"app": "store"},
    ],

    # Sidebar
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    "order_with_respect_to": ["auth", "store"],

    # FontAwesome Icons
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",

        # Golden Glamour models
        "store.Address": "fas fa-map-marker-alt",
        "store.Category": "fas fa-tags",
        "store.Product": "fas fa-box-open",
        "store.Cart": "fas fa-shopping-cart",
        "store.Order": "fas fa-shipping-fast",
        "store.OrderItem": "fas fa-boxes",
        "store.Coupon": "fas fa-ticket-alt",  
        "store.Wishlist": "fas fa-heart",
        "store.Blog": "fas fa-blog",
        "store.Customer": "fas fa-user-friends",
        "store.Review": "fas fa-comments",
        "store.Payment": "fas fa-credit-card",


    },

    # Admin form layout
    "changeform_format": "horizontal_tabs",
    "related_modal_active": True,

    # Custom UI
    "custom_css": "css/custom_admin.css",
    "custom_js": "js/custom_admin.js",

    "custom_links": {
    "auth": [
        {
            "name": "Admin Dashboard",
            "url": "store:admin-dashboard",  # Same as before
            "icon": "fas fa-chart-line",
            "permissions": ["auth.view_user"]
        }
    ]
    }
}

#google seting fopr login/regioster


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]


LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/accounts/login/'
ACCOUNT_LOGIN_METHODS = {'email'}
ACCOUNT_SIGNUP_FIELDS = ['email*']
ACCOUNT_EMAIL_VERIFICATION = 'none'
SOCIALACCOUNT_AUTO_SIGNUP = True


SOCIALACCOUNT_ADAPTER = 'store.adapters.MySocialAccountAdapter'

# Production security settings
if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = os.environ.get('SECURE_SSL_REDIRECT', 'True').lower() in ('true', '1', 'yes')
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    if os.environ.get('SECURE_HSTS_SECONDS'):
        SECURE_HSTS_SECONDS = int(os.environ.get('SECURE_HSTS_SECONDS'))
        SECURE_HSTS_INCLUDE_SUBDOMAINS = True
        SECURE_HSTS_PRELOAD = True

