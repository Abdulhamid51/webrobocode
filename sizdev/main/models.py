from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.expressions import OrderBy
from accounts.models import UserProfile
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Category(models.Model):
	name = models.CharField('name', max_length=70)
	c_slug = models.SlugField('*')
	def __str__(self):
		return self.name


class Posts(models.Model):
	admin = models.ForeignKey(User, verbose_name=("user_posts"), on_delete=models.CASCADE)
	category = models.ForeignKey(Category, verbose_name=("category"), on_delete=models.PROTECT, blank=True, null=True)
	user_pro = models.ForeignKey(UserProfile, verbose_name=("user_link"), on_delete=models.PROTECT)
	title = models.CharField('title', max_length=250)
	body = RichTextField('body')
	date = models.DateTimeField('date', auto_now=False, auto_now_add=True)
	post_slug = models.SlugField('slug', unique=True)


	class Meta:
		verbose_name = 'Post'
		verbose_name_plural = 'Posts'
		ordering = ['-date']

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("main:post_detail", kwargs={"post_slug": self.post_slug})