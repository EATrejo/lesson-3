from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm


# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                messages.success(request, "You have been logged in!")
                return redirect(request.POST.get('next'))
            else:
                messages.success(request, "You have been logged in!")
                return redirect("home")

        else:
            messages.success(request, "There was an error at login in, please try again")
            return render(request, 'users/login.html')
    else:
        return render(request, 'users/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out, see you soon!")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully registered")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'users/register.html', {'form': form})
    
    return render(request, 'users/register.html', {'form': form})
