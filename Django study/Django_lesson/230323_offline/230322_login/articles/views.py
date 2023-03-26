from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article
# Create your views here.
def index(request):
    articles = Article.objects.all()
    context={
        'articles' : articles
    }
    return render(request,'articles/index.html', context)


def detail(request,pk):
    pass

def create(request):
    if request.method=='POST':
        #DB에 저장
        # 요청객체에 데이터가 들어가 있음
        # model.save() >> form.save()
        # 데이터 검증이 가능하기 때문에 modelform을 사용해서 저장
        form = ArticleForm(data=request.POST)
        if form.is_valid(): #정상적인 데이터일때만 저장
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    # form.is_valid() 를 수행했을때 유효하지 않으면
    # 다시 글쓰기 화면으로 보내기 위해서 25~28줄을 내어쓰기
    context={
        'form' : form
    }
    return render(request,'articles/create.html',context)

def update(request,pk):
    pass

def delete(request,pk):
    pass