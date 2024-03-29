from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.decorators import login_required
# from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'accounts/index.html')


# @csrf_exempt
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, request.POST)
        if form.is_valid():
            print("in if")          
            username = form.cleaned_data.get('username')
            print(username)
            password = form.cleaned_data.get('password')
            print(password)
            user = authenticate(request,username=username, password=password)
            print("user ",user)
            if user:
                login(request, user)
                return redirect('dashboard')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})

# @csrf_exempt
def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            print(user.username,user.password)
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')
