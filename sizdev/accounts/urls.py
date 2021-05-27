from re import template
from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import UserProfile
from .forms import UpdateProfileForm
from django.contrib.auth.models import User

app_name = 'accounts'

urlpatterns = [
    path("profile/", UserProfileView.as_view(), name="profile"),
    path('profile/<pk>', UpdateProfileView.as_view(), name="update_pro"),
    path("login/", LoginView.as_view(template_name='auth_login.html'), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", Register.as_view(), name="register"),
    path("addpost/", AddPosts.as_view(), name="addpost"),
]