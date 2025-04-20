from django.db import models
import datetime
from app.models.perfilModel import Usuario

# Create your models here.

class PostsFoto(models.Model):
    idPost = models.AutoField(primary_key=True)
    imagens  = models.ImageField(upload_to='fotosUsuarios/fotosUsuarios',blank=True,null=False)
    datapostagem = models.DateField(default=datetime.date.today)
    descricao = models.TextField(max_length=255, null=False)
    idUsuario = models.ForeignKey(Usuario, to_field="idusuario",on_delete=models.CASCADE)

class PostsText(models.Model):
    idPostText = models.AutoField(primary_key=True)
    datapostagem = models.DateField(default=datetime.date.today)
    descricao = models.TextField(max_length=255,null=False)
    idUsuario = models.ForeignKey(Usuario, to_field="idusuario",on_delete=models.CASCADE)

class ComentariosPostsFoto(models.Model):
    idComentario = models.AutoField(primary_key=True)
    textComentado = models.TextField(max_length=255, null=False)
    dataComentario = models.DateField(default=datetime.date.today)
    idUsuario = models.ForeignKey(Usuario, to_field="idusuario",on_delete=models.CASCADE)
    idPost = models.ForeignKey(PostsFoto, to_field="idPost", on_delete=models.CASCADE)

class ComentarioPostsText(models.Model):
    idComentario = models.AutoField(primary_key=True)
    textComentado = models.CharField(max_length=190)
    dataComentario = models.DateField(default=datetime.date.today)
    idUsuario = models.ForeignKey(Usuario, to_field="idusuario",on_delete=models.CASCADE)
    idPostText = models.ForeignKey(PostsText, to_field="idPostText", on_delete=models.CASCADE)



"""
insert into app_usuario(username,password,is_active, first_name, last_name, datacriacao,email) values('kaua','123','true','kaua','correa','2025-04-16','teste123@gmail.com')

insert into app_postsfoto(imagens,dataPostagem,descricao,idUsuario_id) values('sandy.png','2025-04-16','teste aparece teste aparece teste aparece teste aparece','1')

"""

"""

create database perfil;
create database mensagens;
create database postes;

"""