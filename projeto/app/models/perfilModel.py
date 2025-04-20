from django.db import models
import datetime

class Usuario(models.Model):
    idusuario = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True, null=False)
    password = models.CharField(max_length=255, null=False)
    is_active = models.BooleanField(default=True)
    #is_staff = models.BooleanField(default=False)
    #is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    datacriacao = models.DateField(default=datetime.date.today)
    email = models.EmailField(blank=True,unique=True,null=True)
    fotousuario = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.username

class DadosPessoais(models.Model):
    dataNascimento = models.DateField()
    cidadeNatal = models.CharField(max_length=50)
    estadocivil = models.CharField(max_length=15)
    idUsuario = models.ForeignKey(Usuario, to_field="idusuario", on_delete=models.CASCADE, related_name='dados_pessoais')

class Amizades(models.Model):
    idAmizade = models.AutoField(primary_key=True)
    idUsuario = models.ForeignKey(Usuario, related_name='amizades_iniciadas', on_delete=models.CASCADE)
    idAmigo = models.ForeignKey(Usuario, related_name='amizades_recebidas', on_delete=models.CASCADE)
    status = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.idUsuario.username} está amigo de {self.idAmigo.username} ({self.status})"