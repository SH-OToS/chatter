"""
WSGI config for chat project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys
import site

os.environ.setdefault("DJANGO_SETTINGS_MODULE","chat.settings")
site.addsitedir("/home/tori6978/WebApp/lib/python3.5/site-packages")

sys.path.append("/home/tori6978/WebApp/chat/chat")
sys.path.append("/home/tori6978/WebApp/chat")
sys.path.append("/home/tori6978/WebApp/lib/python3.5/site-packages/django/bin")

#sys.path.append("/var/www/html/test/chat")
#sys.path.append("/var/www/html/test/chat/chat")


#activate_env = os.path.expanduser("/home/tori6978/WebApp/bin/activate_this.py")
#execfile(activate_env, dict(__file__=activate_env))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
