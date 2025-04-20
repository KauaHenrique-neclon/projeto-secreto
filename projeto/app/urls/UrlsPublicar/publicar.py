from django.urls import path
from app.views.publicar import publicar
from django.conf.urls import static
from django.conf import settings

urlpatterns = [
    path('publicarPostFoto',publicar.publicarPost, name='publicarPostFoto'),
    path('publicarPostText',publicar.publicarPostText, name='publicarPostText'),
    path('publicarComentario',publicar.publicarComentario, name='publicarComentario'),
]
