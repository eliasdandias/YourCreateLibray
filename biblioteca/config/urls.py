

from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('cadastro_pessoa/', views.CadastrarPessoa.as_view(), name='pessoa'),
    path('cadastrar_genero/', views.CadastrarGenero.as_view(), name='genero'),
    path('cadastrar_livro/', views.CadastrarLivro.as_view(), name='livro'),    
    path('cadastrar_capitulo/', views.CadastrarCapitulo.as_view(), name='capitulo'),
    path('cadastrar_bibliografia/', views.CadastrarBibliografia.as_view(), name='bibliografia'),
    path('cadastro_franquia/', views.CadastrarFranquia.as_view(), name='franquia'),
    # path('listar_dados/', views.listar_dados, name='listar_dados'),
]