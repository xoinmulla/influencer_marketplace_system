from django.shortcuts import render

def profile(request):
    # You can pass context variables, such as user information, to the template
    return render(request, 'accounts/profile.html', {})

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm
from .models import Profile
from django.contrib.auth.models import User

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            Profile.objects.create(user=user, role=form.cleaned_data['role'])
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')  # Change to your dashboard or homepage
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

# views.py
def logout_view(request):
    logout(request)
    return redirect('login')

