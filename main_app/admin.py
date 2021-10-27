from django.contrib import admin

# Register your models here.
from .models import Nft, Comment, Photo

admin.site.register(Nft)
admin.site.register(Comment)
admin.site.register(Photo)