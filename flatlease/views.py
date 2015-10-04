from django.shortcuts import render


def calculator(request):
    return render(request, 'flatlease/calculator.html')


def addition(request):
    return render(request, 'flatlease/addition.html')


def search(request):
    return render(request, 'flatlease/search.html')


def statistics(request):
    return render(request, 'flatlease/statistics.html')
