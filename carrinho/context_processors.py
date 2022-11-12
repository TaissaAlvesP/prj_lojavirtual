from .carrinho import Carrinho

#retorna um dicionário contendo compras(em qualquer págnia o usuário consegue ver suas compras)
def carrinho(request):
    resultado = {
        'carrinho': Carrinho(request)
    }
    return resultado
