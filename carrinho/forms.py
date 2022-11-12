from django import forms

OPCOES_QUANTIDADE_PRODUTO = []

#Permite que o usuário possa escolher a quantidade de itens(mesmo item) de 1 até 10
#ou seja, pode escolher até 10 do mesmo item.
for i in range(1, 11):
    OPCOES_QUANTIDADE_PRODUTO.append((i, str(i)))


class FormAdicionarProdutoAoCarrinho(forms.Form):

    #coerce=int força a conversão de qualquer valor para quantidade em número inteiro
    quantidade = forms.TypedChoiceField(
        choices=OPCOES_QUANTIDADE_PRODUTO, coerce=int)

    #widget=forms... permite que os dados incluídos nessa tag possam ser  enviados sem a necessidade
    #de estarem visivéis no formulário quando ocorrer uma operação de envio
    atualizar = forms.BooleanField(required=False, widget=forms.HiddenInput)
