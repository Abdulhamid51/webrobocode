# Generated by Django 3.2 on 2021-05-27 05:49

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Kasbingiz')),
                ('job_slug', models.SlugField(verbose_name='slug')),
            ],
            options={
                'verbose_name': 'Job',
                'verbose_name_plural': 'Jobs',
            },
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='skills')),
                ('skill_slug', models.SlugField(verbose_name='slug')),
            ],
            options={
                'verbose_name': 'Skill',
                'verbose_name_plural': 'Skills',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='user_avatars/', verbose_name='avatar image')),
                ('birth', models.DateField(blank=True, null=True, verbose_name="Tug'ilgan Kuningiz")),
                ('place', models.CharField(blank=True, max_length=250, null=True, verbose_name='place')),
                ('phone', models.CharField(blank=True, max_length=25, null=True, verbose_name='Telefon raqam')),
                ('python', models.CharField(max_length=2, verbose_name='Python')),
                ('php', models.CharField(max_length=2, verbose_name='PHP')),
                ('js', models.CharField(max_length=2, verbose_name='JS')),
                ('java', models.CharField(max_length=2, verbose_name='Java')),
                ('c', models.CharField(max_length=2, verbose_name='C,C++,C#')),
                ('edu', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name="Ta'lim")),
                ('work', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Ish')),
                ('bio', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Bio')),
                ('job', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='jobs', to='accounts.jobs')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User_profile',
                'verbose_name_plural': 'User_profiles',
            },
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.PositiveIntegerField(verbose_name='degree')),
                ('skills', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.skills', verbose_name='degree_skills')),
            ],
            options={
                'verbose_name': 'Degree',
                'verbose_name_plural': 'Degree',
            },
        ),
    ]