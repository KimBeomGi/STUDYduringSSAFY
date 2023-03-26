from django.shortcuts import render, redirect
# 로그인
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# 회원가입
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, CustomUserChangeForm
# 비밀번호 변경
from django.contrib.auth.forms import PasswordChangeForm
# 비밀번호 변경시 로그인 유지하게하기 위함
from django.contrib.auth import update_session_auth_hash
# 데코레이터 사용하기
from django.views.decorators.http import require_POST, require_safe, require_http_methods

# Create your views here.
def login(request):
    # 로그인 되어있는데 이 페이지로 오면 돌아가 이자식아 하기
    if request.user.is_authenticated:
        return redirect('articles:index')
    # 여기는 로그인을 해보자
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    # 여기는 로그인 화면으로 가보자.
    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('articles:index')

# 회원가입
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/signup.html', context)

@require_http_methods(['POST'])
def delete(request):
    # user = request.user
    # user.delete()
    # auth_logout(request)
    #------
    request.user.delete()
    auth_logout(request)
    return redirect('articles:index')
    #----
    # if request.method == 'POST':
    #     request.user.delete()
    #     auth_logout(request)
    #     return redirect('articles:index')
    # return redirect('articles:index')

def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
    'form':form
    }
    return render(request, 'accounts/update.html', context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form':form
    }
    return render(request, 'accounts/change_password.html', context)