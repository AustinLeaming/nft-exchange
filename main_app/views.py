from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Nft
from django.contrib.auth import forms  
from django.contrib import messages  
from .forms import CustomUserCreationForm  





# Create your views here.


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/nfts')
        else:
            error_message = 'Invalid sign up - try again'
        form = CustomUserCreationForm()
        context = {'form': form, 'error_message': error_message}
        return render(request, 'registration/signup.html', context)
    form = CustomUserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)




class CatCreate(LoginRequiredMixin, CreateView):
    model = Nft
    fields = ['title', 'email', 'price', 'ffile']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)




class Nft:
    def __init__(self, title, owner, price):
        self.title = title
        self.owner = owner
        self.price = price

nfts = [
    Nft('Grizzly bear eating a fish', 'Austin', 2),
    Nft('Shapes', 'David', 4),
    Nft('spongebob meme', 'Harry', 3)
]
def home(request):
    return render(request, 'home.html')
    # ^ change to render when home page design comes in

def nfts_index(request):
    return render(request, 'nfts/index.html', {'nfts': nfts})

def about(request):
    return render(request, 'about.html')







