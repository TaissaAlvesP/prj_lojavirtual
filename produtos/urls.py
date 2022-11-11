from django.urls import path
from .views import listar_produtos, detalhar_produto

app_name = 'produtos'

urlpatterns = [
    path('<str:id_produto>/<slug_produto>/', detalhar_produto, name='detalhes_produto'),
    path('<slug_categoria>/', listar_produtos, name='listar_produtos_por_categoria'),
    path('', listar_produtos, name='listar_produtos'),
]