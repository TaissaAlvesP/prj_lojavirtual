#Recebe e trata as informações encapsuladas pelo formulário que contém os dados do pedido

from django.shortcuts import render
from .models import ItemPedido
from .forms import FormCriarPedido
from carrinho.carrinho import Carrinho


def criar_pedido(request):
    carrinho = Carrinho(request)

    #método post é para instanciar a partir do dicionário que contém os parâmentros enviados pela requisição
    if request.method == 'POST':
        form = FormCriarPedido(request.POST)

        #Verifica se há erros, por exemplo, e-mail inválido
        if form.is_valid():
            pedido = form.save()
            #Para cada item do carrinho é criado (e salvo) um objeto do tipo ItemPedido. Depois o pedido é salvo
            #e apresenta a página concluir.html - que diz o número do pedido gravado no banco de dados.
            for item in carrinho:
                ItemPedido.objects.create(pedido=pedido,
                                          produto=item['produto'],
                                          preco=item['preco'],
                                          quantidade=item['quantidade'],
                                          )
            carrinho.limpar_carrinho()
            return render(request, 'pedidos/pedido/concluir.html', {'pedido': pedido})
    else:
        #se não tiver o pedido, assim que preencher o carrinho vai aparecer o formulário para criar o pedido
        form = FormCriarPedido()
    return render(request, 'pedidos/pedido/criar.html', {'carrinho': carrinho, 'form': form})
