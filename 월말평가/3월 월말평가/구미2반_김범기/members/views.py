from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm


from .forms import CustomUserCreationForm, CustomUserChangeForm

@require_http_methods(['GET', 'POST'])
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('shops:index')
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }
    return render(request, 'members/login.html', context)


@require_POST
def logout(request):
    if not request.user.is_authenticated:
        return redirect('shops:index')
    
    auth_logout(request)
    return redirect('shops:index')


# 문제 1. 회원 가입시 비밀번호가 일치하지 않을 때 발생하는 에러를 수정하시오.
@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('shops:index')
    else:
        form = CustomUserCreationForm()
    # if의 if에서 걸러졌ㄴ을 경우 갈 곳을 받지 못했기에 이 문장 아랫부분에서
    # 받을 수 있도록 기존의 context와 return부분을 앞으로 당겨주었다.
    context = {
        'form': form,
    }
    return render(request, 'members/signup.html', context)

# 문제 3. 회원 탈퇴가 되지 않고 발생하는 에러를 해결하시오.
@require_POST
def delete(request):
    # 기존의 if문에 적혀있던  if not request.user.is_authenticated:에서
    # not을 제거하여 로그인 되어있을 때 작동하도록 해주었으며
    # request.user.delete()와 auth_logout(request)의 순서를 바꾸어주었다.
    # 왜냐하면 logout이 먼저되면 값이 없어서 delete할 수 없기 때문이다.
    if request.user.is_authenticated:   
        request.user.delete()
        auth_logout(request)
        return redirect('shops:index')
    else:
        return redirect('shops:index')



@require_http_methods(['GET', 'POST'])
def update(request):
    if not request.user.is_authenticated:
        return redirect('shops:index')
    
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('shops:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    
    context = {
        'form': form,
    }
    return render(request, 'members/update.html', context)


@require_http_methods(['GET', 'POST'])
def change_password(request):
    if not request.user.is_authenticated:
        return redirect('shops:index')
    
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('shops:index')
    else:
        form = PasswordChangeForm(request.user)

    context = {
        'form': form,
    }
    return render(request, 'members/change_password.html', context)