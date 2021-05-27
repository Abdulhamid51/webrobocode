from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Skills)
admin.site.register(Degree)
admin.site.register(Jobs)