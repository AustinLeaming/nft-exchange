from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path('nfts/', views.nfts_index, name='index'),
    path('about/', views.about, name='about'),
    path('accounts/', include('django.contrib.auth.urls')),
]