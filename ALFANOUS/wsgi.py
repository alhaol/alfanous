#!/usr/bin/eval PYTHON_VERSION=2.7 python

import os, sys


os.environ['DJANGO_SETTINGS_MODULE'] = "ALFANOUS.settings"


from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()