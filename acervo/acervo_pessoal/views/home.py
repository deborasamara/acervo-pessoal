from django.shortcuts import render
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

class HomeView(View):
      def get(self, request, *args, **kwargs):
        return redirect('pag_inicial_logado') if request.user.is_authenticated else render(request, 'home.html')

class HomePageLogadoView(View):
      def get(self, request, *args, **kwargs):
        
        return render(request, 'acervo_pessoal/pag_inicial_logado.html')




