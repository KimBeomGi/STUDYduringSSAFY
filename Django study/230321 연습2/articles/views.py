from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.

# 목록 화면
def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles
    }
    return render(request, 'articles/index.html', context)

# 게시글 작성
def create(request):
    if request.method == 'POST':
        form = ArticleForm(data=request.POST, files=request.FILES)
        if form.is_valid():     # form에 값이 있으면
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context={
        'form':form
    }
    return render(request, 'articles/create.html', context)

# 게시글 세부 내용 확인
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article':article
    }
    return render(request, 'articles/detail.html', context)

# 게시글 수정
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():     # form에 값이 있으면
            form.save()
            return redirect('articles:detail', pk)
    else:
        form = ArticleForm(instance=article)
        context = {
            'article':article,
            'form':form,
        }
        return render(request, 'articles/update.html', context)

# 게시글 삭제
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
    return redirect('articles:index')