import logging
import os
from sentry.client.handlers import SentryHandler

logging.getLogger().addHandler(SentryHandler())
logger = logging.getLogger('sentry.errors')
logger.propagate = False
logger.addHandler(logging.StreamHandler())
logging.getLogger('south').setLevel(logging.NOTSET)

DEBUG = False
TEMPLATE_DEBUG = DEBUG
TIME_ZONE = 'US/Pacific'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'static')
MEDIA_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'
CACHE_BACKEND = "memcached://127.0.0.1:11211/"
CACHE_TIMEOUT = 60*5
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    "grappelli.context_processors.admin_template_path",
    "places.context_processors.project_context",
)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.eggs.Loader',
    'django.template.loaders.app_directories.Loader',
)
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'breadcrumbs.middleware.BreadcrumbsMiddleware',
)
TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), "templates"),
)
ROOT_URLCONF = 'places.urls'
INSTALLED_APPS = (
    'grappelli',
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.flatpages',
    'django.contrib.messages',
    'django.contrib.redirects',
    'django.contrib.sessions',
    'django.contrib.sites',
    'breadcrumbs',
    'google_analytics',
    'filebrowser',
    'django_extensions',
    'south',
    'oembed',
    'registration',
    'robots',
    'sentry.client',
    'taggit',
    'uni_form',
    'places',
)
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
SESSION_COOKIE_AGE = 10512000
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
DATE_FORMAT = "m-j-y"
BREADCRUMBS_AUTO_HOME = True
ADMIN_TOOLS_MENU = 'places.menu.CustomMenu'
ADMIN_TOOLS_INDEX_DASHBOARD = 'places.dashboard.CustomIndexDashboard'
GRAPPELLI_ADMIN_TITLE = "Places"
GRAPPELLI_ADMIN_HEADLINE = "Places"
FILEBROWSER_DEBUG = False
FILEBROWSER_URL_FILEBROWSER_MEDIA = "/static/filebrowser/"
FILEBROWSER_PATH_MEDIA =  os.path.join(MEDIA_ROOT, 'filebrowser/')
FILEBROWSER_MAX_UPLOAD_SIZE = 104857600
FILEBROWSER_VERSIONS = {
    'fb_thumb': {'verbose_name': 'Admin Thumbnail', 'width': 60, 'height': 60, 'opts': 'crop upscale'},
    'thumbnail': {'verbose_name': 'Thumbnail (140px)', 'width': 140, 'height': '', 'opts': 'upscale'},
    'homepage': {'verbose_name': 'Homepage (165x123px)', 'width': 165, 'height': 123, 'opts': 'crop upscale'},
    'archive': {'verbose_name': 'Archive (180px)', 'width': 180, 'height': '', 'opts': 'upscale'},
    'issue': {'verbose_name': 'Issue (369px)', 'width': 369, 'height': '', 'opts': 'upscale'},
    'small': {'verbose_name': 'Small (205px)', 'width': 205, 'height': '', 'opts': 'upscale'},
    'medium': {'verbose_name': 'Medium (460x300px)', 'width': 450, 'height': 300, 'opts': 'crop upscale'},
    'big': {'verbose_name': 'Big (620px)', 'width': 620, 'height': '', 'opts': 'upscale'},
    'cropped': {'verbose_name': 'Cropped (60x60px)', 'width': 60, 'height': 60, 'opts': 'crop'},
    'croppedthumbnail': {'verbose_name': 'Cropped Thumbnail (140x140px)', 'width': 140, 'height': 140, 'opts': 'crop'},
}
FILEBROWSER_ADMIN_VERSIONS = ['thumbnail', 'small', 'medium', 'archive', 'issue', 'big']
ACCOUNT_ACTIVATION_DAYS = 7
try:
    from local_settings import *
except ImportError:
    pass