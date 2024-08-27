from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Pessoa(models.Model):
    user = models.OneToOneField(User, related_name='profile',on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    data_de_nascimento = models.DateField()
    cidade = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)
    pais_de_origem = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nome} {self.data_de_nascimento} {self.cidade} {self.uf} {self.pais_de_origem}'
    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

class Genero(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    class Meta:    
        verbose_name = "Gênero"
        verbose_name_plural = "Gêneros"

class Livro(models.Model):
    nome = models.CharField(max_length=50)
    data_de_conclusao = models.CharField(max_length=50)
    autor = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} {self.autor} {self.genero} {self.data_de_conclusao}' 
    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"

class Capitulo(models.Model):
    numero = models.IntegerField()
    nome = models.CharField(max_length=50)
    conteudo = models.TextField(max_length=2000)
    data_de_criacao = models.CharField(max_length=50)
    livro = models.ForeignKey(Livro,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.numero} {self.nome} {self.conteudo} {self.data_de_criacao}'
    class Meta:    
        verbose_name = "Capítulo"
        verbose_name_plural = "Capítulos"

class Bibliografia(models.Model):
    autor = models.OneToOneField(Pessoa, on_delete=models.CASCADE, primary_key=True)
    livro = models.ForeignKey(Livro,on_delete=models.CASCADE)
    depoimento = models.CharField(max_length=2000)
    
    def __str__(self):
        return f'{self.autor} {self.livro} {self.depoimento}'
    class Meta:    
        verbose_name = "Bibliografia"

class Franquia(models.Model):
    nome = models.CharField(max_length=50)
    livro = models.ForeignKey(Livro,on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.nome} {self.livro}'
    class Meta:    
        verbose_name = "Franquia"
        verbose_name_plural = "Franquias"