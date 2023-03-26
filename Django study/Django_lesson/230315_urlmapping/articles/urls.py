from django.urls import path
from . import views # 나랑 같은 곳에 있는 views를 이용할 거임
app_name = 'articles'
urlpatterns = [
    # path('articles/', include('articles.urls')),
    # articles/index/를 처리하는 것이다.
    path('index/', views.index, name='index'),
    # path('hello/<int:name>/', views.index, name='hello2'),
    path('hello1/<str:name>/', views.hello1, name='hello1'),
    path('hello2/<int:name>/', views.hello2, name='hello2'),
]