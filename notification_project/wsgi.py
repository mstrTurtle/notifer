"""
WSGI config for notification_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "notification_project.settings")

application = get_wsgi_application()



from notification_app.startup import startup_spawn
startup_spawn()
