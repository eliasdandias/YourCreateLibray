# No arquivo forms.py da sua aplicação
from django import forms


from .models import Pessoa, Genero, Livro, Capitulo, Bibliografia, Franquia

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'

class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = '__all__'

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = '__all__'

class CapituloForm(forms.ModelForm):
    class Meta:
        model = Capitulo
        fields = '__all__'

class BibliografiaForm(forms.ModelForm):
    class Meta:
        model = Bibliografia
        fields = '__all__'

class FranquiaForm(forms.ModelForm):
    class Meta:
        model = Franquia
        fields = '__all__'
