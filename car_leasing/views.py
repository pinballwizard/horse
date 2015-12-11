import logging
from flatlease.models import *
from base.models import Client, Document, Passport, Spouse, Relative, Transaction
from car_leasing.models import Car, Model, Brand
from django import forms
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from base.views import TransactionAddForm, DocumentAddForm, PassportAddForm

logger = logging.getLogger(__name__)


class SearchForm(forms.Form):
    search = forms.CharField(max_length=50, required=False)
    search.widget = forms.TextInput(attrs={'class': 'input-field', 'type': 'search'})


class CarAddForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['owner', 'model', 'color', 'man_date', 'mileage',
                  'photo', 'comment']
        labels = {
            'photo': '',
        }
        widgets = {
            'color': forms.TextInput(attrs={
                'class': 'validate',
            }),
            'man_date': forms.DateInput(attrs={
                'class': 'validate datepicker',
                'placeholder': 'дд.мм.гггг',
                'required': True,
            }),
            'comment': forms.Textarea(attrs={
                'class': 'materialize-textarea',
                'rows': 3,
            }),
}


@login_required
def car_search(request):
    data = {
        'cars': Car.objects.all(),
        'search_form': SearchForm(),
        'car_form': CarAddForm(),
    }
    if request.method == 'POST':
        car_form = CarAddForm(request.POST, request.FILES)
        if car_form.is_valid():
            car_form.save()
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            search_str = form.cleaned_data['search']
            q1 = Car.objects.filter(mileage__icontains=search_str)
            q2 = Car.objects.filter(color__icontains=search_str)
            q3 = Car.objects.filter(man_date__icontains=search_str)
            queryset = q1 | q2 | q3
            data['cars'] = queryset
            data['search_form'] = form
    paginator = Paginator(data['cars'], 10)
    page = request.GET.get('page')
    try:
        data['cars'] = paginator.page(page)
    except PageNotAnInteger:
        data['cars'] = paginator.page(1)
    except EmptyPage:
        data['cars'] = paginator.page(paginator.num_pages)
    logger.debug("user use search")
    return render(request, "car_leasing/car_search.html", data)

