from rest_framework import serializers
from .models import Actor, Movie, Review

class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'
        
class ActorDetailSerializer(serializers.ModelSerializer):
    class MovieTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)
            
    movies = MovieTitleSerializer(many=True,read_only=True)
    class Meta:
        model = Actor
        fields = '__all__'
            
            
class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'overview')
        
class MovieDetailSerializer(serializers.ModelSerializer):
    class ReviewTitleContentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = ('title','content',)
    
    class ActorNameSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('name',)
    # class ReviewTitleSerializer(ReviewListSerializer):
    #     def to_representation(self,instance):
    #         rep = super().to_representation(instance)
    #         # rep = dict(filter(lambda x : x[0]=='title',rep.items()))
    #         rep.pop('content',None)
    #         rep.pop('movie',None)
    #         rep.pop('id',None)
    #         return rep
    
    actors = ActorNameSerializer(many=True,read_only=True)
    review_set = ReviewTitleContentSerializer(many=True,read_only=True)
    # review_set = serializers.SlugRelatedField(many=True,read_only=True,slug_field='title')
    # actors = ActorListSerializer(many=True,read_only=True)
    # 모델과는 상관없는 데이터도 직렬화에 포함시 킬 수 있다. 
    
    
    class Meta:
        model = Movie
        fields = '__all__'
        
        
        
class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('title', 'content',)
        
        
class ReviewDetailSerializer(serializers.ModelSerializer):
    class MovieTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)
            
    movie = MovieTitleSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'