from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# 전체 게시글 목록 가지고 와서  템플릿에 전달
def index(request):
    articles = Article.objects.all()
    context={
        'articles' : articles
    }
    return render(request,'articles/index.html',context)

# 게시글 작성화면 보여주기 : GET
# 클라이언트에서 던진 데이터를 받아서, DB에 저장하기 : POST
def create(request):
    if request.method == 'POST':
        # title =request.POST.get('title')
        # content =request.POST.get('content')
        # # print(request.FILES)
        # article = Article(title = title, content=content)
        # article.save()
        form = ArticleForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
        # return render(request,'articles/create.html')
    # GET 요청 받으면...form 객체 만들어서 템플릿에 넣어주기
    else: 
        form = ArticleForm()
    context = {
        'form' : form
    }
    return render(request,'articles/create.html', context)

# 게시글 하나의 상세 정보를 담고 있는 상세페이지 보여주기
def detail(request,pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request,'articles/detail.html',context)

# 게시글 수정화면 보여주기
def edit(request,pk):
    article = Article.objects.get(pk=pk)
    context={
        'article' : article
    }
    return render(request,'articles/edit.html',context)

# 수정 정보 받아서 DB에 수정하고....???? 상세 화면 보여주기
def update(request,pk):
    # 1. DB에서 article 조회하기
    # 2. 요청으로 받은 정보 업데이트하기 
    # 3. 저장하기 
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('articles:detail',pk)
    else:
        context={
            'article' : article
        }
        return render(request,'articles/update.html',context)

def delete(request,pk):
    if request.method == 'POST':
        article = Article.objects.get(pk=pk)
        article.delete()
    return redirect('articles:index')