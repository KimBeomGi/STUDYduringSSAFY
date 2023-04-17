from rest_framework import serializers
# from .models import (__(a)__)
from .models import Article # 답


# class ArticleSerializer(__(b)__):
class ArticleSerializer(serializers.ModelSerializer):   # 답

    class Meta:
        model = Article
        # fields = (__(c)__) # 개별 필드를 나열하지 말 것
        fields = '__all__'