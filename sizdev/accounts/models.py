from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import IPAddressField
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.

class Jobs(models.Model):
    name = models.CharField('Kasbingiz', max_length=150)
    job_slug = models.SlugField('slug')

    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'

    def __str__(self):
        return self.name
        

class Skills(models.Model):
    name = models.CharField('skills', max_length=100)
    skill_slug = models.SlugField('slug')

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name
        

class Degree(models.Model):
    degree = models.PositiveIntegerField('degree')
    skills = models.ForeignKey(Skills, verbose_name=("degree_skills"), on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Degree'
        verbose_name_plural = 'Degree'

    def __str__(self):
        return str(self.degree)
        

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile', null=True)
    avatar = models.ImageField('avatar image', upload_to='user_avatars/', null=True, blank=True)
    job = models.ForeignKey(Jobs, related_name=("jobs"), on_delete=models.PROTECT, null=True, blank=True)
    birth = models.DateField("Tug'ilgan Kuningiz", auto_now=False, auto_now_add=False, null=True, blank=True)
    place = models.CharField('place', max_length=250, null=True, blank=True)
    phone = models.CharField('Telefon raqam', max_length=25, null=True, blank=True)
    python = models.CharField('Python', max_length=2, blank=True)
    php = models.CharField('PHP', max_length=2, blank=True)
    js = models.CharField('JS', max_length=2, blank=True)
    java = models.CharField('Java', max_length=2, blank=True)
    c = models.CharField('C,C++,C#', max_length=2, blank=True)
    edu = RichTextField("Ta'lim", null=True, blank=True)
    work = RichTextField('Ish', null=True, blank=True)
    bio = RichTextField('Bio', null=True, blank=True)

    class Meta:
        verbose_name = 'User_profile'
        verbose_name_plural = 'User_profiles'

        

    def get_absolute_url(self):
        return reverse("accounts:user_detail", kwargs={"user_detail": self.user.username})
    