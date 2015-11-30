from django.http import Http404
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
    # id = forms.HiddenField()
    class Meta:
        model = Client
        fields = ['id', 'last_name', 'name', 'second_name', 'birthday', 'residence',
                  'phone', 'email', 'photo', 'health', 'workplace', 'work_position',
                  'salary', 'profit', 'monthly_payment', 'comment']
        labels = {
            'photo': '',
            'health': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'id': 'name',
                'class': 'validate',
                'required': True,
                'pattern': ".*",
            }),
            'last_name': forms.TextInput(attrs={
                'id': 'last_name',
                'class': 'validate',
                'required': True,
            }),
            'second_name': forms.TextInput(attrs={
                'id': 'second_name',
            }),
            'birthday': forms.DateInput(attrs={
                'id': 'birthday',
                'class': 'datepicker',
                'placeholder': 'дд.мм.гггг',
            }),
            'residence': forms.TextInput(attrs={
                'id': 'residence',
            }),
            'phone': forms.TextInput(attrs={
                'type': 'tel',
                'id': 'phone',
                'required': True,
            }),
            'email': forms.EmailInput(attrs={
                'type': 'email',
                'id': 'email',
            }),
            'photo': forms.FileInput(attrs={
                'type': 'file',
            }),
            'health': forms.Select(attrs={
                'class': 'browser-default',
                # 'multiple': True,
            }),
            'workplace': forms.TextInput(attrs={
                'id': 'workplace',
            }),
            'work_position': forms.TextInput(attrs={
                'id': 'work_position',
            }),
            'salary': forms.TextInput( attrs={
               'id': 'salary',
            }),
            'profit': forms.TextInput( attrs={
               'id': 'profit',
            }),
            'monthly_payment': forms.TextInput( attrs={
               'id': 'month_payment',
            }),
            'comment': forms.Textarea(attrs={
                'class': 'materialize-textarea',
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
                'required': True,
                'pattern': ".*",
            }),
            'cost': forms.TextInput(attrs={
                'type': 'text',
                'required': True,
            }),
        }


class TransactionAddForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['type', 'count']
        widgets = {
            'type': forms.Select(attrs={
                'class': 'browser-default',
                'required': False,
            }),
            # 'count': forms.DecimalField(attrs={
            #     'required': True,
            # }),
        }


class DocumentAddForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['type', 'document']
        labels = {
            'type': '',
            'document': '',
        }
        widgets = {
            'document': forms.FileInput(attrs={
                'required': True,
            }),
            'type': forms.Select(attrs={
                'class': 'browser-default',
                'required': True,
            }),
        }


class RelativeAddForm(forms.ModelForm):
    class Meta:
        model = Relative
        fields = ['relation', 'last_name', 'name', 'second_name', 'birthday',
                  'residence', 'phone',]
        labels = {
            'relation': '',
        }
        widgets = {
            'relation': forms.Select(attrs={
                'class': 'browser-default',
            }),
            'name': forms.TextInput(attrs={
                'id': 'name',
                'class': 'validate',
                'required': True,
                'pattern': ".*",
            }),
            'last_name': forms.TextInput(attrs={
                'id': 'last_name',
                'class': 'validate',
                'required': True,
            }),
            'second_name': forms.TextInput(attrs={
                'id': 'second_name',
            }),
            'birthday': forms.DateInput(attrs={
                'id': 'birthday',
                'class': 'datepicker',
                'placeholder': 'дд.мм.гггг',
            }),
            'residence': forms.TextInput(attrs={
                'id': 'residence',
            }),
            'phone': forms.TextInput(attrs={
                'type': 'tel',
                'id': 'phone',
                'required': True,
            }),
        }


class PassportAddForm(forms.ModelForm):
    class Meta:
        model = Passport
        fields = ['number', 'date', 'whom', 'image', 'birthplace', 'registration']
        labels = {
            'image': '',
        }
        widgets = {
            'number': forms.TextInput(attrs={
                'required': True,
            }),
            'date': forms.DateInput(attrs={
                'required': True,
                'class': 'datepicker',
                'placeholder': 'дд.мм.гггг',
            }),
            'whom': forms.Textarea(attrs={
                'required': True,
            }),
            'image': forms.FileInput(attrs={
                'required': True,
            }),
            'birthplace': forms.TextInput(attrs={
                'required': True,
            }),
            'registration': forms.TextInput(attrs={
                'required': True,
            }),
}


class SpouseAddForm(forms.ModelForm):
    class Meta:
        model = Spouse
        fields = ['last_name', 'name', 'second_name', 'birthday', 'residence',
                  'phone', 'workplace', 'work_position', 'salary']
        widgets = {
            'last_name': forms.TextInput(attrs={
                'required': True,
            }),
            'name': forms.TextInput(attrs={
                'required': True,
            }),
            'second_name': forms.TextInput(attrs={
                'required': True,
            }),
            'birthday': forms.DateInput(attrs={
                'class': 'datepicker',
                'placeholder': 'дд.мм.гггг',
                'required': True,
            }),
            'residence': forms.TextInput(attrs={
                'required': True,
            }),
            'phone': forms.TextInput(attrs={
                'type': 'tel',
                'required': True,
            }),
            'workplace': forms.TextInput(attrs={
                'required': True,
            }),
            'work_position': forms.TextInput(attrs={
                'required': True,
            }),
            'salary': forms.TextInput(attrs={
                'required': True,
            }),
}


