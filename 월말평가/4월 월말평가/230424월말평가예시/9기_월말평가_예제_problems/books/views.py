from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404

from .serializers import BookListSerializer, BookSerializer
from .models import Book

@api_view(['GET', 'POST'])
def book_list(request):
    # Q 1.
    # Q 2.
    pass

