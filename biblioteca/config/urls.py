

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
    path('livros/',  views.LivroListView.as_view(), name='livro_list'),
    path('livros/<int:pk>/',  views.LivroDetailView.as_view(), name='livro_detail'),
    path('capitulos/', views.CapituloListView.as_view(), name='capitulo_list'),
    path('capitulos/<int:pk>/', views.CapituloDetailView.as_view(), name='capitulo_detail'),
    path('bibliografias/', views.BibliografiaListView.as_view(), name='bibliografia_list'),
    path('bibliografias/<int:pk>/', views.BibliografiaDetailView.as_view(), name='bibliografia_detail'),
    path('franquias/', views.FranquiaListView.as_view(), name='franquia_list'),
    path('franquias/<int:pk>/', views.FranquiaDetailView.as_view(), name='franquia_detail'),

]