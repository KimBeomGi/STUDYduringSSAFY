from django.shortcuts import render, redirect
from .models import Todos
from .forms import TodosForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

# Create your views here.

@ login_required
def index(request):
    todos = Todos.objects.all()
    context = {
        'todos' : todos
    }
    return render(request, 'todos/index.html', context)

@require_http_methods(['POST', 'GET'])
def create(request):
    if request.method == 'POST':
        form = TodosForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            todo.save()
            return redirect('todos:index')
    else:
        form = TodosForm
    context = {
        'form':form
    }
    return render(request, 'todos/create.html', context)