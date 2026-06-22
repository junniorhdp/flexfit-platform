from django.core.management.base import BaseCommand
from core.models import Usuario, TipoUsuario
from django.contrib.auth.hashers import make_password
from django.utils import timezone

class Command(BaseCommand):
    help = 'Crea un usuario Admin del sistema'

    def handle(self, *args, **kwargs):
        usuario = input("Usuario: ")
        email = input("Email: ")
        password = input("Contraseña: ")

        tipo_admin = TipoUsuario.objects.get(
        rol="Admin"
        )

        if Usuario.objects.filter(usuario=usuario).exists():
            self.stdout.write(self.style.ERROR("Ese usuario ya existe"))
            return

        Usuario.objects.create(
            nombre="Admin",
            apellido="Sistema",
            usuario=usuario,
            email=email,
            contrasena=make_password(password),
            genero="Otro",  # ← ESTA ERA LA CLAVE 🔥
            fecha_registro=timezone.now().date(),
            id_tipo_usuario=tipo_admin
        )

        self.stdout.write(self.style.SUCCESS("✅ Admin creado correctamente"))