from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def index(request):
    if not request.user.is_authenticated:
        return render(request, "users/login.html")
    
    context = {
        "user": request.user
    }
    return render(request, "users/user.html", context)

def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))

    if request.method == "GET":
        return render(request, "users/login.html" )
    
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is None:
        return HttpResponse("<h1> Invalid Login Credentials </h1>")
    else:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))

def signup_view(request):
    return render(request, "users/signup.html")
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))