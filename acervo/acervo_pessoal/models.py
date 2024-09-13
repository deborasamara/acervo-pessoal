from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Livro(models.Model):
    nome = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    ano  = models.IntegerField()
    foto = models.ImageField(upload_to='capas/')

    def __str__(self):
        return "Nome: " + self.nome + " Autor: " + self.autor + " Ano: " + self.ano

class Contato(models.Model):
    nome =  models.CharField(max_length=255)
    email = models.EmailField()
    senha = models.CharField(max_length=255)
    def __str__(self):
        return "Nome: " + self.nome + " Email: " + self.email

class Emprestimo(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    contato = models.ForeignKey(Contato, on_delete=models.CASCADE)
    data_emprestimo = models.DateTimeField()
    data_devolucao = models.DateTimeField(blank=True, null=True)
    usuario_portador = models.ForeignKey(User, on_delete=models.CASCADE)
    status_emprestimo = models.CharField(max_length=10, choices= [ ('ativo', 'Ativo'),
        ('devolvido', 'Devolvido')], default='ativo')
    
    def __str__(self):
        return "Livro "+ self.livro + " emprestado para "+ self.contato + " em " + self.data_emprestimo + " status: "+ self.status_emprestimo
    
    def registrar_devolucao():
        self.status_emprestimo = 'devolvido'
        self.data_devolucao = timezone.now()
        self.save() # salva mesmo no banco de dados
