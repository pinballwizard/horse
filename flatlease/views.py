from django.shortcuts import render, redirect
from flatlease.models import *
from django import forms
import logging
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

logger = logging.getLogger(__name__)

class ClientAddForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['last_name', 'name', 'second_name', 'birthday', 'residence',
                  'phone', 'email', 'photo', 'health', 'workplace', 'work_position',
                  'salary', 'profit', 'monthly_payment', 'comment']
        labels = {
            'photo': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'input-field',
                'required': True,
                'pattern': ".*",
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'input-field',
                'required': True,
            }),
            'second_name': forms.TextInput(attrs={
                'class': 'input-field',
            }),
            'birthday': forms.DateInput(attrs={
                'class': 'datepicker',
            }),
            'residence': forms.TextInput(attrs={
                'class': 'input-field',
            }),
            'phone': forms.TextInput(attrs={
                'type': 'tel',
                'class': 'input-field',
                'required': True,
            }),
            'email': forms.EmailInput(attrs={
                'type': 'email',
                'class': 'input-field',
            }),
            'photo': forms.FileInput(attrs={
                'class': 'file-field input-field',
            }),
            'health': forms.Select(attrs={
                'class': '',
            }),
            'workplace': forms.TextInput(attrs={
                'class': 'input-field',
            }),
            'work_position': forms.TextInput(attrs={
                'class': 'input-field',
            }),
            'comment': forms.Textarea(attrs={
                'class': 'materialize-textarea',
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
                'class': 'input-field',
                'required': True,
                'pattern': ".*",
            }),
            'cost': forms.TextInput(attrs={
                'type': 'text',
                'class': 'input-field',
                'required': True,
            }),
        }


class TransactionAddForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['type', 'count']
        widgets = {
            # 'type': forms.Select(attrs={
            #     'required': True,
            # }),
            # 'count': forms.DecimalField(attrs={
            #     'required': True,
            # }),
        }


class DocumentAddForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['type', 'document']
        widgets = {
            'document': forms.FileInput(attrs={
                'required': True,
            }),
            'type': forms.Select(attrs={
                'required': True,
            }),
        }


class SearchForm(forms.Form):
    search = forms.CharField(max_length=50)
    search.widget = forms.TextInput(attrs={'id': 'search', 'class': 'input-field', 'type': 'search', 'required': 'true'})
    debtor = forms.BooleanField(required=False)
    debtor.widget = forms.CheckboxInput()
    my_clients = forms.BooleanField(required=False)
    my_clients.widget = forms.CheckboxInput()


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
    return render(request, 'flatlease/login.html', data)


def user_logout(request):
    logout(request)
    return render(request, 'flatlease/login.html')


def calculator(request):
    logger.debug("user use calculator")
    return render(request, 'flatlease/calculator.html')


def test_page(request):
    data = {
        'var': User.objects.get(pk=3),
    }
    return render(request, 'flatlease/test.html', data)


@login_required
def client_page(request, client_id):
    client_obj = Client.objects.get(pk=client_id)
    data = {
        'client': client_obj,
        'transactions': client_obj.transaction_set.all(),
        'documents': client_obj.document_set.all(),
        'fixed_property': client_obj.fixedproperty_set.all(),
        'relatives': client_obj.relative_set.all(),
        # 'passport': client_obj.passport,
        # 'spouse': client_obj.spouse,
        'transaction_form': TransactionAddForm(),
        'document_form': DocumentAddForm(),
        'property_form': PropertyAddForm(),
    }
    if request.method == 'POST':
        transaction_form = TransactionAddForm(request.POST)
        if transaction_form.is_valid():
            t = transaction_form.save(commit=False)
            t.owner = client_obj
            t.save()
        document_form = DocumentAddForm(request.POST)
        if document_form.is_valid():
            d = document_form.save(commit=False)
            d.owner = client_obj
            d.save()
        property_form = PropertyAddForm(request.POST)
        if property_form.is_valid():
            d = property_form.save(commit=False)
            d.owner = client_obj
            d.save()
    return render(request, 'flatlease/client.html', data)


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
        client_form = ClientAddForm(request.POST, request.FILES)
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
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            search_str = form.cleaned_data['search']
            q1 = Client.objects.filter(last_name__icontains=search_str)
            q2 = Client.objects.filter(name__icontains=search_str)
            q3 = Client.objects.filter(phone__icontains=search_str)
            queryset = q1 | q2 | q3
            if form.cleaned_data['debtor']:
                for item in queryset:
                    if not item.debt():
                        queryset.exclude(id=item.id)
            if form.cleaned_data['my_clients']:
                for item in queryset:
                    if not item.manager == request.user.is_authenticated():
                        queryset.exclude(id=item.id)
            data['clients'] = queryset
            data['form'] = form
    return render(request, 'flatlease/search.html', data)


@login_required
def statistics(request):
    #Починить условие сортировки
    data = {
        'balance': [person.balance() for person in Client.objects.order_by('-pub_date')[0:5]],
        'last_transactions': Transaction.objects.order_by('-pub_date')[0:10],
        'transaction_sum': sum((transaction.count for transaction in Transaction.objects.all())),
        'clients_count': len(Client.objects.all()),
    }
    return render(request, 'flatlease/statistics.html', data)
