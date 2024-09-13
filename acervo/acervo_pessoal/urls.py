from django.urls import path
from . import views

app_name = 'acervo_pessoal'
urlpatterns = [
    path('', views.index, name = 'index'),
    
]