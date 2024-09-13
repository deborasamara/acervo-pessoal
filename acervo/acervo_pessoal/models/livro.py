from django.db import models
from django.contrib.auth.models import User

class Livro(models.Model):
    nome = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    ano  = models.IntegerField()
    foto = models.ImageField(upload_to='capas/')

    def __str__(self):
        return "Nome: " + self.nome + " Autor: " + self.autor + " Ano: " + self.ano

    class Meta:

