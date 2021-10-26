from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User 



RATINGS = (
    ('1', 'One'),
    ('2', 'Two'),
    ('3', 'Three'),
    ('4', 'Four'),
    ('5', 'Five'),
)


class Nft(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    # file = models.ImageField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # file = models.ImageField() <--just need charfield
    # user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'nft_id': self.id})


class Comment(models.Model):
    text = models.CharField(max_length=150)
    rating = models.CharField(
        max_length=1,
        choices=RATINGS,
        default=RATINGS[0][0]
    )
    
    nft = models.ForeignKey(Nft, on_delete=models.CASCADE)

class Photo(models.Model):
    url = models.CharField(max_length=200)
    nft = models.ForeignKey(Nft, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for nft_id: {self.nft_id} @{self.url}"
