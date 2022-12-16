from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader


def index(request):
    if request.user.is_authenticated:
        return HttpResponse(loader.get_template('ethereal/index.html').render())
    else:
        return HttpResponseRedirect('/accounts/login')

