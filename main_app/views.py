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
from .models import Nft, Photo
from .forms import CommentForm
import uuid
import boto3

S3_BASE_URL = 'https://s3.amazonaws.com/'
BUCKET = 'tokenize-nft-app'

# Create your views here.

class NftUpdate(LoginRequiredMixin, UpdateView):
    model = Nft
    fields = ['price', 'description']
    success_url = '/nfts/'
    


    

class NftDelete(LoginRequiredMixin, DeleteView):
    model = Nft
    success_url = '/nfts/'
    




    # def post_remove(request, nft_id):
    #    item = Nft.objects.get(pk=nft_id)
    #    if request.user == item.user:
    #        Nft.objects.filter(id=nft_id).delete()
    #        return redirect('nfts:mynfts')
   


class NftCreate(LoginRequiredMixin, CreateView):
    model = Nft
    fields = ['title', 'description', 'price']
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


def add_photo(request, nft_id):
    photo_file = request.FILES.get('photo-file', None)
    print(nft_id, "id of nft (above if)")
    if photo_file:
        s3 = boto3.client('s3')
        print(s3, "s3 var inside if statement") 
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f'{S3_BASE_URL}{BUCKET}/{key}'
            Photo.objects.create(url=url, nft_id=nft_id)
        except:
            print('Error occurred when uploading file to S3')
    return redirect('detail', nft_id=nft_id)



