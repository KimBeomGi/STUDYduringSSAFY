from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Article
# Register your models here.
class ArticleAdmin(ModelAdmin):
    fields = ('title','content')
    list_display = ('title','content')

admin.site.register(Article,ArticleAdmin)