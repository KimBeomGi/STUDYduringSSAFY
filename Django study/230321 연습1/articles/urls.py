from django.urls import path
from . import views

app_name='articles'
urlpatterns = [
    # articles/ 게시글 전체 조회
    path('', views.index, name='index'),
    # 게시글 작성
    path('create/', views.create, name='create'),
    # 게시글 상세조회
    path('<int:pk>/', views.detail, name='detail'),
    # 게시글 수정
    path('<int:pk>/update/', views.update, name='update'),
    # 게시글 삭제
    path('<int:pk>/delete/', views.delete, name='delete'),
]