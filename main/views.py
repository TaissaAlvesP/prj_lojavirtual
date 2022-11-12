from django.shortcuts import render
from .forms import ContatoForm
from django.contrib import messages


def index (request):
    return render(request, 'main/index.html')

def sobre (request):
    return render(request, 'main/sobre.html')

def contato(request):

    form = ContatoForm(request.POST or None)
    #Mostra no console os dados presentes no envio dos dados de login
    print(f'Post: {request.POST}')

    if str(request.method) == 'POST':
        #Verifica as regras estabelecidas no core/forms.py na classe ContatoForm
        if form.is_valid():

            form.send_mail()

            #cleaned data captura os dados preenchidos nos campos de formulários
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            messages.success(request, 'E-mail enviado com sucesso!')
            #form = ContatoForm() é para limpar o formulário
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar o e-mail')

    context = {
        'form': form
    }
    return render(request, 'main/contato.html', context)

# Create your views here.
