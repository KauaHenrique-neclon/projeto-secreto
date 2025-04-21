from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from app.models.homeModels import PostsFoto, PostsText, ComentarioPostsText, ComentariosPostsFoto
from app.models.perfilModel import Usuario
import datetime
from django.utils import timezone


def publicarPost(request):
    """if not request.user.is_authenticated:
        messages.error(request, "Você precisa estar logado para publicar um post.")
        return redirect('login')
    user_id = request.user.id
    print(f"user id: {user_id}")"""
    try:
        user_id = request.session.get('user_id')
        dadosUsuario = Usuario.objects.get(idusuario=user_id)
        contextoDadosUsuario = {'dados': dadosUsuario}
    except Usuario.DoesNotExist:
        messages.error(request, "Usuário não encontrado.")
        return redirect('publicarPostFoto')
    if request.method == 'POST':
        imagem = request.FILES.get('image')
        descricao = request.POST.get('descricao')
        if not imagem or not descricao:
            messages.error(request, "Preencha todos os dados")
            return redirect('publicarPostFoto')
        try:
            salvarPublicacaoFoto = PostsFoto(
                imagens=imagem,
                datapostagem=timezone.now(),
                descricao=descricao,
                idUsuario=dadosUsuario
            )
            salvarPublicacaoFoto.save()
            messages.success(request, "Postagem publicada com sucesso!")
            return redirect('publicarPostFoto')
        except Exception as e:
            messages.error(request, f'Não foi possível publicar: erro: {e}')
            return redirect('publicarPostFoto')
    return render(request, 'publicar/publicar.html', contextoDadosUsuario)

def publicarPostText(request):
    try:
        user_id = request.session.get('user_id')
        dadosUsuario = Usuario.objects.get(idusuario=user_id)
    except Usuario.DoesNotExist:
        messages.error(request, "Usuario não encontrado.")
        return redirect('publicarPostFoto')
    if request.method == 'POST':
        descricao = request.POST.get('descricao')
        if not descricao:
            messages.error(request,'Preencha o campo do texto')
            return redirect('publicarPostFoto')
        try:
            salvarPublicacaoText = PostsText(
                datapostagem=timezone.now(),
                descricao=descricao,
                idUsuario=dadosUsuario
            )
            salvarPublicacaoText.save()
        except:
            messages.error(request, 'Não foi possivel publicar')
            return redirect('publicarPostFoto')


def publicarComentario(request):
    try:
        userID = request.session.get('user_id')
        dadosUsuario = Usuario.objects.get(idusuario=userID)
    except Usuario.DoesNotExist:
        messages.error(request, 'Usuario não encontrado.')
        #return redirect('')
    if request.method == 'POST':
        idDoPost = request.POST.get('idPostComentario')
        dadosPost = PostsFoto.objects.get(idPost=idDoPost)
        comentarioDoUsuario = request.POST.get('comentarioUsuario')
        if not idDoPost:
            messages.error(request,'Erro ao carregar comentarios')
        if not comentarioDoUsuario:
            messages.error(request,'Digite seu comentario para publicar')
        try:
            salvarComentario = ComentariosPostsFoto(
                textComentado = comentarioDoUsuario,
                dataComentario = timezone.now(),
                idUsuario = dadosUsuario,
                idPost = dadosPost
            )
            salvarComentario.save()
        except:
            messages.error(request, 'Não foi possivel publicar comentario')