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


logger = logging.getLogger(__name__)


def car_search(request):
    data = {
        'cars': Car.objects.all(),
    }
    return render(request, "car_leasing/car_search.html", data)
