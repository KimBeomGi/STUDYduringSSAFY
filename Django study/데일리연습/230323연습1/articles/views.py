from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
# from .forms

# Create your views here.
# 목록보기
def index(request):
    articles = Article.objects.all()
    context= {
        'articles':articles
    }
    return render(request, 'articles/index.html', context)

# 생성하기
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form':form
    }
    return render(request, 'articles/create.html', context)

# 세부내용보기
def detail(request,pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article':article
    }
    return render(request, 'articles/detail.html', context)


# 수정하기
def update(request,pk):
    article = Article.objects.get(pk=pk)
    if request.method =='POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article:detail', pk=article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form':form,
        'article':article
    }
    return render(request, 'articles/update.html', context)

# 삭제하기
def delete(request,pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')