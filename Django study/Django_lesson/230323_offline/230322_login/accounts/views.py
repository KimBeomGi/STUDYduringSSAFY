from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
# 회원가입
from .forms import CustomUserCreationForm, CustomUserChangeForm
# 비밀번호 수정 시 로그인 유지
from django.contrib.auth import update_session_auth_hash
# 데코레이터 사용
from django.views.decorators.http import require_POST, require_safe, require_http_methods


# Create your views here.
@require_http_methods(['GET','POST'])
def login(request):
    #GET 요청을 받으면 화면 보여주기
    #POST 요청을 받으면 로그인 처리하기
    if request.method == 'POST':
        #로그인 처리
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            auth_login(request,form.get_user())
            return redirect('articles:index')
    else:   # GET 요청이라면 로그인 화면보여주기
        #django.contrib.auth.forms.AuthenticationForm
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request,'accounts/login.html',context)

@require_POST
def logout(request):
    if request.method=='POST':
        auth_logout(request)
        return redirect('articles:index')
    
def signup(request):                # 회원가입 화면, 진짜 회원가입
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/signup.html', context)

@require_http_methods(['GET','POST'])
def update(request):
    # request가 현재 로그인된 사용자의 정보를 가지고 있다.ㄴ
    # request.user
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        # 현재 로그인된 사용자의 정보를 담은 form을 만들어야 합니다.
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form':form
    }
    return render(request, 'accounts/update.html', context)

@require_http_methods(['GET','POST'])
def password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            # 기존 세션이 가지고 있던 인증정보를 수정하는 함수
            # 인증정보와 세션정보가 달라서 세션이 무효화되는 것을 막을 수 있음
            update_session_auth_hash(request,form.user)     # => 로그인 유지
            return redirect('articles:index')
        pass
    else:
        form = PasswordChangeForm(user=request.user)
    context = {
        'form':form
    }
    return render(request, 'accounts/change_password.html',context)

# 처음부터 post만 받자. 혹은 get만 받자 등등 데코레이터 이용!
@require_http_methods(['POST'])
def delete(request):
    # DB에서 회원정보 지우기
    # if request.method == 'POST':
    request.user.delete()
    auth_logout(request)
    return redirect('articles:index')
