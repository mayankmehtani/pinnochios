from django.urls import path
from . import views as user_view

urlpatterns = [
    path("", user_view.index, name="index"),
    path("login", user_view.login_view, name="login"),
    path("logout", user_view.logout_view, name="logout"),
    path("menu", user_view.menu, name="menu"),
    path("salad", user_view.salad, name="salad"),
    path("pasta", user_view.pasta, name="pasta"),
    path("subs", user_view.subs, name="subs"),
    path("signup", user_view.signup_view, name="signup"),
    path("register", user_view.register, name="register")
]