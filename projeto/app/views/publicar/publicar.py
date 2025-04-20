from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from app.models.homeModels import PostsFoto, PostsText, ComentarioPostsText, ComentariosPostsFoto
from app.models.perfilModel import Usuario
import datetime


def publicarPost(request):
    user_id = request.session.get('user_id')
    dadosUsuario = Usuario.objects.get(idusuario=user_id)
    contextoDadosUsuario = {'dados':dadosUsuario}
    if request.method == 'POST':
        imagem = request.FILES.get('image')
        descricao = request.POST.get('descricao')
        if not imagem or not descricao:
            messages.error(request, "Preencha todos os dados")
            return render(request, 'publicar/publicar.html', contextoDadosUsuario)
        try:
            usuario = Usuario.objects.get(idusuario=user_id)
            salvarPublicacaoFoto = PostsFoto(
                imagens = imagem,
                datapostagem = datetime.datetime.now().day,
                descricao = descricao,
                idUsuario = usuario.idusuario
            )
            salvarPublicacaoFoto.save()
        except Exception as e:
            messages(request,f'Não foi possivel publicar:  erro: {e}')
            return render(request, 'publicar/publicar.html', contextoDadosUsuario)
    return render(request, 'publicar/publicar.html', contextoDadosUsuario)

def publicarPostText(request):
    user_id = request.session.get('user_id')
    dadosUsuario = Usuario.objects.get(idusuario=user_id)
    contextoDadosUsuario = {'dados':dadosUsuario}
    if request.method == 'POST':
        descricao = request.POST.get('descricao')
        if not descricao:
            messages.error(request,'Preencha o campo do texto')
            return render(request, 'publicar/publicar.html', contextoDadosUsuario)
        try:
            salvarPublicacaoText = PostsText(
                datapostagem = datetime.datetime.now().day,
                descricao = descricao,
                idUsuario = user_id
            )
            salvarPublicacaoText.save()
        except:
            messages.error(request, 'Não foi possivel publicar')
            return render(request, 'publicar/publicar.html', contextoDadosUsuario)


def publicarComentario(request):
    userID = request.session.get('user_id')
    if request.method == 'POST':
        idDoPost = request.POST.get('idPostComentario')
        comentarioDoUsuario = request.POST.get('comentarioUsuario')
        if not idDoPost:
            messages.error(request,'Erro ao carregar comentarios')
        if not comentarioDoUsuario:
            messages.error(request,'Digite seu comentario para publicar')
        try:
            if idDoPost and comentarioDoUsuario:
                salvarComentario = ComentariosPostsFoto(
                    textComentado = comentarioDoUsuario,
                    idUsuario = userID,
                    idPost = idDoPost
                )
                salvarComentario.save()
        except:
            messages.error(request, 'Não foi possivel publicar comentario')