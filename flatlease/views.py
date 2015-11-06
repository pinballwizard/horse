from django.shortcuts import render, redirect
from flatlease.models import *
from django import forms
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm


class ClientAddForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'last_name', 'second_name', 'birthday', 'residence',
                  'phone', 'email', 'photo', 'passport', 'deposit', 'comment']
        labels = {
            'passport': '',
            'photo': '',
            'deposit': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'mdl-textfield__input',
                'required': True,
                'pattern': ".*",
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'mdl-textfield__input',
                'required': True,
            }),
            'second_name': forms.TextInput(attrs={
                'class': 'mdl-textfield__input',
            }),
            'birthday': forms.DateInput(attrs={
                'class': 'mdl-textfield__input',
                'required': True,
            }),
            'residence': forms.TextInput(attrs={
                'class': 'mdl-textfield__input',
                'required': True,
            }),
            'phone': forms.TextInput(attrs={
                'type': 'tel',
                'class': 'mdl-textfield__input',
                'required': True,
            }),
            'email': forms.EmailInput(attrs={
                'type': 'email',
                'class': 'mdl-textfield__input',
            }),
            # 'passport': forms.ImageField(attrs={
            #     'class': '',
            # }),
            # 'photo': forms.ImageField(attrs={
            #     'class': '',
            # }),
            # 'deposit': forms.DecimalField(attrs={
            #     'class': '',
            # }),
            'comment': forms.Textarea(attrs={
                'class': 'mdl-textfield__input',
                'rows': 4,
            }),
        }


class PropertyAddForm(forms.ModelForm):
    class Meta:
        model = FixedProperty
        fields = ['location', 'cost']
        widgets = {
            'location': forms.TextInput(attrs={
                'type': 'text',
                'class': 'mdl-textfield__input',
                'required': True,
                'pattern': ".*",
            }),
            'cost': forms.TextInput(attrs={
                'type': 'text',
                'class': 'mdl-textfield__input',
                'required': True,
            }),
        }


class SearchForm(forms.Form):
    search = forms.CharField(max_length=50)
    search.widget = forms.TextInput(attrs={'placeholder': 'Поиск...', 'class': 'mdl-textfield__input', 'type': 'text'})
    debtor = forms.BooleanField()
    debtor.widget = forms.CheckboxInput()
    my_clients = forms.BooleanField()
    view = forms.BooleanField()


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=50)
    username.widget = forms.TextInput(attrs={'placeholder':'Имя пользователя', 'class': 'mdl-textfield__input', 'type': 'text'})
    password = forms.CharField(max_length=50)
    password.widget = forms.PasswordInput(attrs={'placeholder':'Пароль', 'class': 'mdl-textfield__input', 'type': 'password'})


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
                print(user)
                login(request, user)
                return redirect('calculator')
    return render(request, 'flatlease/login.html', data)


def user_logout(request):
    logout(request)
    return render(request, 'flatlease/login.html')


def calculator(request):
    return render(request, 'flatlease/calculator.html')


@login_required
def addition(request, client_id=None):
    data = {
        'add_client_form': ClientAddForm(),
        'add_property_form': PropertyAddForm(),
    }
    if client_id is not None:
        client = Client.objects.get(pk=client_id)
        data['add_client_form'] = ClientAddForm(instance=client)
    if request.method == 'POST':
        client = Client.objects.get(pk=client_id)
        client_form = ClientAddForm(request.POST, request.FILES, instance=client)
        if client_form.is_valid():
            client_form.save()
        else:
            data['add_client_form'] = client_form
    return render(request, 'flatlease/addition.html', data)


@login_required
def search(request):
    data = {
        'clients': Client.objects.order_by('-pub_date'),
        'property': FixedProperty.objects.all(),
        'form': SearchForm(),
    }
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search_str = form.cleaned_data['search']
            q1 = Client.objects.filter(last_name__icontains=search_str)
            q2 = Client.objects.filter(name__icontains=search_str)
            q3 = Client.objects.filter(phone__icontains=search_str)
            data['clients'] = q1 | q2 | q3
            data['form'] = form
    return render(request, 'flatlease/search.html', data)


@login_required
def statistics(request):
    deposit_str = []
    clients = Client.objects.order_by('-deposit')[0:5]
    for person in clients:
        deposit_str.append(person.deposit)
    print(deposit_str)
    data = {
        'deposit': deposit_str
    }
    return render(request, 'flatlease/statistics.html', data)
