from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm

# Create your views here.


# ## 회원가입
class Registration(View):
    def get(self, request):
        # 로그인한 상태일때 보여주는 페이지
        if request.user.is_authenticated:
            return redirect('blog:list')
        form = RegisterForm()
        context = {
            'title': 'User',
            'form': form,
        }
        return render(request, 'user/user_register.html', context)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('user:login')


# ## 로그인
class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('blog:list')
        form = LoginForm()
        context = {
            'title': 'User',
            'form': form,
        }
        return render(request, 'user/user_login.html', context)

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('blog:list')
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect('blog:list')

        form.add_error(None, '아이디가 없습니다.')
        context = {
            'title': 'User',
            'form': form,
        }
        return render(request, 'user/user_login.html', context)


# ## 로그아웃
class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('blog:list')
