from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def hello1(request, name):
    context ={
        'name':name,
    }
    return render(request, 'articles/hello1.html', context)

def hello2(request, name):
    context ={
        'name':name,
    }
    return render(request, 'articles/hello2.html', context)