import sys
import os

# add project path to django
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

# django configuration
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gameStore.settings")

# vercel wsgi
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
