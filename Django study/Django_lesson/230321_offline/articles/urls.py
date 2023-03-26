from django.urls import path
from . import views

app_name='articles'
urlpatterns = [
    # 1. 전체 게시글 목록 보기 
    path('index/',views.index, name="index"),  
    # 2. 게시글 하나 보기
    # 상세페이지를 보기 위해서는 어떤 게시글을 보려는지 서버에게 알려주어야 한다.
    path('<int:pk>/',views.detail, name="detail"),  
    # 3. 새 게시글 작성화면 보기 GET
    # 4. 새 게시글 작성하기  POST
    path('create/',views.create, name="create"),  
    # 5. 수정 화면 보기:GET  
    # 6. 수정하기  : POST
    path('update/<int:pk>/',views.update, name="update"),    
    # 7. 삭제하기
    path('delete/<int:pk>/',views.delete, name="delete"),  
]
