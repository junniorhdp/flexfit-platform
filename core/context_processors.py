from .models import Usuario


def usuario_actual(request):

    usuario_id = request.session.get(
        'usuario_id'
    )

    if not usuario_id:

        return {
            'usuario_actual': None
        }

    try:

        usuario = Usuario.objects.get(
            pk=usuario_id
        )

        return {
            'usuario_actual': usuario
        }

    except Usuario.DoesNotExist:

        return {
            'usuario_actual': None
        }