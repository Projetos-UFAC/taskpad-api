from django.urls import path
from . import views
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('criar_lista/', views.criar_lista, name='criar_lista'),
    path('criar_atividade/', views.criar_atividade, name='criar_atividade'),
    path('criar_tarefa/', views.criar_tarefa, name='criar_tarefa'), 
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)