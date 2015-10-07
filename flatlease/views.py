from django.shortcuts import render
from flatlease.models import *
from django import forms


class ClientAddForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'last_name', 'second_name', 'birthday', 'residence',
                  'phone', 'email', 'photo', 'passport', 'deposit', 'comment']
        widgets = {
            'name': forms.TextInput(attrs={
                'type': 'text',
                'class': 'mdl-textfield__input',
                'required': True,
                'pattern': ".*",
            }),
            'last_name': forms.TextInput(attrs={
                'type': 'text',
                'class': 'mdl-textfield__input',
                'required': True,
            }),
            'second_name': forms.TextInput(attrs={
                'type': 'text',
                'class': 'mdl-textfield__input',
            }),
            'birthday': forms.DateInput(attrs={
                'type': 'date',
                'class': 'mdl-textfield__input',
                'required': True,
            }),
            'residence': forms.TextInput(attrs={
                'type': 'text',
                'class': 'mdl-textfield__input',
                'required': True,
            }),
            'phone': forms.TextInput(attrs={
                'type': 'text',
                'class': 'mdl-textfield__input',
                'required': True,
            }),
            'email': forms.EmailInput(attrs={
                'class': 'mdl-textfield__input',
            }),
            'comment': forms.Textarea(attrs={
                'type': 'text',
                'class': 'mdl-textfield__input',
                'rows': 3,
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


def calculator(request):
    return render(request, 'flatlease/calculator.html')


def addition(request):
    data = {
        'add_client_form': ClientAddForm(),
        'add_property_form': PropertyAddForm()
    }
    if request.method == 'POST':
        client_form = ClientAddForm(request.POST)
        if client_form.is_valid():
            print("YES")
            data['add_client_form'] = client_form
            client_form.save()
        else:
            data['add_client_form'] = client_form
    return render(request, 'flatlease/addition.html', data)


def search(request):
    data = {
        'clients': Client.objects.all(),
        'property': FixedProperty.objects.all(),
        'form': SearchForm(),
    }
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search_str = form.cleaned_data['search']
            data['clients'] = Client.objects.filter(last_name__contains=search_str)
            data['property'] = FixedProperty.objects.filter(location__contains=search_str)
            data['form'] = form
    return render(request, 'flatlease/search.html', data)


def statistics(request):
    return render(request, 'flatlease/statistics.html')
