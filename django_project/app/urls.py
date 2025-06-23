from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.MainPageView.as_view(), name='home'),
    path('about', views.AboutView.as_view(), name='about'),
    path('company/<int:company_id>', views.CompanyView.as_view(), name='company'),
    path('enterpreneur/<int:person_id>', views.EnterpreneurView.as_view(), name='enterpreneur'),
]