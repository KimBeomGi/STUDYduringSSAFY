from django.db import models

# Create your models here.
# django에서 다루고자 하는 데이터를 정의
# 우리는 여기서 게시글 정보를 DB에 저장하려고 함.
# 제목과 내용만 먼저 저장해보자.

# 모델을 만들건데? 음. 기본 기능 필요! ORM 관련된 동작을 이 클래스가 해야함.
# ORM 기능은 누가 만들어 놓은 것 재사용 >>> '상속'을 이용해 재사용 할 것.
# Model 클래스를 상속 하자. models 모듀ㅠ에 구현되어 있음.

class Article(models.Model):
    # 속성 = 이 속성이 DB에 어떤 형태로 저장될지 결정
    # 나는 title이라는 것과 content 라는 데이터 속성을 저장할 건데
    # 아래와 같이 저장하겠다.
    title = models.CharField(max_length=20)
    content = models.TextField()