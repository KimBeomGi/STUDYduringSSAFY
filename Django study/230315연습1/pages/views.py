from django.shortcuts import render

# Create your views here.
def practice(request):
    
    return render(request, 'pages/practice.html')