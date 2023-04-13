from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    # 첫 목록 화면
    path('', views.index, name='index'),
    # 생성하기 및 생성 화면
    path('create/', views.create, name='create'),
    # 게시글 상세 조회
    path('<int:pk>/', views.detail, name='detail'),
    # 수정하기 및 수정 화면
    path('<int:pk>/update/', views.update, name='update'),
    # 삭제하기 및 삭제 화면
    path('<int:pk>/delete/', views.delete, name='delete'),
]