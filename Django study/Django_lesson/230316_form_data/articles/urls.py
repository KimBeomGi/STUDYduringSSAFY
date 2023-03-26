from django.urls import path
from . import views
app_name = 'articles'

urlpatterns = [
    path('throwpage/', views.throw, name = 'throw'),
    path('catchpage/', views.catch, name = 'catch'),
]