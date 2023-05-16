from django import forms

from .models import *

class CommentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['name', 'email', 'body']