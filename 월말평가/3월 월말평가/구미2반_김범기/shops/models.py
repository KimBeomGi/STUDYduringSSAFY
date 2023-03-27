from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    detail = models.TextField()

    def __str__(self):
        return f'item : {self.name}, price: {self.price}'

