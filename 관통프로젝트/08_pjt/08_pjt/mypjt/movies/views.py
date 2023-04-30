from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Movie, Genre
import random

# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies':movies
    }
    return render(request, 'movies/index.html', context)

@require_safe
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    # movie_form = MovieForm(instance=movie)
    context = {
        'movie':movie
    }
    return render(request, 'movies/detail.html', context)


@require_safe
def recommended(request):
    if request.GET.get('genre') == "00":
        return redirect("movies:index")
    genre = Genre.objects.get(pk=request.GET.get('genre'))
    # genre = Genre.objects.get(pk=genre_pk)
    # N:M 관계 Genre와 Movie 에서 Genre의 genre에서 Movie의 genres를 역참조해서 가져온
    movies = genre.movie_set.all()
    # movies = Movie.objects.filter(genres=genre)
    # 추천 영화 10개를 추스려서 가져옴
    
    # print(type(movies))
    movies = list(movies)
    random.shuffle(movies)
    recommended_movies = movies[:10]
    # 선택된 영화 정보를 사용자에게 보여주기
    context = {
        'recommended_movies': recommended_movies,
        'genre' : genre.name,
    }
    return render(request, 'movies/recommended.html', context)