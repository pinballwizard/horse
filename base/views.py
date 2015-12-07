import logging
from flatlease.models import *
from base.models import Client, Document, Passport, Spouse, Relative, Transaction
from django import forms
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


logger = logging.getLogger(__name__)


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=50)
    username.widget = forms.TextInput(attrs={'placeholder':'Имя пользователя', 'class': 'input-field', 'type': 'text'})
    password = forms.CharField(max_length=50)
    password.widget = forms.PasswordInput(attrs={'placeholder':'Пароль', 'class': 'input-field', 'type': 'password'})


def user_login(request):
    data = {
        'login_form': LoginForm()
    }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('calculator')
    return render(request, 'base/login.html', data)


def user_logout(request):
    logout(request)
    return redirect('login')


def choice(request):
    return render(request, 'base/choice.html')


def test_page(request):
    data = {
        'var': User.objects.get(pk=3),
    }
    return render(request, 'base/test.html', data)