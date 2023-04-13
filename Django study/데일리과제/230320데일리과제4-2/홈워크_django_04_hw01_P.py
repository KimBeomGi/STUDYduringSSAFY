def create(request):
    title = request.POST.get('title') 
    content = request.POST.get('content')
    article = Article(__(a)__, __(b)__)
    # a: title=tile
    # b: content=content
    # c: article.save()
    __(c)__
    return render(request, 'articles/create.html')