from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('company/<int:company_id>', views.MainPageView.as_view(), name='company'),
    path('enterpreneur/<int:person_id>', views.enterpreneur, name='enterpreneur'),
]