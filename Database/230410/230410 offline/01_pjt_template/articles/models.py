from django.db import models
# 모델에서는 아래 방법은 쓰지 않습니다.
# from django.contrib.auth import get_user_model
from django.conf import settings

# Create your models here.
class Article(models.Model):
    # related_name='' 역참조 할 때 사용하기 위함.
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}번째글 - {self.title}'

#########
# 댓글 생성을 위한 클래스
class Comment(models.Model):
    # related_name을 변경해주면 현재 원래이름은 comment_set인데 변경한 그 네임을 참조하겠다라는 게 된다.
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name = 'comments')
    # 위에있는 Article참조하겠다. # Comment자체가 Article의 id를 참조하는데, 만약 이 게시글이 삭제되면
    # 이 것도 삭제할 거임!!!
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
