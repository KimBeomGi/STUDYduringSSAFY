from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)

@login_required
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = article.comments.all()
    context = {
        'article': article,
        'comment_form' : comment_form,
        'comments' : comments
        }
    return render(request, 'articles/detail.html', context)

@login_required
@require_http_methods(['POST','GET'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            # article 인스턴스가... user 정보만 가지고 있으면 save 가능
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()

    context = {'form': form}
    return render(request, 'articles/create.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if article.user == request.user:
        article.delete()
    return redirect('articles:index')


@login_required
@require_http_methods(['POST', 'GET'])
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

# 댓글 생성
def comment_create(request, article_pk):
    article = Article.objects.get(pk = article_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()
    return redirect('articles:detail', article_pk)

# 댓글 삭제
def comment_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)
    