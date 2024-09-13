from django.shortcuts import render

# Create your views here.
from django.views import View
from ..models.livro import *
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

class GerenciarLivro(view):
    def get(self, request, *args, **kwargs):
        ... 

    