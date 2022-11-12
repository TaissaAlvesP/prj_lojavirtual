from django.urls import path
from . import views

app_name = 'carrinho'

#urlpattens é para criar as rotas
#se não for digitado /"nome desejado" irá procurar em detalhes-carrinho
#se for digitado a rota "/adicionar" vai adicionar ao carrinho
urlpatterns = [
    path('', views.detalhes_carrinho, name='detalhes_carrinho'),
    path('adicionar/<int:id_produto>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('remover/<int:id_produto>/', views.remover_do_carrinho, name='remover_do_carrinho'),
]
