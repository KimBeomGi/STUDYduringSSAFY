from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    # html = '안녕하세요!'
    # return HttpResponse(html)
    
    context = {
        'name':'김범기'
    }
    return render(request, 'articles/hello.html', context)