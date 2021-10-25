from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('nfts/', views.nfts_index, name='index'),
    path('nfts/create/', views.NftCreate.as_view(), name='nfts_create'),
    path('accounts/signup/', views.signup, name='signup'),
]