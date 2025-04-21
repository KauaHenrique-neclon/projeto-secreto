from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from app.models.homeModels import PostsFoto, PostsText, ComentarioPostsText, ComentariosPostsFoto
from app.models.perfilModel import Usuario
import random
from django.utils import timezone

def loginUsuario(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        if not email or not senha:
            messages.error(request, 'Entre com email e senha')
        user = Usuario.objects.filter(username=email).first()
        if user is not None and senha == user.password:
            request.session['user_id'] = user.idusuario
            return redirect('escolha')
    return render(request,'login/login.html')

def escolher(request):
    return render(request,'login/escolha.html')

def paginaInicial(request):
    contexto = {}
    if request.method == "POST":
        idPostPagina = request.POST.get('comentario')
        if idPostPagina:
            post = get_object_or_404(PostsFoto, idPost=idPostPagina)
            comentarioPost = PostsFoto.objects.filter(idPost=idPostPagina).all()
            if comentarioPost.exists():
                usuarioComentarios = random.choice(comentarioPost)
                usuarios = Usuario.objects.filter(idusuario=usuarioComentarios.idUsuario)
                contexto = {
                    'comentario': comentarioPost,
                    'usuarioComentario': usuarios,
                    'posterFotos': [],
                    'usuario': None
                }
            else:
                contexto = {
                    'comentario': 'sem comentarios',
                    'usuarioComentario': 'sem comentarios',
                    'posterFotos': [],
                    'usuario': None
                }
        else:
            messages.error(request, 'ID do post não fornecido.')
    else:
        usuariosAleatorio = Usuario.objects.all()
        if usuariosAleatorio.exists():
            usuario_aleatorio = random.choice(usuariosAleatorio)
            publicacaoFotos = PostsFoto.objects.filter(idUsuario=usuario_aleatorio.idusuario).all()
            contexto = {
                'posterFotos': publicacaoFotos,
                'usuario': usuario_aleatorio
            }
        else:
            contexto = {
                'posterFotos': [],
                'usuario': None
            }
    return render(request, 'home/home.html', contexto)

def comentariosPost(request, idPost):
    idUser = request.session.get('user_id')
    if request.method == 'POST':
        comentario = request.POST.get('comentarioUsuario')
        dadosUsuario = Usuario.objects.get(idusuario=idUser)
        if dadosUsuario:
            comentar = ComentariosPostsFoto(
                idPost = idPost,
                textComentado = comentario,
                idUsuario = dadosUsuario,
                dataComentario = timezone.now()
            )
            comentar.save()
            messages.success(request,'Comentario feito')
        else:
            messages.error(request,'Comentario não feito')
    else:
        messages.error(request,'Comentario não feito')