from unipath import Path
BASE_DIR = Path(__file__).ancestor(2)

SECRET_KEY = 'acuswvsos@u@cfl9&_a75t4n42-t!f3_gjt3str^noo7_t71*='

DJANGO_APPS = (

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',	

)

THIRD_PARTY_APPS = (

    'south',

)	

LOCAL_APPS = (

    'sistemaDiscusiones.apps.home',
    'sistemaDiscusiones.apps.users',
    'sistemaDiscusiones.apps.discuss',

)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS



MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'sistemaDiscusiones.urls'

WSGI_APPLICATION = 'sistemaDiscusiones.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_DIRS = [BASE_DIR.child('templates')]

AUTH_USER_MODEL = 'users.User'