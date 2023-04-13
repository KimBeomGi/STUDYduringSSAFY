from django.urls import path
from . import views
app_name = 'articles'

urlpatterns = [
    path('practice/', views.practice, name='practice'),
]