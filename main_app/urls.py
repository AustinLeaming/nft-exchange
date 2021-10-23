from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('nfts/', views.nfts_index, name='index'),
    path('about/', views.about, name='about'),
]