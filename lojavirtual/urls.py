
"""lojavirtual URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    #para qualquer rota ' ', deve ser incluido o arquivo de rotas da aplicação core(main.urls)
    path('', include('main.urls')),
    path('produtos/', include('produtos.urls', namespace='produtos')),
    path('carrinho/', include('carrinho.urls', namespace='carrinho')),
    path('pedidos/', include('pedidos.urls',namespace ='pedidos')),
#template de todas as aplicações dentro do proheto, tenham acesso às imagens
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

