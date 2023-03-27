from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .models import Item
from .forms import ItemForm


@require_safe
def index(request):
    items = Item.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'shops/index.html', context)

# 문제 5. 글을 생성하면 발생하는 에러를 수정하여 detail 페이지로 이동하도록 하시오.
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            # shops의 index.html을 보게되면 아래와 같은 코드가 있다.
            # <a href="{% url 'shops:detail' item.id %}">show detail</a>
            # 여기서도 볼 수 있듯이 item.id가 주어지므로 
            # 기존의 return redirect('shops:detail') 가 아닌 item.id를 추가해주었다.
            return redirect('shops:detail', item.id)
    else:
        form = ItemForm()

    context = {
        'form': form,
    }
    return render(request, 'shops/create.html', context)


@require_safe
def detail(request, pk):
    item = Item.objects.get(pk=pk)
    context = {
        'item': item,
    }
    return render(request, 'shops/detail.html', context)


# 문제 6. 글 수정이 아닌 새롭게 생성되고 있다. 이를 수정하시오.
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    # 해당문제에서는 ItemForm에 instance=item을 추가해주면 된다.
    # item은 if문 위에서 정의되고 있으므로,
    # 기존 가지고 있는 값인 itme값을 그대로 받아와야하기에 instance=item을 추가해줌으로
    # 가지고 있었던 문제점을 해결해주었다.
    item = Item.objects.get(pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('shops:detail', pk)
    else:
        form = ItemForm(instance=item)
    
    context = {
        'form': form,
        'pk': pk,
    }
    return render(request, 'shops/update.html', context)


@require_POST
def delete(request, pk):
    item = Item.objects.get(pk=pk)
    item.delete()
    return redirect('shops:index')