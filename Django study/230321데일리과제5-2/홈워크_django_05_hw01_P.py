def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            title = form.__(a)__#request.POST.get('title')
            content = form.__(b)__#request.POST.get('content')
            article = Article(title=title,content=content)
            __(c)__ # article.save()
            return redirect('articles:detail',article.pk)
    form = ArticleForm()
    context = {
        'form':form
    }
    return render(request,'articles/create.html',context)