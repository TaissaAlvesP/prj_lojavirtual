#Para ser possível efetuar alterações no painel administrativo

from django.contrib import admin
from django.contrib import admin
from .models import Pedido, ItemPedido


class ItemPedidoInLine(admin.TabularInline):
    model = ItemPedido
    #Para definir os produtos aparecendo com uma lupa ao lado, em "Item Pedidos"
    raw_id_fields = ['produto']


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'email', 'logradouro',
                    'numero', 'complemento', 'bairro', 'cidade',
                    'uf', 'cep', 'data_criacao', 'pago']
    list_filter = ['pago', 'data_criacao', 'nome']

    #Faz com que os dados das classes relacionadas(no caso ItemPedido e Produtos) sejam
    #apresentados no painel Adimin
    inlines = [ItemPedidoInLine]

# Register your models here.
