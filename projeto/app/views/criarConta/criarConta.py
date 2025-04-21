from django.shortcuts import render, redirect
from django.contrib import messages
from app.models.perfilModel import Usuario
from django.utils import timezone
import re
from django.core.validators import validate_email

def criandoConta(request):
    if request.method == 'POST':
        nomeUsuario = request.POST.get('username')
        password = request.POST.get('password')
        primeiroNome = request.POST.get('first_name')
        ultimoNome = request.POST.get('last_name')
        email = request.POST.get('email')
        datanascimento = request.POST.get('dataNascimento')
        cidadenatal = request.POST.get('cidadeNatal')
        estadocivil = request.POST.get('estadoCivil')
        if not nomeUsuario or not password or not primeiroNome or not ultimoNome or not email:
            messages.error(request, 'Preencha todos os campos')
        if not datanascimento or not cidadenatal or not estadocivil:
            messages.error(request, 'Preencha todos os campos')
        if len(password) <= 8 and password.isdigit():
            messages.error(request, 'Senha deve ter pelo menos 8 digitos')
        #if not validate_email(email):
           # messages.error(request, 'Entra com um email')
        try:
            padrão = r"^[a-zA-Z0-9._%+-]+@[gmail.-]+\.(com)$"
            #if re.match(padrão, email, re.IGNORECASE):
            #verificarEmail = Usuario.objects.filter(email=email).first()
            #if verificarEmail is None:
            if re.match(padrão, email, re.IGNORECASE):
                verificarEmail = Usuario.objects.filter(email=email).first()
                if verificarEmail is None:
                    criandoContaUsuario = Usuario(
                        username = nomeUsuario,
                        password = password,
                        first_name = primeiroNome,
                        last_name = ultimoNome,
                        datacriacao = timezone.now(),
                        email = email,
                        datanascimento = datanascimento,
                        cidadenatal = cidadenatal,
                        estadocivil = estadocivil
                    )
                    criandoContaUsuario.save()
                    messages.success(request, 'Conta criada com sucesso.')
                    return redirect('login')
                else:
                    messages.success(request, 'Conta criada com sucesso.')
            else:
                messages.error(request, 'Entre com um email')
                #return redirect('login')
        except:
            messages.error(request, 'Desaculpa, Erro em criar conta')
            #return redirect('login')
    return render(request, 'criarConta/criarConta.html')