"""
WSGI config for podcaster project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "podcaster.settings")

application = get_wsgi_application()

# uncomment the following, and comment the application= line above to check if
# we're running in embedded mode, or daemon mode
# def application(environ, start_response):
#     status = '200 OK'

#     if not environ['mod_wsgi.process_group']:
#       output = u'EMBEDDED MODE'
#     else:
#       output = u'DAEMON MODE'

#     response_headers = [('Content-Type', 'text/plain'),
#                         ('Content-Length', str(len(output)))]

#     start_response(status, response_headers)

#     return [output.encode('UTF-8')]
