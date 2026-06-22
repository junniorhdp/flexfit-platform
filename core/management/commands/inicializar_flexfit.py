from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from core.models import Usuario, TipoUsuario, Logro


class Command(BaseCommand):

    help = "Carga datos iniciales FlexFit"


    def handle(self, *args, **kwargs):

        # ==========================
        # TIPOS DE USUARIO
        # ==========================

        for rol in ["Admin", "Coach", "Usuario"]:

            TipoUsuario.objects.get_or_create(
                rol=rol
            )


        admin_tipo = TipoUsuario.objects.get(
            rol="Admin"
        )


        # ==========================
        # ADMIN FLEXFIT
        # ==========================

        Usuario.objects.get_or_create(

            usuario="admin",

            defaults={

                "nombre": "Administrador",

                "apellido": "FlexFit",

                "email": "admin@flexfit.com",

                "genero": "Otro",

                "contrasena": make_password(
                    "Admin1234"
                ),

                "id_tipo_usuario": admin_tipo

            }
        )


        # ==========================
        # LOGROS
        # ==========================

        logros = [

            ("Primer Paso",
             "Completa tu primera sesión",
             1),

            ("Constancia Inicial",
             "Completa 3 sesiones",
             3),

            ("Guerrero Fitness",
             "Completa 25 sesiones",
             25),

            ("Leyenda FlexFit",
             "Completa 100 sesiones",
             100),

            ("Calentando Motores",
             "Completa 5 ejercicios",
             5),

        ]


        for nombre, descripcion, cantidad in logros:

            Logro.objects.get_or_create(

                nombre=nombre,

                defaults={

                    "descripcion": descripcion,

                    "cantidad": cantidad,

                    "estado": "Disponible"

                }

            )


        self.stdout.write(
            self.style.SUCCESS(
                "FlexFit inicializado correctamente"
            )
        )