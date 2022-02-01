from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import *

# Create your views here.

def register(request):
    if request.method == 'POST':
        x = User.objects.create_user(
            username=request.POST['login'],
            password=request.POST['password']
        )
        login(request, x)
        return redirect('login')
    return render(request, 'Register.html')

def plans(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
                ToDo.objects.create(
                        title=request.POST.get('title'),
                        time=request.POST['date-time'],
                        place=request.POST['place'],
                        description=request.POST['description'],
                        status=request.POST['status'],
                        user=request.user
                )
                return redirect('ToDo')
        plans = ToDo.objects.filter(user=request.user)
        return render(request, 'Plan.html', {'pl' : plans})
    else:
        return redirect('login')

def delete_plan(request, num):
    b = ToDo.objects.get(id = num)
    b.delete()
    return  redirect('ToDo')


def LoginView(request):
    if request.method == 'POST':
        users = authenticate(username=request.POST['login'], password=request.POST['password'])
        if users is None:
            return redirect('login')
        else:
            login(request, users)
            return redirect('ToDo')
    return render(request, 'Login.html')

def LogoutView(request):
    logout(request)
    return redirect('login')