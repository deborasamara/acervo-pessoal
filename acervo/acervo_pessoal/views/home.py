from django.shortcuts import render

# Create your views here.
from django.views import View
from . models import *
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

class home(View):
      def get(self, request, *args, **kwargs):
        return redirect('pag_inicial_logado') if request.user.is_authenticated else render(request, 'acervo_pessoal/home.html')

class homePageLogado(View):
      def get(self, request, *args, **kwargs):
        
        return render(request, 'acervo_pessoal/pag_inicial_logado.html')




