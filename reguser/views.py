from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.db import IntegrityError
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
def reguserview(request):
    if request.method == "GET":
        return render(request, 'registration/reguser.html', {'formuser' : UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'registration/reguser.html', {'formuser' : UserCreationForm(), 'error': 'Это имя уже используется'})
        else:
            return render(request, 'registration/reguser.html', {'formuser' : UserCreationForm(), 'error': 'Пароли должны совпадать'})
def loginuserview(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form' : form})
    else:
        form = AuthenticationForm(request.POST)
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        try:
            login(request, user)
            return redirect('home')
        except:
            return render(request, 'registration/login.html',{'form': form, 'error': 'Неверный логин или пароль'})

def logoutuserview(request):
    logout(request)
    return redirect('home')

def profileview(request):
    user_profile = request.user.userprofile
    return render(request, 'profile.html', {'user_profile': user_profile})

def profileupview(request):
    user_profile = request.user.userprofile

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Профиль успешно обновлен')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)
        return render(request, 'profileup.html', {'form': form})

# Create your views here.
