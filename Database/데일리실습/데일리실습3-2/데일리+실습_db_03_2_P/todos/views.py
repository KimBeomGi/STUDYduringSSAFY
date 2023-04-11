from django.shortcuts import render, redirect
from .models import Todos
from accounts.models import User
from .forms import TodosForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

# Create your views here.

@ login_required
def index(request):
    todos = Todos.objects.all()
    user = User.objects.all()
    context = {
        'todos' : todos,
        'user' : user
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


def toggle(request, pk):
    todo = Todos.objects.get(pk=pk)
    if request.user == todo.author:
        if request.method == 'POST':
            if todo.Completed == False:
                todo.Completed = True
            elif todo.Completed == True:
                todo.Completed = False
            todo.save()
            return redirect('todos:index')
    else:
        return redirect(request,'todos/index.html')

@require_http_methods(['POST'])
def delete(request, pk):
    todo = Todos.objects.get(pk=pk)
    if request.method == 'POST':
        if request.user == todo.author:
            todo.delete()
    return redirect('todos:index')