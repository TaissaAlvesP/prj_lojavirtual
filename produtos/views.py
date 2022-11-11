from django.shortcuts import render, get_object_or_404
from .models import Produto, Categoria
from carrinho.forms import FormAdicionarProdutoAoCarrinho



def listar_produtos(request, slug_categoria=None):
    categoria = None
    lista_categorias = Categoria.objects.all()
    lista_produtos = Produto.objects.filter(ativo=True)
    if slug_categoria:
        categoria = get_object_or_404(Categoria, slug=slug_categoria)
        lista_produtos = Produto.objects.filter(categoria=categoria)
    contexto = {
        'categoria': categoria,
        'lista_categorias': lista_categorias,
        'lista_produtos': lista_produtos,
    }
    return render(request, 'produtos/produtos.html', contexto)


def detalhar_produto(request, id_produto, slug_produto):

    produto = get_object_or_404(Produto,
                                id=id_produto,
                                slug=slug_produto,
                                ativo=True)

    form_adicionar_produto_ao_carrinho = FormAdicionarProdutoAoCarrinho()

    contexto = {
        'produto': produto,
        'form_produto_carrinho': form_adicionar_produto_ao_carrinho

    }
    return render(request, 'produtos/detalhes.html', contexto)
