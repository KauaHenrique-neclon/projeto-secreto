from django.shortcuts import render, redirect
from app.models.homeModels import VideosUsuario
from app.models.perfilModel import Usuario


def videosUsuario(request):
    dadosVideo = VideosUsuario.objects.select_related('idUsuario').all()
    return render(request, 'areaVideo/videosUsuario.html', dadosVideo)