"""
Bare minimum settings for collecting production assets.
"""
from ..common import *
from openedx.core.lib.derived import derive_settings

ENABLE_COMPREHENSIVE_THEMING = True
COMPREHENSIVE_THEME_DIRS.append('/openedx/themes')

STATIC_ROOT_BASE = '/openedx/staticfiles'

SECRET_KEY = 'secret'
XQUEUE_INTERFACE = {
    'django_auth': None,
    'url': None,
}
DATABASES = {
    "default": {},
}
