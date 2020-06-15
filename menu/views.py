from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from users.models import Account

# Create your views here.

def home(request):
    context = {}
    return render(request, 'menu/home.html', context)

def about(request):
    context = {}
    return render(request, 'menu/about.html', context)

def menu(request):
    menus = Menu.objects.all()
    context = {
        'menus': menus
    }
    return render(request, 'menu/menu.html', context)

def pricing(request):
    accounts = Account.objects.all()
    plans = Plan.objects.all()
    context = {
        'plans': plans,
        'accounts': accounts
    }
    return render(request, 'menu/pricing.html', context)

