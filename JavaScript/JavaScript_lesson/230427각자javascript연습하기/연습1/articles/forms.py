from django import forms
from .models import Comment, Article


class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        # fields = '__all__'
        excludes = ('user', 'like_users',)


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        # fields = '__all__'
        excludes = ('article', 'user',)