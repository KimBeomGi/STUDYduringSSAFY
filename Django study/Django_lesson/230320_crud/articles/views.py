from django.shortcuts import render, redirect
from .models import Article         # 나랑 같은 곳에 있는 models에 있는 Article을 사용할 거임.

# Create your views here.

# 전체 게시글 목록 가지고 와서 템플릿에 전달
def index(request):
    articles = Article.objects.all()
    context={
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

# 새 게시글 작성화면 보여주기
def new(request):
    return render(request, 'articles/new.html')

# 클라이언트에 던진 데이터를 받아서, DB에 저장하기
def create(request):
    # DB에 저장하기: QuerySet API 사용하기
    # 요청객체에서 데이터 꺼내서, model 인스턴스에 넣어주고
    # 저장하기
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Article(title = title, content =content)
    article.save()
    # 문제점
    # 1. 목록이 화면에 안보임,
    # 2. url이 create인데, 화면은 index.
    # 해결책 : index화면은 index로 요청해서 보게 하자.
    #       # redirect
    # return render(request, 'articles/index.html')
    return redirect('articles:index')

# 게시글 하나의 상세 정보를 담고 있는 상세페이지 보여주기
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)

# 게시글 수정화면 보여주기
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/edit.html', context)

# 수정정보 받아서 DB에 수정하고...?? 상세화면? 목록 화면?
# 여기선 상세화면을 보여주자.
def update(request, pk):
    #1. DB에서 article 조회하기
    #2. 요청으로 받은 정보 업데이트 하기
    #3. 저장하기
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    
    return redirect('articles:detail', pk)

def delete(request, pk):
    if request.method == 'POST':
        article = Article.objects.get(pk=pk)
        article.delete()
    
    return redirect('articles:index')