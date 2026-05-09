from django.core.management.base import BaseCommand
from core.models import Usuario, TipoUsuario
from django.contrib.auth.hashers import make_password
from django.utils import timezone

class Command(BaseCommand):
    help = 'Crea un usuario Coach del sistema'

    def handle(self, *args, **kwargs):
        usuario = input("Usuario Coach: ")
        email = input("Email: ")
        password = input("Contraseña: ")

        tipo_coach = TipoUsuario.objects.get(id_tipo_usuario=2)

        if Usuario.objects.filter(usuario=usuario).exists():
            self.stdout.write(self.style.ERROR("Ese usuario ya existe"))
            return

        Usuario.objects.create(
            nombre="Coach",
            apellido="Sistema",
            usuario=usuario,
            email=email,
            contrasena=make_password(password),
            genero="Otro",
            fecha_registro=timezone.now().date(),
            id_tipo_usuario=tipo_coach
        )

        self.stdout.write(self.style.SUCCESS("✅ Coach creado correctamente"))
        