from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def index(request):
    if request.method == 'POST':
        a = request.POST.get('username')
        b = request.POST.get('passsword')

        user = authenticate(request, username=a, password=b)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'index.html', {'error': 'Invalid username or password'})

    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        a = request.POST.get('username')
        b = request.POST.get('passsword')

        if User.objects.filter(username=a).exists():
            return render(request, 'register.html', {'error': 'Username already exists'})

        User.objects.create_user(username=a, password=b)
        return redirect('index')

    return render(request, 'register.html')


def dashboard(request):
    return render(request, 'dashboard.html')