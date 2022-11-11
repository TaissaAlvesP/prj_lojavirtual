from django.db import models
from stdimage.models import StdImageField
from django.db.models import signals
from django.template.defaultfilters import slugify
from django.urls import reverse

class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True


class Categoria(Base):
    nome = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField('Slug', max_length=250, unique=True,
                            blank=True, editable=False)

    class Meta:
        ordering = ('nome',)
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse(
            'produtos:listar_produtos_por_categoria',
            kwargs={
                'slug_categoria': self.slug
            }
        )


class Produto(Base):
    nome = models.CharField('Nome', max_length=200)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    estoque = models.IntegerField('Estoque')
    descricao = models.TextField(blank=True)
    imagem = StdImageField('Imagem', upload_to='produtos',
                           variations={'thumb': (300, 300)})
    slug = models.SlugField('Slug', max_length=250, unique=True,
                        blank=True, editable=False)
    categoria = models.ForeignKey('produtos.Categoria',
                              verbose_name='Categoria', on_delete=models.CASCADE)


    class Meta:
        ordering = ('nome',)
        verbose_name = 'produto'
        verbose_name_plural = 'produtos'


    def __str__(self):
        return self.nome


    def get_absolute_url(self):
        return reverse(
            'produtos:detalhes_produto',
            kwargs={
                'id_produto': self.id,
                'slug_produto': self.slug
            }
        )


def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)


def categoria_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)


signals.pre_save.connect(produto_pre_save, sender=Produto)
signals.pre_save.connect(categoria_pre_save, sender=Categoria)
