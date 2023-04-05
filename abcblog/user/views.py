from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from user.forms import SignUpForm


# Create your views here.





def login(request):
    return HttpResponse('Hola, estas en el login')

def register(request):
    return HttpResponse('Hola, estas en el register.')
