from django.shortcuts import render, redirect
from django.views import View
from .models import Pessoa, Genero, Livro, Capitulo, Bibliografia, Franquia
from .forms import PessoaForm, GeneroForm, LivroForm, CapituloForm, BibliografiaForm, FranquiaForm


# Create your views here.

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
    
class HomeView(View):
    def get(self, request):
        return redirect('index') 

class CadastrarPessoa(View):    
    def get(self, request):
        form = PessoaForm()
        return render(request, 'pessoa.html', {'form': form})

    def post(self, request):
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html')
        return render(request, 'index.html')


class CadastrarGenero(View):    
    def get(self, request):
        form = GeneroForm()
        return render(request, 'genero.html', {'form': form})

    def post(self, request):
        form = GeneroForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html')
        return render(request, 'index.html')

class CadastrarLivro(View):
    def get(self, request):
        form = LivroForm()
        return render(request, 'livro.html', {'form': form})

    def post(self, request):
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html')
        return render(request, 'index.html')

class CadastrarCapitulo(View):
    def get(self, request):
        form = CapituloForm()
        return render(request, 'capitulo.html', {'form': form})

    def post(self, request):
        form = CapituloForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html')
        return render(request, 'index.html')

class CadastrarBibliografia(View):
    def get(self, request):
        form = BibliografiaForm()
        return render(request, 'bibliografia.html', {'form': form})

    def post(self, request):
        form = BibliografiaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html')
        return render(request, 'index.html')
    
class CadastrarFranquia(View):
    def get(self, request):
        form = FranquiaForm()
        return render(request, 'franquia.html', {'form': form})

    def post(self, request):
        form = FranquiaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html')
        return render(request, 'index.html')