class SearchForm(forms.Form):
    search = forms.CharField(max_length=50, required=False)
    search.widget = forms.TextInput(attrs={'id': 'search', 'class': 'input-field', 'type': 'search'})
    debtor = forms.BooleanField(required=False, label_suffix='', label="Должники")
    debtor.widget = forms.CheckboxInput()
    my_clients = forms.BooleanField(required=False, label_suffix='', label="Мои клиенты")
    my_clients.widget = forms.CheckboxInput()
    potential = forms.BooleanField(required=False, label_suffix='', label="Потенциальные")
    potential.widget = forms.CheckboxInput()


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
    return redirect('login')


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
    try:
        client_obj = Client.objects.get(pk=client_id)
    except Client.DoesNotExist:
        raise Http404("Клиентов с id = {0} не найдено".format(client_id))

    try:
        passport = client_obj.passport
    except Passport.DoesNotExist:
        passport = None

    try:
        spouse = client_obj.spouse
    except Spouse.DoesNotExist:
        spouse = None

    data = {
        'client': client_obj,
        'transactions': client_obj.transaction_set.all(),
        'documents': client_obj.document_set.all(),
        'fixed_property': client_obj.fixedproperty_set.all(),
        'relatives': client_obj.relative_set.all(),
        'transaction_form': TransactionAddForm(),
        'document_form': DocumentAddForm(),
        'property_form': PropertyAddForm(),
        'relative_form': RelativeAddForm(),
        'passport_form': PassportAddForm(instance=passport),
        'spouse_form': SpouseAddForm(instance=spouse),
    }

    if request.method == 'POST':
        print(request.FILES)
        transaction_form = TransactionAddForm(request.POST)
        if transaction_form.is_valid():
            t = transaction_form.save(commit=False)
            t.owner = client_obj
            t.save()
        document_form = DocumentAddForm(request.POST, request.FILES)
        if document_form.is_valid():
            d = document_form.save(commit=False)
            d.owner = client_obj
            d.save()
        property_form = PropertyAddForm(request.POST)
        if property_form.is_valid():
            d = property_form.save(commit=False)
            d.owner = client_obj
            d.save()
        relative_form = RelativeAddForm(request.POST)
        if relative_form.is_valid():
            r = relative_form.save(commit=False)
            r.owner = client_obj
            r.save()
        passport_form = PassportAddForm(request.POST, request.FILES)
        if passport_form.is_valid():
            p = passport_form.save(commit=False)
            p.owner = client_obj
            p.save()
        else:
            data['passport_form'] = passport_form
        spouse_form = SpouseAddForm(request.POST)
        if spouse_form.is_valid():
            s = spouse_form.save(commit=False)
            s.owner = client_obj
            s.save()
    return render(request, 'flatlease/client.html', data)


@login_required
def add(request):
    data = {
        'add_client_form': ClientAddForm(),
    }
    if request.method == 'POST':
        client_form = ClientAddForm(request.POST, request.FILES)
        if client_form.is_valid():
            client_form.save()
        else:
            data['add_client_form'] = client_form
    return render(request, 'flatlease/update.html', data)


@login_required
def update(request, client_id=None):
    data = {
        'add_client_form': ClientAddForm(),
    }
    if client_id is not None:
        try:
            client = Client.objects.get(pk=client_id)
        except Client.DoesNotExist:
            raise Http404("Клиентов с id = {0} не найдено".format(client_id))
        data['add_client_form'] = ClientAddForm(instance=client)
        data['client_id'] = client_id
    else:
        client = None

    if request.method == 'POST':
        print(request.POST)
        client_form = ClientAddForm(request.POST, request.FILES, instance=client)
        if client_form.is_valid():
            c = client_form.save(commit=False)
            c.manager = request.user
            c.save()
            print(c.id)
            return redirect('client_page', c.id)
        else:
            data['add_client_form'] = client_form
    return render(request, 'flatlease/update.html', data)\


@login_required
def search(request):
    data = {
        'clients': Client.objects.order_by('-pub_date'),
        'property': FixedProperty.objects.all(),
        'form': SearchForm(),
    }
    logger.debug("user use search")
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
                        queryset = queryset.exclude(id=item.id)
            if form.cleaned_data['my_clients']:
                queryset = queryset.filter(manager=request.user)
            if form.cleaned_data['potential']:
                queryset = queryset.filter(document__isnull = True)
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
        'clients_count': Client.objects.count(),
        'managers_count': User.objects.filter(groups=Group.objects.get(name='managers')).count(),
    }
    return render(request, 'flatlease/statistics.html', data)
