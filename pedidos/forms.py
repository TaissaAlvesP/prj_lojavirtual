from django import forms
from .models import Pedido


class FormCriarPedido(forms.ModelForm):

    nome = forms.CharField(label='nome', max_length=100,
                           widget=forms.TextInput(attrs={
                               'class': 'order__field',
                               'placeholder': 'digite seu nome'}))

    email = forms.EmailField(label='E-mail', max_length=200,
                             widget=forms.TextInput(attrs={
                                 'class': 'order__field',
                                 'placeholder': 'digite seu e-mail'}))

    logradouro = forms.CharField(label='Logradouro', max_length=100,
                                 widget=forms.TextInput(attrs={
                                     'class': 'order__field',
                                     'placeholder': 'rua, avenida, praça, ...'}))

    numero = forms.CharField(label='Numero', max_length=10,
                             widget=forms.TextInput(attrs={
                                 'class': 'order__field'}))

    complemento = forms.CharField(label='Complemento', max_length=20,
                                  widget=forms.TextInput(attrs={
                                      'class': 'order__field'}))

    bairro = forms.CharField(label='Bairro', max_length=50,
                             widget=forms.TextInput(attrs={
                                 'class': 'order__field'}))

    cidade = forms.CharField(label='Cidade', max_length=100,
                             widget=forms.TextInput(attrs={
                                 'class': 'order__field'}))

    uf = forms.CharField(label='UF', max_length=2,
                         widget=forms.TextInput(attrs={
                             'class': 'order__field'}))

    cep = forms.CharField(label='CEP', max_length=8,
                          widget=forms.TextInput(attrs={
                              'class': 'order__field'}))

    class Meta:
        model = Pedido
        fields = ['nome', 'email', 'logradouro', 'numero', 'complemento',
                  'bairro', 'cidade', 'uf', 'cep']
