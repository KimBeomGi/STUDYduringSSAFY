from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles
    }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == 'POST':
        # title = request.POST.get('title')
        # content = request.POST.get('content')
        # article = Article(title = title, content = content)
        # article.save()
        form = ArticleForm(data=request.POST, files=request.FILES)
        if form.is_valid():     # form에 값이 있으면
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form':form
    }
    return render(request,'articles/create.html', context)
    
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article':article
    }
    return render(request, 'articles/detail.html', context)
    
def update(request, pk):
    article = Article.objects.get(pk=pk)
    # if request.method == 'POST':
    #     article.title = request.POST.get('title')
    #     article.content = request.POST.get('content')
    #     article.save()
    #     return redirect('articles:detail', pk)

    # 여기서만의 예로 보게 되면 POST의 경우는 해당 update 페이지에서 작성을 해서 넘길때
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', pk)

    # 여기서만의 예로 보게 되면 POST외의 경우에는 타 페이지에서 update 페이지로 넘어올때
    else:
        form = ArticleForm(instance=article)
        context ={
            'article':article,
            'form':form,
        }
        return render(request,'articles/update.html', context)

def delete(request,pk):
    article = Article.objects.get(pk=pk)
    if request.method =='POST':
        article.delete()
    return redirect('articles:index')