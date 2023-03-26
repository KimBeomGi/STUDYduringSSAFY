from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
# 목록보기
def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles
    }
    return render(request, 'articles/index.html', context)

# 세부내용 보기
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article':article
    }
    return render(request, 'articles/detail.html', context)

# 생성하기
def create(request):
    if request.method == 'POST':
        # DB에 저장
        # 요청 객체에 데이터가 들어가 있음       # model.save() >> form.save()
        # 데이터 검증이 가능하기 때문에 modelform을 사용해서 저장
        form = ArticleForm(data=request.POST)
        if form.is_valid():     # 정상적인 데이터일때만 저장
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    ##### form.is_valid()를 수행했을 때 유효하지않으면 다시 글쓰기 화면으로 보냄.
    # 따라서 아래를 내어쓰기 함.
    context={
        'form':form
    }
    return render(request, 'articles/create.html', context)

# 수정하기
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail',article.pk)
    else:
        form = ArticleForm(instance=article)

    context = {
        'form':form,
        'article':article
    }
    return render(request,'articles/update.html', context)

# 삭제하기
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')