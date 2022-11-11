from django.contrib import admin
from .models import Produto, Categoria

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'categoria', 'preco', 'estoque', 'slug',
'criado', 'modificado', 'ativo']

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
     list_display = ['nome', 'slug']

# Register your models here.
