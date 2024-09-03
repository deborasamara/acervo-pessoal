from django.db import models
from django.db import models

# Create your models here.
class Livro(models.Model):
    nome = models.CharField(255)
    autor = models.CharField(255)
    ano  = models.IntegerField()
    foto = models.ImageField(upload_to='capas/')
    def __str__(self):
        return 

class Contato(models.Model):
    nome =  models.CharField(255)
    email = models.EmailField()
    def __str__(self):
        return 

class Emprestimo(models.Model):
    def __str__(self):
        return 

class Usuario(models.Model):
    def __str__(self):
        return 

