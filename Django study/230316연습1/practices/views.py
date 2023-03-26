from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'practices/index.html')

def catch(request):
    return render(request, 'practices/catch.html')