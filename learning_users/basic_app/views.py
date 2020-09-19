from django.shortcuts import render
from .import forms

from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
#from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, "basic_app/index.html")

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = forms.UserForm(data=request.POST)
        profile_form = forms.UserProfileInfoForms(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_picture' in request.FILES:
                profile.profile_picture = request.FILES['profile_picture']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = forms.UserForm()
        profile_form = forms.UserProfileInfoForms()

    return render(request, "basic_app/registration.html",
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('basic_app:index'))

            else:
                return HttpResponse('Account not active')

        else:
            print('Someone tried to login and failed!')
            print("Username: {} and Password: {}".format(username, password))
            return HttpResponse('Invalid login detail supplied!')

    else:
        return render(request, 'basic_app/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('basic_app:index'))

def special(request):
    return HttpResponse('You are logged in')
