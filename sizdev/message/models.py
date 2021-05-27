from django.db import models
from accounts.models import UserProfile
# Create your models here.

class Message(models.Model):
    text_to = models.ForeignKey(UserProfile, related_name=("message_to"), on_delete=models.CASCADE)
    msg_author = models.CharField('author', max_length=150)
    message = models.CharField('message', max_length=10500)

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
