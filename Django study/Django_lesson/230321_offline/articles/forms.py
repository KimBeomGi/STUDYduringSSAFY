# 메타 데이터 : 데이터를 설명하기 위한 데이터..?
# 사진 >>> 데이터, 언제 찍혔고, 어디서 직혔고 크기는 얼마고 이런 것들을 일컬음.

from django import forms
from .models import Article

# articles/forms.py(새로생성)
# ModelForm 생성하기
# Form + Model
# 사용자가 입력한 데이터 검증 + ORM 기능 이것이 ModelFomr

class ArticleForm(forms.ModelForm):
    # 어떤 형태의 데이터를 입력을 받을건지 선언
    # Model Article이 가지고 있는 field 이용해서 선언
    class Meta:
        model = Article
        fields = '__all__'