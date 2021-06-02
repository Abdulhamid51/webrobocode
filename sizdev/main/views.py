from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic.base import View

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.models import User
from .models import *
from accounts.models import UserProfile
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q

# Create your views here.

class HomeView(View):
    def get(self, request):
        posts = Posts.objects.all()
        last = User.objects.all()
        context = {'post':posts,'last':last}
        return render(request, 'index.html', context)

def post_detail(request,post_slug):
    post = get_object_or_404(Posts ,post_slug=post_slug)
    return render(request, 'post_detail.html', {'post':post})