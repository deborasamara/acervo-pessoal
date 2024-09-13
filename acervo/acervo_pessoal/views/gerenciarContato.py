from django.shortcuts import render

# Create your views here.
from django.views import View
from ..models.contato import *
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

class GerenciarEmprestimo(View):
    def get(self, request, *args, **kwargs):
        ...