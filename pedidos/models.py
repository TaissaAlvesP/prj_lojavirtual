from django.db import models

from django.db import models
from decimal import Decimal
from produtos.models import Produto


class Pedido(models.Model):
    # Dados do comprador:
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    logradouro = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=20)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    cep = models.CharField(max_length=8)

    # Dados específicos do pedidos:
    data_criacao = models.DateField(auto_now=True)
    pago = models.BooleanField(default=False)

    class Meta:
        ordering = ('-data_criacao',)

    def __str__(self):
        return 'Pedido # ' + str(self.id)

    def get_total_geral(self):
        resultado = Decimal(0.0)
        for item in self.itens.all():
            subtotal = Decimal(item['quantidade']) * Decimal(item['preco'])
        resultado = resultado + subtotal
        return resultado


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='itens', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, related_name='itens_pedido', on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return 'id ItemPedido #' + str(self.id)

    def get_sub_total(self):
        return self.preco * self.quantidade

# Create your models here.
