from django.contrib import admin
from django.contrib import admin
from .models import Pedido, ItemPedido


class ItemPedidoInLine(admin.TabularInline):
    model = ItemPedido
    raw_id_fields = ['produto']


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'email', 'logradouro',
                    'numero', 'complemento', 'bairro', 'cidade',
                    'uf', 'cep', 'data_criacao', 'pago']
    list_filter = ['pago', 'data_criacao', 'nome']
    inlines = [ItemPedidoInLine]

# Register your models here.
