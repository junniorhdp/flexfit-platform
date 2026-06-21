from django.contrib import admin
from django.urls import path, include


from django.conf import settings
from django.conf.urls.static import static
from core.views import media_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),

    re_path(
        r'^media/(?P<path>.*)$',
        media_view
    ),
]