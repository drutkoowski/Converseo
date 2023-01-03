from django.contrib import admin
from accounts.models import UserProfile, Account

# Register your models here.

admin.site.register(Account)
admin.site.register(UserProfile)