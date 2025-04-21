from django.urls import path
from app.views import home
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('',home.loginUsuario, name='login'),
    path('escolha',home.escolher, name='escolha'),
    path('home', home.paginaInicial, name='home'),
    path('comentarios/<int:idPost>', home.comentariosPost),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)