from django.forms import ModelForm
from .models import Comment
from django import forms

class CommentForm(ModelForm):
  text = forms.CharField(
  required=False,
  widget=forms.Textarea(
  attrs={"placeholder": "Add a Comment", 'label':''}
  ),
  )
  

  class Meta:
    model = Comment
    fields = ['text', 'rating']
