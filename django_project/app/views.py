from django.shortcuts import render, redirect
from django.http import HttpRequest

from .models import Company


# Create your views here.


def index(request: HttpRequest):
    return redirect('home')


def home(request: HttpRequest):
    context = {
        'companies': Company.objects.all(),
    }
    return render(request, 'app/homepage.html', context=context)


def about(request: HttpRequest):
    pass


def company(request: HttpRequest, company_id: int):
    context = {
        'company': Company.objects.get(pk=company_id),
    }
    return render(request, 'app/company.html', context=context)
