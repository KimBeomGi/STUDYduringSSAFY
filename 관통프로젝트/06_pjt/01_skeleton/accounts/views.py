from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import(
    AuthenticationForm,
    UserChangeForm,
    PasswordChangeForm
)


from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash, get_user_model
from .forms import CustomUserChangeForm, CustomUserCreationForm

# Create your views here.

@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('movies:index')
    
    # 진짜 로그인창
    if request.method =='POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'movies:index')
    # 로그인 창 띄우기
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html',context)


@require_POST
def logout(request):
    #로그인 되어있으면 진행하기
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('movies:index')


@require_http_methods(['GET', 'POST'])
def signup(request):
    # 계정 생성하기
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
        return redirect('movies:index')
    # 계정 생성 화면으로 가기
    else:
        form = CustomUserCreationForm()
    context={
        'form':form
    }
    return render(request, 'accounts/signup.html',context)


@require_http_methods(['GET', 'POST'])
def update(request):
    #계정 수정하기
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(request.GET.get('next') or 'movies:index')

    #계정 수정 화면으로 가기
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form':form
    }
    return render(request, 'accounts/update.html', context)


@require_POST
def delete(request):
    # 로그인 되어있어야 삭제가능
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect('movies:index')
        


@require_http_methods(['GET', 'POST'])
def change_password(request):
    # 패스워드 변경
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(request.GET.get('next') or 'movies:index')
    # 패스워드 변경 화면으로 가기
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/change_password.html', context)

@login_required
@require_safe
def profile(request, username):
    # 프로필 화면으로 가기
    person = get_user_model().objects.get(username=username)
    context = {
        'person' : person
    }
    return render(request, 'accounts/profile.html', context)


@require_POST
def follow(request,username):
    # 팔로우 눌렀을때!
    if request.user.is_authenticated:
        person = get_user_model().objects.get(username=username)
        if person != request.user:
            # 팔로우가 되어있으면??
            if person.followers.filter(username=request.user.username).exists():
                person.followers.remove(request.user)
            # 팔로우가 안되어있으면??
            else:
                person.followers.add(request.user)
        return redirect('accounts:profile', username)
    return redirect('accounts:login')