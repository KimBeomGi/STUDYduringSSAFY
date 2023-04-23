from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Movie, Actor, Review
from .serializers import MovieListSerializer, MovieDetailSerializer, ActorListSerializer, ActorDetailSerializer, ReviewListSerializer, ReviewDetailSerializer
# Create your views here.

@api_view(['GET'])
def actor_list(request):
    actors = get_list_or_404(Actor)
    serializer = ActorListSerializer(actors, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def actor_detail(request, actor_pk):
    actor = get_object_or_404(Actor,pk=actor_pk)
    serializer = ActorDetailSerializer(actor)
    return Response(serializer.data)

@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie,pk=movie_pk)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)

@api_view(['GET'])
def review_list(request):
    reviews = get_list_or_404(Review)
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review,pk=review_pk)
    if request.method=='GET':
        serializer = ReviewDetailSerializer(review)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer = ReviewDetailSerializer(instance=review,data=request.POST)
        if serializer.is_valid(raise_exception=True):# 오류 알아서 띄워주는 raise_exception=True
            serializer.save()
            return Response(serializer.data)

    elif request.method=='DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def create_review(request, movie_pk):
    movie = get_object_or_404(Movie,pk=movie_pk)
    if request.method=='POST':
        # 리뷰 작성
        serializer = ReviewDetailSerializer(data=request.POST)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie)
            return Response(serializer.data,status=status.HTTP_201_CREATED)