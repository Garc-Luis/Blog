from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from user.forms import SignUpForm


# Create your views here.
class SignUpViews(CreateView):
    form_class = SignUpForm
    template_name = 'login/register.html'



def login(request):
    return HttpResponse('Hola, estas en el login')
