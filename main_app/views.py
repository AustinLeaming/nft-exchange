from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Nft
from django.contrib.auth import forms  
from django.contrib import messages  
from .forms import CustomUserCreationForm  
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Nft
from .forms import CommentForm

# Create your views here.

class NftUpdate(LoginRequiredMixin, UpdateView):
    model = Nft
    fields = ['price']

class NftDelete(LoginRequiredMixin, DeleteView):
    model = Nft
    success_url = '/nfts/'

class NftCreate(LoginRequiredMixin, CreateView):
    model = Nft
    fields = '__all__'
    success_url = '/nfts/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)




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






def home(request):
    return render(request, 'home.html')
    # ^ change to render when home page design comes in

@login_required
def nfts_detail(request, nft_id):
    nft = Nft.objects.get(id=nft_id)
    comment_form = CommentForm()
    return render(request, 'nfts/detail.html', {
    'nft': nft, 'comment_form': comment_form
    })

@login_required
def nfts_index(request):
    nfts = Nft.objects.all()
    return render(request, 'nfts/index.html', {'nfts': nfts})

def about(request):
    return render(request, 'about.html')


@login_required
def add_comment(request, nft_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.nft_id = nft_id
        new_comment.save()
    return redirect('detail', nft_id=nft_id)





