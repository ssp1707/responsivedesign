from django.shortcuts import render

# Create your views here.


def home(request):
    context = {}
    return render(request, 'responsiveapp/home.html', context)


def productsresponsive(request):
    context = {}
    return render(request, 'responsiveapp/productsresponsive.html', context)


def peopleresponsive(request):
    context = {}
    return render(request, 'responsiveapp/peopleresponsive.html', context)


def contactus(request):
    context = {}
    return render(request, 'responsiveapp/contactus.html', context)
