from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
from .models import Article, Comment, Hashtag
from .forms import ArticleForm, CommentForm

# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.order_by('-pk')
    
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        articles = Article.objects.all()
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            # 교수님이 작성해주셨음
            words = article.content.split()
            for word in words:
                if word[0] == '#':  
                    # if word not in articles.hashtags:
                    # Hashtag.objects.get(content=word)
                    if not Hashtag.objects.filter(content = word).exists(): 
                        hash_tag = Hashtag(content=word)
                        hash_tag.save()
                    else:
                        hash_tag = Hashtag.objects.get(content = word)
                    article.hashtags.add(hash_tag)
                
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@require_safe
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)


@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user.is_authenticated:
        if request.user == article.user: 
            article.delete()
            return redirect('articles:index')
    return redirect('articles:detail', article.pk)


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)


@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
        return redirect('articles:detail', article.pk)
    return redirect('accounts:login')


@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('articles:detail', article_pk)

def hashtag(request, hash_pk):
    # hashtagings = Hashtag.objects.order_by('-pk')
    # articles = Article.objects.order_by('-pk')
    hashtag = Hashtag.objects.get(pk=hash_pk)
    articles = hashtag.article_set.all()
    # article = get_object_or_404(Article, pk=article_pk)
    # comments = article.comment_set.all()
    
    context = {
        'hashtag' : hashtag,
        # 'hashtagings' : hashtagings,
        'articles' : articles,
        # 'comments' : comments
    }
    return render(request, 'articles/hashtag.html', context)