from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def register_page(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data['username']
            messages.success(request, 'Account created successfully. Please Login.')
            return redirect('login')


    context = {'form': form}
    return render(request, 'register.html', context)

def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('notes_app:home')
        else:
            messages.info(request, 'Username OR Password is incorrect')

# def logout_user(request):
#     return redirect('login')


    context = {}
    return render(request, 'login.html', context)
