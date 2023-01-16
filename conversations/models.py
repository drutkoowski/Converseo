from datetime import datetime, timedelta

from django.db import models
from accounts.models import Account


def get_current_date():
    return datetime.today()


def get_expire_date():
    return datetime.today() + timedelta(minutes=1)


# Create your models here.
class Conversation(models.Model):
    users = models.ManyToManyField(Account)
    created_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(Account, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)


class SearchQueue(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=get_current_date)
    expires_at = models.DateTimeField(default=get_expire_date)


class Match(models.Model):
    users = models.ManyToManyField(Account)
    created_at = models.DateTimeField(default=get_current_date)
    expires_at = models.DateTimeField(default=get_expire_date)
    accepted_by = models.ManyToManyField(Account, blank=True, null=True, related_name='accepted')
    declined_by = models.ManyToManyField(Account, blank=True, null=True, related_name='declined')