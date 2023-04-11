from .models import Todo
# from django.forms import ModelForm
from django import forms

class TodoForm(forms.ModelForm):
    
    class Meta:
        model = Todo
        # fields = '__all__'
        exclude = ('author',)