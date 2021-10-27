from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('nfts/', views.nfts_index, name='index'),
    path('nfts/<int:nft_id>/', views.nfts_detail, name='detail'),
    path('nfts/create/', views.NftCreate.as_view(), name='nfts_create'),
    path('nfts/<int:pk>/update/', views.NftUpdate.as_view(), name='nfts_update'),
    path('nfts/<int:pk>/delete/', views.NftDelete.as_view(), name='nfts_delete'),
    path('nfts/<int:nft_id>/add_comment/', views.add_comment, name='add_comment'),
    path('accounts/signup/', views.signup, name='signup'),
    path('nfts/<int:nft_id>/add_photo/', views.add_photo, name = 'add_photo'),
    path('profile/', views.profile, name='profile'),
]