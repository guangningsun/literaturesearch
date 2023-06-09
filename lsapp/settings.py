import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'y8)ahmo4#n)aoatj@en2r#f_u99l&b)%9z22+r--j7(+aq)w57'
DEBUG = True
ALLOWED_HOSTS = ["*"]

# 为评论添加
SITE_ID =100

INSTALLED_APPS = [
    'simpleui',
    'rest_framework',
    'django_comments',
    'django.contrib.sites',
    'django_filters',
    'import_export',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'lsapp',
    'AppModel',
    'corsheaders',
    'mptt',
    'django_extensions',
    'werkzeug_debugger_runserver',
    'social_django',
    # 'simpleui_auth',
]

# 第三方登录
AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
    # 'simpleui_auth.backends.FacebookBackend',
    # 'simpleui_auth.backends.GoogleBackend',
    # 'simpleui_auth.backends.TwitterBackend',
    # 'django.contrib.auth.backends.ModelBackend',
)
SOCIAL_AUTH_FACEBOOK_KEY = '<your-facebook-app-id>'
SOCIAL_AUTH_FACEBOOK_SECRET = '<your-facebook-app-secret>'
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '<your-google-oauth2-key>'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '<your-google-oauth2-secret>'
SOCIAL_AUTH_TWITTER_KEY = '<your-twitter-key>'
SOCIAL_AUTH_TWITTER_SECRET = '<your-twitter-secret>'
# SIMPLEUI_AUTH_FACEBOOK_APP_ID = '<your-facebook-app-id>'
# SIMPLEUI_AUTH_FACEBOOK_APP_SECRET = '<your-facebook-app-secret>'
# SIMPLEUI_AUTH_GOOGLE_CLIENT_ID = '<your-google-client-id>'
# SIMPLEUI_AUTH_GOOGLE_CLIENT_SECRET = '<your-google-client-secret>'
# SIMPLEUI_AUTH_TWITTER_CONSUMER_KEY = '<your-twitter-consumer-key>'
# SIMPLEUI_AUTH_TWITTER_CONSUMER_SECRET = '<your-twitter-consumer-secret>'

# env need pip install django-cors-headers
CORS_ORIGIN_ALLOW_ALL = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

ROOT_URLCONF = 'lsapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR+'/templates'],
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

WSGI_APPLICATION = 'lsapp.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'OPTIONS': {
            'timeout': 30,
        }
    }

}

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

LANGUAGE_CODE = 'zh-Hans'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'

# simple ui setting
# 首页信息是否展示
SIMPLEUI_HOME_INFO = False
# 操作是否展示
SIMPLEUI_HOME_ACTION = True
# 数据分析是否展示
SIMPLEUI_ANALYSIS = False
# 批量导入数据
IMPORT_EXPORT_USE_TRANSACTIONS = True
#STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


SIMPLEUI_CONFIG = {
    'menus': [{
        'app': 'AppModel',
        'name': '科研文献管理系统',
        'icon': 'fab fa-dashcube',
        'models': [{
            'name': '文献管理',
            'url': 'AppModel/literatureinfo',
            'icon': 'fa fa-server'
        }]
        },{
        'app': 'auth',
        'name': '权限管理',
        'icon': 'fas fa-user-shield',
        'models': [{
            'name': '系统用户',
            'icon': 'fa fa-user',
            'url': 'auth/user/'
        },{
            'name': '用户组',
            'icon': 'fa fa-users',
            'url': 'auth/group/'
        }]
    }]
}

MPTT_ADMIN_LEVEL_INDENT = 20
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
PRCODE_ROOT = os.path.join(BASE_DIR, 'prcode')
PRCODE_URL = '/prcode/'
#SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
#SECURE_SSL_REDIRECT = True
#SESSION_COOKIE_SECURE = True
#CSRF_COOKIE_SECURE = True
#CSRF_TRUSTED_ORIGINS = ['brilliantlife.com.cn']
#CSRF_TRUSTED_ORIGINS = ['*']
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'http')
CONF_DIR = os.path.join(BASE_DIR, "conf/xz.conf")


# SIMPLEUI_HOME_PAGE = '/tasks/dashboard/'
# SIMPLEUI_HOME_TITLE = '控制面板!' 
# SIMPLEUI_HOME_ICON = 'fa fa-eye'