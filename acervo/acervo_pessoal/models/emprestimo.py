from django.db import models 
from acervo_pessoal.models.livro import Livro
from acervo_pessoal.models.contato import Contato
from acervo_pessoal.models.livro import Livro
from django.contrib.auth.models import User

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
