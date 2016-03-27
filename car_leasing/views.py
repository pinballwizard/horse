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
from reportlab.pdfgen import canvas
from django.http import HttpResponse


logger = logging.getLogger(__name__)


class SearchForm(forms.Form):
    search = forms.CharField(max_length=50, required=False)
    search.widget = forms.TextInput(attrs={'class': 'input-field', 'type': 'search'})


class CarAddForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['owner', 'model', 'color', 'man_date', 'mileage',
                  'photo', 'comment']
        # labels = {
        #     'photo': '',
        # }
        widgets = {
            'color': forms.TextInput(attrs={
                'class': 'validate',
                'type': 'color',
            }),
            'man_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'validate datepicker',
                'placeholder': 'дд.мм.гггг',
                'required': True,
            }),
            'comment': forms.Textarea(attrs={
                'class': 'materialize-textarea',
                'rows': 3,
            }),
        }


class ModelAddForm(forms.ModelForm):
    class Meta:
        model = Model
        fields = ['brand', 'name', 'year']
        labels = {
            'photo': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'validate',
            }),
            'year': forms.DateInput(attrs={
                # 'type': 'date',
                'class': 'validate',
                'required': True,
            }),
        }


class BrandAddForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'logo']
        labels = {
            'logo': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'validate',
            }),
        }


@login_required
def brand_save(request):
    if request.method == 'POST':
        brand_form = BrandAddForm(request.POST, request.FILES)
        if brand_form.is_valid():
            brand_form.save()
    return redirect('car:search')


@login_required
def update(request, car_id=None):
    if car_id is not None:
        try:
            car = Car.objects.get(pk=car_id)
        except Car.DoesNotExist:
            raise Http404("Автомобилей с id = {0} не найдено".format(car_id))
    else:
        car = None

    data = {
        'car_id': car_id,
        'car_form': CarAddForm(instance=car),
        'brand_form': BrandAddForm(),
        'model_form': ModelAddForm(),
    }

    if request.method == 'POST':
        car_form = CarAddForm(request.POST, instance=car)
        if car_form.is_valid():
            c = car_form.save(commit=False)
            c.manager = request.user
            c.save()
            car_form = CarAddForm(request.POST, request.FILES, instance=c)
            if car_form.is_valid():
                c.save()
            return redirect('car:car_page', c.id)
        else:
            data['add_car_form'] = car_form
    return render(request, 'car_leasing/update.html', data)


@login_required
def car_search(request):
    data = {
        'cars': Car.objects.all(),
        'search_form': SearchForm(),
    }
    if request.method == 'POST':
        car_form = CarAddForm(request.POST, request.FILES)
        if car_form.is_valid():
            car_form.save()
        model_form = ModelAddForm(request.POST)
        if model_form.is_valid():
            model_form.save()

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


@login_required
def car_page(request,car_id):
    try:
        car_obj = Car.objects.get(pk=car_id)
    except Car.DoesNotExist:
        raise Http404("Автомобилей с id = {0} не найдено".format(car_id))

    data = {
        'car': car_obj
    }

    return render(request, "car_leasing/car.html", data)


def car_to_pdf(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="car.pdf"'
    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response