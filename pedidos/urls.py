from django.urls import path
from . import views

app_name = 'pedidos'

#Rota de pedidos. "endereço"/criar/, direciona para a página de criar pedido
urlpatterns = [
    path('criar/', views.criar_pedido, name='criar_pedido')
]
