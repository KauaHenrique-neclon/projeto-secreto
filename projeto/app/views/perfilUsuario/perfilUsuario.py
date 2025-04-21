from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from app.models.perfilModel import Usuario, Amizades
from app.models.homeModels import PostsFoto, PostsText, ComentariosPostsFoto
import random

def perfilUsuario(request):
    user_id = request.POST.get('idUsuarioPerfil', request.session.get('user_id'))
    if user_id is None:
        return redirect('login')
    dadosPost = PostsFoto.objects.filter(idUsuario=user_id).all()
    dadosUsuario = Usuario.objects.get(idusuario=user_id)
    dadosPostText = PostsText.objects.filter(idUsuario=user_id).all()
    amizadesPedendes = Amizades.objects.filter(idAmigo=dadosUsuario, status='pedende').all()
    usuariosQuePediramAmizade = Amizades.objects.filter(idAmigo=dadosUsuario, status='pendente')
    listaDeAmigos = []
    for amigos in usuariosQuePediramAmizade:
        usuarioAmigo = Usuario.objects.get(idusuario=amigos.idUsuario)
        listaDeAmigos.append({
                'nome': usuarioAmigo.username,
                'fotos': usuarioAmigo.fotousuario,
        })
    dados = {'dadosPost':dadosPost,
            'dadosUsuario':dadosUsuario,
            'dadosPostText':dadosPostText,
            'amizadesPedendes':amizadesPedendes,
            'usuariosQuePediramAmizade':listaDeAmigos}
    contexto = {}
    ## pegando comentario de post
    if request.method == 'POST':
        idPostComentario = request.POST.get('comentario')
        if idPostComentario:
            post = get_object_or_404(PostsFoto, idPost=idPostComentario)
            if post:
                dadosComentarioPost = ComentariosPostsFoto.objects.filter(idPost=idPostComentario).all()
                if dadosComentarioPost.exists():
                    comentarioRandom = random.choice(dadosComentarioPost)
                    usuarioComentario = get_object_or_404(Usuario, idusuario=comentarioRandom.idUsuario)
                    contexto['comentario'] = comentarioRandom
                    contexto['usuario'] = usuarioComentario
                else:
                    contexto['mensagem'] = "Não há comentários para este post."
    dadosTotais = {**dados, **contexto}
    return render(request, 'perfilUsuario/perfilUsuario.html', dadosTotais)

def deletePostFoto(request):
    idPostRecebido = request.POST.get('deletePost')
    user_id = request.session.get('user_id')
    if idPostRecebido:
        #usuario = Usuario.objects.get(idusuario=user_id)
        post = PostsFoto.objects.filter(idPost=idPostRecebido, idUsuario=user_id).first()
        if post:
            post.delete()
            messages.success(request, 'Sucesso ao deletar Post.')
            return redirect('')
    else:
        messages.error(request, 'Erro ao deletar Post.')

def perfilUsuarioVer(request, idUsuario):
    idVisitante = request.session.get('user_id')
    if not idVisitante:
        return redirect('login')
    idUsuarioPegado = get_object_or_404(Usuario, idUsuario)
    statusAmizade = "Não Amigos"
    if idVisitante:
        try:
            amizade = Amizades.objects.get(idUsuario=idVisitante, idAmigo=idUsuarioPegado)
            statusAmizade = amizade.status
        except Amizades.DoesNotExist:
            statusAmizade = "Não Amigos"
    if idUsuarioPegado:
        dadosUsuario = Usuario.objects.get(idUsuario=idUsuario)
        postsFotos = PostsFoto.objects.get(idUsuario=dadosUsuario.idusuario)
        postsText = PostsText.objects.get(idUsuario=dadosUsuario.idusuario)
        contexto = {'dadosUsuario':dadosUsuario,
                    'postsFotos':postsFotos,
                    'postsText':postsText,
                    'statusAmizade':statusAmizade}
    return render(request, 'perfilUsuario/verPerfilUsuario.html',contexto)

def adicionarAmigos(request, idUsuarioPerfil):
    idUsuario = request.session.get('user_id')
    dadosUsuario = Usuario.objects.get(idUsuario=idUsuario)
    dadosUsuarioAdicionar = Usuario.objects.get(idUsuario=idUsuarioPerfil)
    try:
        fazerAmizade = Amizades(
            idUsuario = dadosUsuario,
            idAmigo = dadosUsuarioAdicionar,
            status = 'pedende'
            )
        fazerAmizade.save()
        messages.success(request,'Amizade enviada')
    except:
        messages.error(request, 'Não foi possivel adicionar.')

def aceitarAmizade(request, idAmigo):
    idUser = request.session.get('user_id')
    if request.method == 'POST':
        dadosUsuario = get_object_or_404(Usuario, idusuario=idUser)
        amigoExiste = get_object_or_404(Usuario, idusuario=idAmigo)
        try:
            amizade = Amizades.objects.get(idAmigo=amigoExiste, idUsuario=dadosUsuario, status='pendente')
            amizade.status = 'amigos'
            amizade.save()
            messages.success(request, 'Amizade aceita')
        except Amizades.DoesNotExist:
            messages.error(request, 'Não há pedido de amizade pendente')
    else:
        messages.error(request, 'Method não aceito')

def recusarAmizade(request,idAmigo):
    idUser = request.session.get('user_id')
    if request.method == 'POST':
        dadosUsuario = get_object_or_404(Usuario, idusuario=idUser)
        amigoExiste = get_object_or_404(Usuario, idusuario=idAmigo)
        try:
            amizade = Amizades.objects.get(idAmigo=amigoExiste, idUsuario=dadosUsuario, status='pendente')
            amizade.delete()
            amizade.save()
            messages.success(request, 'Amizade recusada')
        except Amizades.DoesNotExist:
            messages.error(request, 'Não há pedido de amizade pendente')
    else:
        messages.error(request, 'Method não aceito')