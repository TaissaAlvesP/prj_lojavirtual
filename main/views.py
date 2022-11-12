from django.shortcuts import render

def index (request):
    return render(request, 'main/index.html')

def sobre (request):
    return render(request, 'main/sobre.html')

def contato(request):
    return render(request, 'main/contato.html')

# Create your views here.
