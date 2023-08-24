from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

urlpatterns = [
    path("",  include('home.urls')),
    path("admin/", admin.site.urls),
    path("auth/", include('usuarios.urls')),
    # Acessa o download do schema
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Opções de documentação
    path('api/docs/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
