from django.urls import path
from . import views # 나랑 같은 곳에 있는 views를 이용할 거임
app_name = 'pages'
urlpatterns = [
    # path('pages/', include('pages.urls')),
    # pages/index를 처리
    path('index/', views.index, name='index'),
]