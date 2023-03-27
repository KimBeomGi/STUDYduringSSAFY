from django.urls import path
from . import views

app_name = 'boards'
urlpatterns = [
    path('index/', views.index, name='index'),
]