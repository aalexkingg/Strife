from django.shortcuts import render
from .forms import InputForm
from django.template import loader
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def login_view(request):
    user = authenticate(request,
                        username=request.POST.get('username'),
                        password=request.POST.get('password'))

    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/home/')
    else:
        if request.user.is_authenticated:
            login(request, user)
            return HttpResponseRedirect('/home/')
        else:
            context = {'form': InputForm}
            return render(request, "accounts/login.html", context)
