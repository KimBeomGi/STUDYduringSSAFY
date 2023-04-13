from django.shortcuts import render

# Create your views here.
def go(request):
    return render(request, 'articles/go.html')

def index(request):
    return render(request, 'articles/index.html')