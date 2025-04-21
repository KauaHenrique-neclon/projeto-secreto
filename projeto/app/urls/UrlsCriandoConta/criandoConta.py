from django.urls import path
from app.views.criarConta import criarConta

urlpatterns = [
    path('criandoConta/',criarConta.criandoConta, name='criandoConta'),
]
