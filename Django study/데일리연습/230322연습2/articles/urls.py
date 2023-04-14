from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    # 목록보기
    path('', views.index, name='index'),
    # 상세보기
    path('<int:pk>', views.detail, name='detail'),
    # 생성하기
    path('create', views.create, name='create'),
    # 수정하기
    path('<int:pk>/update/', views.update, name='update'),
    # 삭제하기
    path('<int:pk>/delete/', views.delete, name='delete'),
]