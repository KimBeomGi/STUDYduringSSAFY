from django import forms
from .models import Movie
# from django.contrib.auth.forms import *

class MovieForm(forms.ModelForm):
    # class Meta:
    #     model = Movie
    #     fields = '__all__'

    class Meta:
        model = Movie
        # fields = ('title', 'audience', 'genre', 'score', 'poster_url', 'description', 'release_date')
        fields = '__all__'
        widgets = {
            'genre' : forms.Select(choices=[('comedy', '코미디'),('horror', '공포'), ('romance', '로맨스'), ('thriller', '스릴러')]),
            # 또는 'score' : forms.Input(attrs={'Type':'number','step':0.5, 'min':0, 'max':5}),
            'score' : forms.NumberInput(attrs={'step': 0.5, 'min':0, 'max':5}),
            'release_date' : forms.DateInput(attrs={'type':'date'}),
        }