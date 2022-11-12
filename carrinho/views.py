from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from produtos.models import Produto
from .carrinho import Carrinho
from .forms import FormAdicionarProdutoAoCarrinho

#redireciona para a página detalhes do carrinho já com o produto adicionado.
@require_POST
def adicionar_ao_carrinho(request, id_produto):
    carrinho = Carrinho(request)
    produto = get_object_or_404(Produto, id=id_produto)
    form = FormAdicionarProdutoAoCarrinho(request.POST)
    if form.is_valid():
        dados = form.cleaned_data
        carrinho.adicionar(
            produto=produto,
            quantidade=dados['quantidade'],
            atualizar_quantidade=dados['atualizar'])
    return redirect('carrinho:detalhes_carrinho')


def remover_do_carrinho(request, id_produto):
    carrinho = Carrinho(request)
    produto = get_object_or_404(Produto, id=id_produto)
    carrinho.remover(produto)
    return redirect('carrinho:detalhes_carrinho')


def detalhes_carrinho(request):

    #Instância o objeto do tipo carrinho carregando todos os dados  do carrinho presente na sessão(onde é armazenado os dados)
    carrinho = Carrinho(request)

    #Varre o carrinho, para atualizar ele sempre que ocorrer modificações
    for item in carrinho:
        item['formulario_adicionar_produto_ao_carrinho'] = \
            FormAdicionarProdutoAoCarrinho(initial={'quantidade': item['quantidade'], 'atualizar': True})

    #Todos os dados do carrinho são enviado para a página que irá mostrar os detalhes do carrinho
    return render(request, 'carrinho/detalhes_carrinho.html', {'carrinho': carrinho})

# Create your views here.
