from django.db import models
from django.contrib.auth.models import User

class Contato(models.Model):
    nome =  models.CharField(max_length=255)
    email = models.EmailField(max_length=100, unique=True)
    
    def __str__(self):
        return "Nome: " + self.nome + " Email: " + self.email
    
    class Meta: