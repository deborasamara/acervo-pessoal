from django.urls import path
from . import views

app_name = 'acervo_pessoal'
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('home_logado', views.homePageLogadoView.as_view(), name='home_logado'), 
]