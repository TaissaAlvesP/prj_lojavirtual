from django import forms
from django.core.mail.message import EmailMessage


class ContatoForm(forms.Form):
    #Esses contact__field são para possibilitar o css do formulário

    nome = forms.CharField(
        label='nome', max_length=100,
        widget=forms.TextInput(attrs={
                'class': 'contact__field',
                'placeholder': 'digite seu nome'}))

    email = forms.EmailField(
        label='E-mail', max_length=200,
        widget=forms.TextInput(
            attrs={
                'class': 'contact__field',
                'placeholder': 'digite seu e-mail'}))

    assunto = forms.CharField(
        label='Assunto', max_length=120,
        widget=forms.TextInput(attrs={
                'class': 'contact__field',
                'placeholder': 'digite o assunto'}))

    mensagem = forms.CharField(
        label='Mensagem',
        widget=forms.Textarea(attrs={
                'class': 'contact__field'}))

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\n' \
                   f'E-mail: {email}\n' \
                   f'Assunto: {assunto}\n' \
                   f'Mensagem: {mensagem}'

        mail = EmailMessage(
            subject='Solicitação de Contato',
            body=conteudo,
            from_email='email-administrativo-do-django@gmail.com',
            to=['responsavel-por-receber-emails-de-contatos@gmail.com', ],
            headers={'Reply-To': email},
        )

        mail.send()
