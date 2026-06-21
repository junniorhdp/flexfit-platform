from django.conf import settings
from .models import Usuario


def usuario_actual(request):

    usuario_id = request.session.get(
        'usuario_id'
    )

    usuario = None

    if usuario_id:

        try:
            usuario = Usuario.objects.get(
                pk=usuario_id
            )

        except Usuario.DoesNotExist:
            usuario = None


    return {
        'usuario_actual': usuario,
        'MEDIA_URL': settings.MEDIA_URL
    }