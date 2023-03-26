from django.urls import path
from . import views
# app_name = 'prices'

urlpatterns = [
    path('<str:product_name>/<int:quantity>/', views.price, name='price'),
]