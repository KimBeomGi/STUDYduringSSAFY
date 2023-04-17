from rest_framework import serializers
from .models import Article, Comment

# 목록 조회용 Article Serializer
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article ',)


# 게시글 상세조회용 Article Serializer 작성
# 게시글 조회할 때, 댓글도 같이 조회하고 싶으면? > 재정의 overriding
class ArticleDetailSerializer(serializers.ModelSerializer):
    # 게시글이 있을 때.. 게시글에 달린 댓글은 어떻게??? 역참조
    # 역참조 매니저를 재정의해서 댓글들 직렬화
    comment_set = CommentSerializer(many=True, read_only=True)
    # 모델과는 상관없는 데이터도 직렬화에 포함시 킬 수 있다.
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    class Meta:
        mode = Article
        # fields = ('id', 'title', 'content')
        fields = '__all___'


    # class ArticleForm(forms.ModelForm):
    #     class Meta:
    #         model = Article
    #         fields = ('id', 'title', 'content')


