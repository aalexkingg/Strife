# Create your views here.

## Functions that take http requests and return http responses, like html docs

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader


def index(request):
    if request.user.is_authenticated:
        return HttpResponse(loader.get_template('home/index.html').render())
    else:
        return HttpResponseRedirect('/accounts/login')
