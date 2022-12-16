from django.shortcuts import render
from .forms import InputForm, RegistrationForm, TwoFactorAuthenticationForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.db.models import F
from .models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
def login_view(request):

    if request.method != 'POST':
        context = {'form': InputForm}
        return render(request, "accounts/login.html", context)

    user = authenticate(request,
                        username=request.POST.get('username'),
                        password=request.POST.get('password'))
    words = authenticate(request,
                         word1=request.POST.get('word1'),
                         word2=request.POST.get('word2'),
                         word3=request.POST.get('word3'))

    print(request.POST)
    print(user)
    print(words)

    # Sort out 3 tries and account password gets reset (num of tries should be added to database, reset after successful login)
    # Sort out groups and user permissions
    # Root user should be the only user to log in using admin (32+ length password)
    # Create automated way of creating new users, as through the admin page doesn't work
    # Need to hash the three security words similar to password

    if request.POST.get('username') == 'root':
        context = {'form': InputForm}
        #return render(request, "accounts/login.html", context)

    # If user is not logged in
    if (user is not None) or (words is not None):
        if user is not None:
            print("test1")
            context = {'form': TwoFactorAuthenticationForm}
            return render(request, "accounts/2FA_login.html", context)

        else:
            print("test2")
            login(request, user)
            return HttpResponseRedirect('/home/')

    # Else is triggered if incorrect or no POST (user already logged in)
    else:
        if request.user.is_authenticated:
            # If user is already logged in and tries to access login page
            print("test3")
            login(request, user)
            return HttpResponseRedirect('/home/')
        else:

            # Increment invalid logins for 'username', if login_attempts>2, set disabled to true

            #if User.objects.filter(username=request.POST.get('username')).select_related('login_attempts') > 2:
             #   User.objects.filter(username=request.POST.get('username')).update(disabled=1)

            #User.objects.filter(username=request.POST.get('username')).update(login_attempt=F("login_attempts")+1)

            print("test4")
            context = {'form': InputForm}
            return render(request, "accounts/login.html", context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login')


def register_view(request):

    if not request.user.is_superuser:
        context = {'form': InputForm}
        #return render(request, "accounts/login.html", context)


# firstly passwords should be hashed and compared
# If successful, username and password saved and user
#   directed to secure word view
# Then everything should be added to database and user
#   redirected to login page

# Then develop custom url link
#   'accounts/register?code=....'
# function should then match POST code to generate code
# Every time link is generated ALL other codes must be destroyed

    if request.method == 'POST':  # And code matches generated code
        print(1)
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print("test")
            user = form.save()
            user.refresh_from_db()

            user.save()
            raw_password = form.cleaned_data.get('password')

            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            return HttpResponseRedirect('/home')

        else:
            # print validation error in red
            # 
            return render(request, 'accounts/register.html', {'form': RegistrationForm})

    else:
        return render(request, 'accounts/register.html', {'form': RegistrationForm})

