from django.urls import path
from app.views.perfilUsuario import perfilUsuario
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('perfilUsuario/',perfilUsuario.perfilUsuario, name='perfilUsuario'),
    path('perfil/<int:idusuario>',perfilUsuario.perfilUsuarioVer, name='verPerfilusuario'),
    path('adicionarAmigos/<int:idusuario>',perfilUsuario.adicionarAmigos,name='adicionarAmigos'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
