from django.db import models

# Create your models here.
class Article(models.Model):
    # title은 문자열 형태야를 말해줌. 최대 몇 자까지 작성 가능한지도 설정해야함.
    title = models.CharField(max_length=20)
    # 이것은 글자수가 정해져있지 않는 필드
    content = models.TextField()