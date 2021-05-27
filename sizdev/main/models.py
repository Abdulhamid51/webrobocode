from django.db import models
from ckeditor.fields import RichTextField
from accounts.models import UserProfile
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Posts(models.Model):
	admin = models.ForeignKey(User, verbose_name=("user_posts"), on_delete=models.CASCADE)
	title = models.CharField('title', max_length=250)
	body = RichTextField('body')
	bg_image = models.ImageField('bg-image', upload_to='post_image/')
	post_slug = models.SlugField('slug', unique=True)

	class Meta:
		verbose_name = 'Post'
		verbose_name_plural = 'Posts'

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("main:post_detail", kwargs={"post_slug": self.post_slug})