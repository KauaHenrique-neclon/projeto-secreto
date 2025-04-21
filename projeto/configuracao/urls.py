from django.contrib import admin
from django.urls import path, include
from app.urls.UrlsHome.home import urlpatterns as urlHome
from app.urls.UrlsPublicar.publicar import urlpatterns as urlPublicar
from app.urls.UrlsCriandoConta.criandoConta import urlpatterns as urlCriandoConta
from app.urls.UrlsPerfilUsuario.UrlsPerfilUsuario import urlpatterns as urlPerfilUsuario
from app.urls.UrlsAdicionarAmigos.urlAdicionarAmigos import urlpatterns as urlAdiconarAmizades

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(urlHome)),
    path('publicar/',include(urlPublicar)),
    path('criarConta/',include(urlCriandoConta)),
    path('perfil/',include(urlPerfilUsuario)),
    path('amizades/',include(urlAdiconarAmizades)),
]