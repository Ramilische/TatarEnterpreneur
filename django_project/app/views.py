from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView

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
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        queryset = Company.objects.order_by('-updated_at')[:self.paginate_by]
        return queryset


class AboutView(TemplateView):
    template_name = 'app/about.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'О нас'
        return context


class CompanyView(DetailView):
    model = Company
    template_name = 'app/company.html'
    context_object_name = 'company'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['company'].name
        return context

    def get_object(self, queryset=None):
        return self.get_queryset().get(slug=self.kwargs['company_slug'])


class EnterpreneurView(DetailView):
    model = Enterpreneur
    template_name = 'app/enterpreneur.html'
    context_object_name = 'enterpreneur'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['enterpreneur'].name
        context['companies'] = Company.objects.filter(enterpreneur=context['enterpreneur'])
        return context

    def get_object(self, queryset=None):
        return self.get_queryset().get(pk=self.kwargs['person_id'])
