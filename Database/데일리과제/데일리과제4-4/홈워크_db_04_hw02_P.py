# articles/views.py
def likes(request, article_pk):
	article = Article.objects.get(pk=article_pk)
	# if article.__(a)__.filter(pk=request.user.pk).__(b)__():
    #답
    if article.like_users.filter(pk=request.user.pk).exist():
		article.like_users.remove(request.user)
	else:
		# article.like_users.__(c)__(request.user)
        #답
        article.like_users.add(request.user)

	return redirect('articles:index')