from django import forms
from .models import Post_Model




class Post_Form(forms.ModelForm):
    class Meta :
        model=Post_Model
        fields="__all__"
