#PARA QUE OS MODELOS CRIADOS POSSAM SER APRESENTADOS NA "ADMINISTRAÇÃO DJANGO"

from django.contrib import admin
from .models import Produto, Categoria

#A ORDEM QUE ESTÁ EM LIST_DISPLAY É A ORDEM EM QUE VAI APARECER OS ITENS
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'categoria', 'preco', 'estoque', 'slug',
'criado', 'modificado', 'ativo']

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
     list_display = ['nome', 'slug']

# Register your models here.
