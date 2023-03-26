from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):

    info = {
        'name': 'aiden',
        'age': '21'
    }
    


    return render(request, 'myapp/index.html', {'info' : info})