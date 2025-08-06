from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.MainPageView.as_view(), name='home'),
    path('about', views.AboutView.as_view(), name='about'),
    path('enterpreneur/<int:person_id>', views.EnterpreneurView.as_view(), name='enterpreneur'),
    re_path(r'.*', views.index) # все странные запросы переводят на главную страницу
]