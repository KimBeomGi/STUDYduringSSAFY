from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def login(request):
    # get 요청을 받으면 화면 보여주기
    # POST 요청을 받으면 로그인 처리하기
    if request.method == 'POST':
        #로그인 처리
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:   # GET요청이라면 로그인 화면 보여주기
        #django.contrib.auth.forms.AuthenticationForm
        form = AuthenticationForm()
        context = {
            'form':form
        }
        return render(request,'accounts/login.html', context)
    
def logout(request):
    if request.method =='POST':
        auth_logout(request)
        return redirect('articles:index')