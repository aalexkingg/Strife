from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return HttpResponse(loader.get_template('sage/index.html').render())
    else:
        return HttpResponseRedirect('/accounts/login')
