from django.shortcuts import render
from flatlease.models import *
from django import forms


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
                'type': 'text',
                'class': 'mdl-textfield__input',
                'required': True,
            }),
            'residence': forms.TextInput(attrs={
                'type': 'text',
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


def addition(request, client_id=None):
    data = {
        'add_client_form': ClientAddForm(),
        'add_property_form': PropertyAddForm()
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
