#!/usr/bin/env python
"""
Ejecuta este script UNA SOLA VEZ para crear el usuario Admin inicial.
Uso:  python setup_admin.py

Requisitos: Django y mysqlclient instalados, XAMPP corriendo con la BD flexfit.
"""
import os, sys, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FLEXFIT.settings')

# Agrega el directorio del proyecto al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

django.setup()

from django.contrib.auth.hashers import make_password
from core.models import Usuario, TipoUsuario
from django.utils import timezone

def crear_admin():
    # Verificar si ya existe
    if Usuario.objects.filter(usuario='admin').exists():
        print("✓ El usuario 'admin' ya existe.")
        return

    try:
        tipo_admin = TipoUsuario.objects.get(rol='Admin')
    except TipoUsuario.DoesNotExist:
        print("✗ Error: No existe el tipo 'Admin' en la BD.")
        print("  Ejecuta primero el script datos_base.sql en phpMyAdmin.")
        return

    Usuario.objects.create(
        nombre='Administrador',
        apellido='FlexFit',
        genero='Otro',
        usuario='admin',
        contrasena=make_password('Admin1234'),
        email='admin@flexfit.com',
        objetivo='Gestionar el sistema',
        id_tipo_usuario=tipo_admin,
        fecha_registro=timezone.now().date()
    )
    print("✓ Usuario admin creado exitosamente.")
    print("  Usuario:    admin")
    print("  Contraseña: Admin1234")
    print("  ⚠ Cambia la contraseña después del primer login.")

if __name__ == '__main__':
    crear_admin()
