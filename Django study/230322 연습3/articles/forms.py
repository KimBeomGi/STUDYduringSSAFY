from django import forms
from django.forms import ModelForm
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'placeholder' : '제목을 입력하세요'
            }
        )
    )
    class Meta:
        model = Article
        fields = '__all__'