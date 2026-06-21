import os
from pathlib import Path
import dj_database_url  # Requerido para leer la BD de Render

BASE_DIR = Path(__file__).resolve().parent.parent

# ── SEGURIDAD: Variables de Entorno en Producción ─────────────────────────────
# Si no encuentra la variable de entorno, usa una por defecto para desarrollo local
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-m8pigmzm98k1&@*49g4_rj%9bti5y_rdosjy)kwgg#2a(v^mbg')

# DEBUG debe ser False en producción
DEBUG = 'RENDER' not in os.environ

ALLOWED_HOSTS = [
    'flexfit-platform.onrender.com',
]

# En Render, tu dominio será algo como flexfit.onrender.com
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


# ── APPS INSTALADAS ───────────────────────────────────────────────────────────
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
]


# ── MIDDLEWARE ────────────────────────────────────────────────────────────────
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # ¡Añadido para los archivos estáticos!
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'FLEXFIT.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'core' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processors.usuario_actual',
            ],
        },
    },
]

WSGI_APPLICATION = 'FLEXFIT.wsgi.application'


# ── CONFIGURACIÓN DE BASE DE DATOS ─────────────────────────────────────────────
# Si está en Render, usa la base de datos que provee Render (PostgreSQL). 
# Si estás en local, usa tu base de datos MySQL de siempre.
if 'RENDER' in os.environ:
    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ.get('DATABASE_URL'),
            conn_max_age=600
        )
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'flexfit_db',
            'USER': 'root',
            'PASSWORD': '',
            'HOST': '127.0.0.1',
            'PORT': '3306',
            'OPTIONS': {
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            },
        }
    }


# ── CONFIGURACIÓN DE EMAIL (Protegido) ─────────────────────────────────────────
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'yuniorochoa333@gmail.com')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', 'masufbtjgzwsnhxz')

DEFAULT_FROM_EMAIL = 'FlexFit <flexfit.app@gmail.com>'


# ── YOUTUBE DATA API V3 (Protegido) ───────────────────────────────────────────
YOUTUBE_API_KEY = os.environ.get('YOUTUBE_API_KEY', 'AIzaSyClfulQi701TZO3Wbo2Di1c_MQqJoZwRQw')


# ── INTERNACIONALIZACIÓN ──────────────────────────────────────────────────────
LANGUAGE_CODE = 'es-co'
TIME_ZONE = 'America/Bogota'
USE_I18N = True
USE_TZ = True


# ── ARCHIVOS ESTÁTICOS Y MEDIA ────────────────────────────────────────────────
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'core' / 'static']

# Carpeta donde WhiteNoise guardará los estáticos procesados en producción
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Almacenamiento eficiente para producción
if not DEBUG:
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/dashboard/'

CSRF_TRUSTED_ORIGINS = [
    "https://flexfit-platform.onrender.com",
]

SECURE_PROXY_SSL_HEADER = (
    'HTTP_X_FORWARDED_PROTO',
    'https'
)

# Ejecutar migraciones y crear superusuario automáticamente en Render
import os
import sys

if 'RENDER' in os.environ:
    from django.core.management import execute_from_command_line
    from django.contrib.auth import get_user_model
    
    print("🚀 Forzando la ejecución de migraciones en Render...")
    try:
        execute_from_command_line(['manage.py', 'migrate', '--no-input'])
        print("✅ Migraciones completadas con éxito.")
        
        # Intentar crear el superusuario automáticamente
        User = get_user_model()
        # Cambia 'admin' y la contraseña por los que tú quieras usar para entrar
        if not User.objects.filter(username='admin').exists():
            print("👤 Creando superusuario administrador...")
            User.objects.create_superuser('admin', 'tu_email@flexfit.com', 'AdminFlexFit2026*')
            print("✅ Superusuario creado con éxito.")
            
    except Exception as e:
        print(f"❌ Error en el proceso de inicialización en producción: {e}", file=sys.stderr)



        # ──────────────────────────────────────────────────────────────────────────────
# CONFIGURACIÓN DE SESIONES Y COOKIES PARA PRODUCCIÓN (HTTPS)
# ──────────────────────────────────────────────────────────────────────────────
if 'RENDER' in os.environ:
    # Asegura que las cookies de sesión viajen únicamente por HTTPS
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    
    # Evita que scripts de JS accedan a las cookies de sesión (Protección XSS)
    SESSION_COOKIE_HTTPONLY = True
    
    # Obliga a Django a guardar la sesión en cada petición para que no expire rápido
    SESSION_SAVE_EVERY_REQUEST = True
    
    # Usa cookies de sesión basadas en base de datos estándar
    SESSION_ENGINE = 'django.contrib.sessions.backends.db'