from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('<h1>HOME PAGE</h1>')
    # ^ change to render when home page design comes in

def about(request):
    return render(request, 'about.html')
