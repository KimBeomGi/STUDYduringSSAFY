from django.db import models
from django.conf import settings

# Create your models here.


class Todos(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Title = models.CharField(max_length=100)
    Completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.Title} - {self.id} 번째 할 일'