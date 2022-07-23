from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Hakaton API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view), # swagger
    path('user/', include('apps.users.urls')),
    path('review/', include('apps.review.urls')),
    path('favorite/', include('apps.favorite.urls')),
    path('auth/', include('djoser.urls')), # djoser регистрация
    path('auth/', include('djoser.urls.authtoken')), # djoser вход и вызод из системы
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 