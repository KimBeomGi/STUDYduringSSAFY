from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.views.decorators.http import require_http_methods

# Create your views here.
def index(request):
    todos = Todo.objects.all().order_by('-pk')
    context = {
        'todos' : todos
    }
    return render(request, 'todos/index.html',context)

def create(request):
    if request.method == 'POST':
        # request에서 데이터 받아와서 DB에 저장하기
        # todo_form =  TodoForm(request.POST)
        # 좀 더 명확히 하게 하기 위해 data=
        form = TodoForm(data=request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            todo.save()
            # return redirect('todos:detail', todo.pk)
            return redirect('todos:index', todo.pk)

    else:
        # todo를 입력할 수 있는 화면 보여주기
        form =  TodoForm()
    context = {
        'form' : form
    }
    return render(request, 'todos/create.html', context)


def detail(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    context = {
        'todo':todo
    }
    return render(request, 'todos/detail.html', context)


@require_http_methods(['POST'])
def update(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    if todo.author == request.user:
        if todo.completed:
            # 참이면 거짓으로, 거짓이면 참으로.
            todo.completed = not todo.completed
            todo.save()
    else:
        return redirect('todos:index')

@require_http_methods(['POST'])
def delete(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    if todo.author == request.user:
        todo.delete()
    return redirect('todos:index')
