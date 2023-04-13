from django.urls import path
from . import views

urlpatterns = [
    path('<str:product_name>/<int:quantity>', views.price, name='price'),
]