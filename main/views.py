from django.shortcuts import render

def index (request):
    context = {
        'nome': "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
        'preco': 109.95,
        'descricao': "Your perfect pack for everyday use and walks in "
                     "the forest.Stash your laptop(up to 15 inches) in the padded sleeve, your everyday ",
        "categoria": "men's clothing",
        "imagem": "https://fakestoreapi.com/img/81fPKd2AYL._AC_SL1500_.jpg"

    }
    return render(request, 'main/index.html', context)

def sobre (request):
    return render(request, 'main/sobre.html')

def contato(request):
    return render(request, 'main/contato.html')

# Create your views here.
