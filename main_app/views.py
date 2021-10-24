from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

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
