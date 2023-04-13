from django.urls import path
from . import views
app_name = 'practices'
urlpatterns = [
    path('index/', views.index, name ='index'),
    path('catch/', views.catch, name ='catch'),
]