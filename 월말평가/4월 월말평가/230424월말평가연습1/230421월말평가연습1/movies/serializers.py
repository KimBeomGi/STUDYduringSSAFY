from rest_framework import serializers
from .models import Actor, Movie, Review

class ActorListserializers(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

## 영화 세부내용
class ActorDetailSerializer(serializers.ModelSerializer):
    class MovieDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)

    movies = MovieDetailSerializer(many=True, read_only=True)
    class Meta:
        model = Actor
        fields = '__all__'


# 영화 리스트
class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'overview',)

# 영화 세부내용
class MovieDetailSerializer(serializers.ModelSerializer):
    class ReviewtitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = ('title', 'content',)

    class ActorNameSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('name',)
    
    actors = ActorNameSerializer(many=True, read_only=True)
    review_set = ReviewtitleSerializer(many=True,read_only=True)
    
    class Meta:
        model = Movie
        fields = '__all__'

# 리뷰 리스트 목록
class ReviewListserializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('title', 'content',)

# 리뷰 세부
class ReviewDetailializers(serializers.ModelSerializer):
    class MovieTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)

    movie = MovieTitleSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'