from django.shortcuts import render, redirect
from .forms import RegistratonForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout


# Create your views here.
def home(request):
    return render(request, 'home.html')


def registration(request):
    if request.method == 'POST':
        fm = RegistratonForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Registration Created Successfully')
            return redirect("/")
    else:
        fm = RegistratonForm()
    return render(request, 'registration.html', {'fm': fm})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "login.html", {"fm": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("/")
