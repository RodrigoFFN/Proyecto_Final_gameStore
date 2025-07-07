import sys
import os

# Agregar el path del proyecto
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))

# Configurar settings de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gameStore.settings")

# Importar la app WSGI
from django.core.wsgi import get_wsgi_application

app = get_wsgi_application()
