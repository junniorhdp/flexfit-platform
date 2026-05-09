"""
utils.py — Servicios externos para FLEXFIT
  - Envío de emails (bienvenida, notificaciones)
  - Búsqueda de videos en YouTube Data API v3
"""

import requests
from django.core.mail import send_mail
from django.conf import settings
from .models import Notificacion
from django.utils import timezone



# ─── NOTIFICACIONES ─────────────────────────────────────────────────────────────────────

def crear_notificacion(usuario, mensaje):
    
    Notificacion.objects.create(
        id_usuario=usuario,
        mensaje=mensaje,
        fecha_hora=timezone.now(),
        estado='No Leída'
    )

# ─── EMAIL ─────────────────────────────────────────────────────────────────────

def enviar_email_bienvenida(nombre, email_destino):
    """Envía un correo de bienvenida al usuario recién registrado."""
    asunto = '¡Bienvenido a FLEXFIT! 💪'
    mensaje = f"""Hola {nombre},

¡Tu cuenta en FLEXFIT ha sido creada exitosamente!

Ya puedes iniciar sesión y comenzar a explorar rutinas, registrar tu progreso y alcanzar tus metas fitness.

¡Mucho éxito en tu entrenamiento!

El equipo de FLEXFIT
"""
    try:
        send_mail(
            subject=asunto,
            message=mensaje,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email_destino],
            fail_silently=False,
        )
        return True
    except Exception as e:
        print(f"[FLEXFIT] Error enviando email de bienvenida a {email_destino}: {e}")
        return False


def enviar_email_notificacion(nombre, email_destino, mensaje_notif):
    """Envía un correo cuando el usuario recibe una notificación nueva."""
    asunto = 'Nueva notificación en FLEXFIT'
    mensaje = f"""Hola {nombre},

Tienes una nueva notificación en FLEXFIT:

"{mensaje_notif}"

Ingresa a la plataforma para verla en detalle.

El equipo de FLEXFIT
"""
    try:
        send_mail(
            subject=asunto,
            message=mensaje,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email_destino],
            fail_silently=True,
        )
        return True
    except Exception as e:
        print(f"[FLEXFIT] Error enviando notificación por email: {e}")
        return False


# ─── YOUTUBE API ───────────────────────────────────────────────────────────────
YOUTUBE_SEARCH_URL = 'https://www.googleapis.com/youtube/v3/search'
YOUTUBE_VIDEOS_URL = 'https://www.googleapis.com/youtube/v3/videos'


def buscar_videos_youtube(query, max_results=3):
    """
    Busca videos en YouTube relacionados con un ejercicio.
    Retorna una lista de dicts con: video_id, titulo, thumbnail, url, embed_url
    """
    api_key = settings.YOUTUBE_API_KEY
    print("API KEY USADA:", api_key)

    try:
        params = {
            'part': 'snippet',
            'q': f'{query} ejercicio tutorial',
            'type': 'video',
            'maxResults': max_results,
            'key': api_key,
            'relevanceLanguage': 'es',
            'safeSearch': 'strict',
        }

        resp = requests.get(YOUTUBE_SEARCH_URL, params=params, timeout=5)
        resp.raise_for_status()
        data = resp.json()

        print("RESPUESTA YOUTUBE:", data)

        videos = []

        for item in data.get('items', []):
            vid_id = item.get('id', {}).get('videoId')

            # ⚠️ Si no hay ID válido, lo saltamos
            if not vid_id:
                continue

            snippet = item.get('snippet', {})

            videos.append({
                'video_id': vid_id,
                'titulo': snippet.get('title', 'Sin título'),
                'thumbnail': snippet.get('thumbnails', {}).get('medium', {}).get('url', ''),
                'url': f'https://www.youtube.com/watch?v={vid_id}',
                'embed_url': f'https://www.youtube-nocookie.com/embed/{vid_id}',
            })

        print("VIDEOS PROCESADOS:", videos)
        return videos

    except Exception as e:
        print(f"[FLEXFIT] Error consultando YouTube API: {e}")
        return []