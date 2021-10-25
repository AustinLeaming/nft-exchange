from django.contrib import admin

# Register your models here.
from .models import Nft, Comment

admin.site.register(Nft)
admin.site.register(Comment)