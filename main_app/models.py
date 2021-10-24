from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Nft(models.Model):
    Title = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Price = models.IntegerField()
    Ffile = models.ImageField()

class Comment(models.Model):
    text: models.CharField(max_length=150)

    
def __str__(self):
    return self.model

def get_absolute_url(self):
    return reverse('detail', kwargs={'nft_id': self.id})



nft = models.ForeignKey(Nft, on_delete=models.CASCADE)


