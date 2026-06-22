from django.core.management.base import BaseCommand
from core.models import Usuario, TipoUsuario
from django.contrib.auth.hashers import make_password


class Command(BaseCommand):

    def handle(self,*args,**kwargs):

        tipo_admin = TipoUsuario.objects.get(
            rol="Admin"
        )


        Usuario.objects.get_or_create(

            usuario="admin",

            defaults={

                "nombre":"Administrador",

                "apellido":"FlexFit",

                "email":"admin@flexfit.com",

                "genero":"Otro",

                "contrasena":make_password(
                    "Admin1234"
                ),

                "id_tipo_usuario":tipo_admin

            }

        )


        self.stdout.write(
            "Admin creado"
        )