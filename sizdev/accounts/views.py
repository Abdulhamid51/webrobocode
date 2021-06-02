from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic.base import View

import rstr

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.models import User
from .models import *
from main.models import Category, Posts
from .forms import *
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.

class UserProfileView(LoginRequiredMixin, View):
    def get(self, request):
        profile = request.user
        context = {'pro':profile}
        return render(request, 'profile.html',context)


class Register(View):
	def get(self,request):
		form = RegisterForm()
		context = {'form':form}
		return render(request,'auth_register.html', context)

	def post(self,request):
		form = RegisterForm(request.POST)
		if form.is_valid():
			print('@'*50)
			u = form.save()
			try:
				user = UserProfile.objects.create(user=u)
				user.save()
				HttpResponseRedirect('/')
			except:
				user = None
				HttpResponseRedirect('/')
		else:
			print('@'*50)
			form = RegisterForm()

		context = {'form':form}
		return render(request,'auth_register.html', context)


class UpdateProfileView(LoginRequiredMixin, UpdateView):
	model = UserProfile
	fields = ['job','birth','place','phone','python','php','js','java','c','edu','work','bio']
	class_form = UpdateProfileForm
	template_name = 'update_pro.html'
	success_url = "/accounts/profile"
	

class AddPosts(View):
	def get(self, request):
		return render(request, 'add_post.html')

	def post(self, request):
		if request.method == 'POST':
			title = request.POST['title']
			body = request.POST['body']
			Posts.objects.create(
				title=title,
				body=body,
				category=None,
				admin=request.user,
				post_slug=rstr.rstr(title.replace(' ','%'),20)
			)
		return render(request,'add_post.html')

def user_detail(request,user_detail):
	user_d = get_object_or_404(User,username=user_detail)
	return render(request, 'usr_detail.html',{'user':user_d})