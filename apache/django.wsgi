import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'pasteproject.settings'

sys.path.append('E:/pasteproject')
 
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()