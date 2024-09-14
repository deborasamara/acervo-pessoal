from django.urls import path
from .views.gerenciarEmprestimo import *
from .views.gerenciarContato import *
from .views.gerenciarLivro import *
from .views.home import *
from .views.outros import *

app_name = 'acervo_pessoal'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('home_logado/', HomePageLogadoView.as_view(), name='home_logado'), 
    path('cadastro/', CadastroView.as_view(), name='cadastro'),
    path('login/', LoginView.as_view(), name='login'),
    
]