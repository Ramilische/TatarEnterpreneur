from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('company/<company_id:int>', views.company, name='company'),
    path('enterpreneur/<person_id:int>', views.enterpreneur, name='enterpreneur'),
]