from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):   # 인증관련 기능을 가지고 있는 기본 User를 상속받아 사용
    pass