from django.views.decorators.http import require_http_methods
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
# 이부분 수정함
from django.contrib.auth import login as auth_login

@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            # 이 부분 수정함
            
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)
