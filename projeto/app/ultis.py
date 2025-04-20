from app.models.perfilModel import Usuario

def nomeUsuario(request):
    idUser = request.session.get('user_id')
    if idUser:
        try:
            nomeUser = Usuario.objects.get(idusuario=idUser)
            return {'nomeUsuario':nomeUser.username}
        except Usuario.DoesNotExist:
            return {'nomeUsuario':'Desconhecido'}
    else:
        return {'nomeUsuario':'Desconectado'}
        
