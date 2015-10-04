from django.shortcuts import render
from flatlease.models import *
from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(max_length=50)
    search.widget = forms.TextInput(attrs={'placeholder': 'Поиск...', 'class': 'mdl-textfield__input', 'type': 'text'})


def calculator(request):
    return render(request, 'flatlease/calculator.html')


def addition(request):
    return render(request, 'flatlease/addition.html')


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
