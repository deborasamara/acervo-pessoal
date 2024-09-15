from django.shortcuts import render, redirect
# Create your views here.
from django.views import View
from ..models.livro import *
from ..models.contato import *
from ..models.emprestimo import *
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

class RegistrarEmprestimoView(View):
    def get(self, request, *args, **kwargs):
        emprestimos = Emprestimo.objects.filter(usuario=request.user).order_by('-id')
        livros = Livro.objects.filter(usuario=request.user)
        contatos = Contato.objects.filter(usuario=request.user)
        return render(request, 'registrar_emprestimo.html', {'emprestimos': emprestimos, 'livros':livros, 'contatos':contatos})
    
    def post(self, request, *args, **kwargs):
        livro_id = request.POST.get('livro') #pega o id do livro
        contato_id = request.POST.get('contato') 

        #procura por id para poder enviar para a criação do emprestimo
        livro = get_object_or_404(Livro, id=livro_id)
        contato = get_object_or_404(Contato, id=contato_id)

        emprestimo = Emprestimo(
            livro= livro,
            contato= contato,
            data_devolucao= None,
            usuario=request.user,
            status_emprestimo='ativo'
        )

        emprestimo.save()
        return redirect(request.META.get('HTTP_REFERER'))
    