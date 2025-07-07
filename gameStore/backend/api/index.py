import sys
import os

# Ruta absoluta al backend
sys.path.append(os.path.join(os.path.dirname(__file__), "../backend"))

# Configuración Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gameStore.settings")

# WSGI
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
