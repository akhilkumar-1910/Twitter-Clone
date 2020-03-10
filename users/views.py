from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

app_name = 'users'
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = User(username=username)
            user.set_password(password)
            return redirect('/accounts/login')
        else:
            print(form.errors)
            return redirect('/tweets/home')
    else:
        form = UserCreationForm
        return render(request, 'register.html', context={'form':form})