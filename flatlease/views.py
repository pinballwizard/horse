import logging
from flatlease.models import FixedProperty
from base.models import Client, Document, Passport, Spouse, Relative, Transaction
from django import forms
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User, Group
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


logger = logging.getLogger(__name__)


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


def calculator(request):
    logger.debug("user use calculator")
    return render(request, 'flatlease/calculator.html')


@login_required
def statistics(request):
    # Починить условие сортировки
    data = {
        'balance': [person.balance() for person in Client.objects.order_by('-pub_date')[0:5]],
        'last_transactions': Transaction.objects.order_by('-pub_date')[0:10],
        'transaction_sum': sum((transaction.count for transaction in Transaction.objects.all())),
        'clients_count': Client.objects.count(),
        'managers_count': User.objects.filter(groups=Group.objects.get(name='managers')).count(),
    }
    return render(request, 'flatlease/statistics.html', data)
