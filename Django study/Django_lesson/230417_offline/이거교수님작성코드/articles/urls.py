from django.urls import path
from articles import views

urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    #article_pk에 해당하는 댓글을 생성 또는 목록 가져오기 
    path('articles/<int:article_pk>/comments/',views.article_comment_list)
]
