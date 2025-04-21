from django.urls import path
from app.views.perfilUsuario import perfilUsuario


urlpatterns = [
    path('aceitarAmizade/<int:idusuario>',perfilUsuario.aceitarAmizade, name='aceitarAmizade'),
    path('recusarAmizade/<int:idusuario>',perfilUsuario.recusarAmizade, name='recusarAmizade')
]
