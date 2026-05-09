from .models import (
    SesionEntrenamiento,
    EjercicioSesion,
    UsuarioLogro,
    Logro
)


def verificar_logros(usuario):

    # =========================
    # TOTAL SESIONES
    # =========================
    total_sesiones = SesionEntrenamiento.objects.filter(
        id_rutina_usuario__id_usuario=usuario,
        completada=True
    ).count()

    # =========================
    # TOTAL EJERCICIOS
    # =========================
    total_ejercicios = EjercicioSesion.objects.filter(
        id_sesion__id_rutina_usuario__id_usuario=usuario,
        completado=True
    ).count()

    # =========================
    # LOGROS POR SESIONES
    # =========================
    logros_sesiones = {
        1: 'Primer Paso',
        3: 'Constancia Inicial',
        25: 'Guerrero Fitness',
        100: 'Leyenda FlexFit',
    }

    for cantidad, nombre in logros_sesiones.items():

        if total_sesiones >= cantidad:

            logro = Logro.objects.filter(nombre=nombre).first()

            if logro:
                UsuarioLogro.objects.get_or_create(
                    id_usuario=usuario,
                    id_logro=logro
                )

    # =========================
    # LOGRO EJERCICIOS
    # =========================
    if total_ejercicios >= 5:

        logro = Logro.objects.filter(
            nombre='Calentando Motores'
        ).first()

        if logro:
            UsuarioLogro.objects.get_or_create(
                id_usuario=usuario,
                id_logro=logro
            )