from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST, require_GET

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)


# 사용자가 로그인 한 경우에만 접근할 수 있도록 허용
@login_required
# @require_http_methods(['GET', 'POST'])
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    # 댓글 조회 후에 context에 추가
    comments = article.comments.all()
    context = {
        'article': article,
        'comment_form' : comment_form,
        'comments' : comments
        }
    return render(request, 'articles/detail.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            # article.user = 현재 로그인 된 사용자
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()

    context = {'form': form}
    return render(request, 'articles/create.html', context)


def delete(request, pk):
    # 게시글 작성자와 현재 로그인된 사용자가 다른데, 삭제가 된다.
    # 게시글 작성자와 로그인된 사용자가 같으면 삭제하도록 변경
    article = Article.objects.get(pk=pk)
    if article.user == request.user:
        article.delete()
    return redirect('articles:index')

@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if article.user == request.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', pk=article.pk)
        else:
            form = ArticleForm(instance=article)

        context = {'form': form, 'article': article}
        return render(request, 'articles/update.html', context)
    else:
        return redirect('articles:index')

@login_required
def comment_create(request, article_pk):
    article = Article.objects.get(pk = article_pk)
    # 댓글저장하고, 상세화면으로 넘겨주기
    comment_form = CommentForm(request.POST)
    # Comment.object.create(content = 'test', aritcle=article)
    # comment_form.article = article
    # 위의 주석 필드는 comment가 가지고 있는거지 commentForm은 안가지고 있거든
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)     # >> DB에 저장
        # commit=False를 하면 데이터베이스에 저장은 안되는데 comment객체는 돌려줌
        comment.article = article
        comment.user = request.user
        comment.save()
    return redirect('articles:detail', article_pk)

def comment_delete(request, article_pk, comment_pk):
    # 댓글 삭제하고... 게시글 상세화면으로 돌아가기
    comment = Comment.objects.get(pk=comment_pk)
    if comment.user == request.user:
        comment.delete()
    return redirect('articles:detail', article_pk)

@login_required
@require_POST
# article_pk인 이유도 해당 게시물에 좋아요를 누르게 되는 것이라서.
def likes(request, article_pk):
    # if request.user.is_authenticated:

    # 현재 로그인한 사람이 게시글에 좋아요를 누르고 있는 것.
    # article_pk에 해당하는 게시글의 좋아요 목록에 로그인한 사람을 추가하거나
    # 이미 있다면 삭제(좋아요 취소)
    article = Article.objects.get(pk=article_pk)
    # 만약 request의 user pk를 확인하는데 이게 article.like_users에 존재하면
    if article.like_users.filter(pk=request.user.pk).exists():
        # 제거하기
        article.like_users.remove(request.user)
        # 아니면 추가하기
    else:
        article.like_users.add(request.user)
    return redirect('articles:detail', article_pk)

    # return redirect('articles:detail', article_pk)