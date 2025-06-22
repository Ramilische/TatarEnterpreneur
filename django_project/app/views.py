from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.views.generic import ListView

from .models import Company, Enterpreneur


# Create your views here.


def index(request: HttpRequest):
    return redirect('home')


class MainPageView(ListView):
    model = Company
    template_name = 'app/homepage.html'
    context_object_name = 'companies'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(self).get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        queryset = Company.objects.all()
        return queryset


def about(request: HttpRequest):
    pass


def company(request: HttpRequest, company_id: int):
    org = Company.objects.get(pk=company_id)
    context = {
        'company': org,
        'title': org.name,
    }
    return render(request, 'app/company.html', context=context)


def enterpreneur(request: HttpRequest, person_id: int):
    person = Enterpreneur.objects.get(pk=person_id)
    context = {
        'enterpreneur': person,
        'title': person.name,
    }
    return render(request, 'app/enterpreneur.html', context=context)
