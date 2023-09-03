from os import environ as env
import sys


try:
    sys.path.remove('/usr/lib/python3/dist-packages')
except:
    pass

# path to django-project
sys.path.insert(0, env.get('PATH_TO_PROJECT'))
# path to config of django-project
sys.path.insert(0, env.get('PATH_TO_CONFIG'))
# path to virtualenv
sys.path.insert(0, env.get('PATH_TO_PACKAGES'))
env['DJANGO_SETTINGS_MODULE'] = 'config.settings.prod'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
