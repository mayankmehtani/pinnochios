from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from . import forms
from . import models
#from models import User 

def index(request):
    if not request.user.is_authenticated:
        return render(request, "users/login.html")
    
    context = {
        "user": request.user
    }
    return render(request, "users/user.html", context)

def menu(request):
    return render(request, "users/menu.html")

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
    if request.method == "GET":
        return render(request, "users/signup.html")

def register(request):
    email = request.POST["email"]
    phone_number = request.POST['phone_number']
    username = request.POST['username']
    password = request.POST["password"]
    password_confirm = request.POST["password_confirm"]
    user = models.User.objects.create_user(username, email, phone_number, password)
    login(request, user)
    return HttpResponseRedirect(reverse("index"))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))