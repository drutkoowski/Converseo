from django.contrib import admin
from accounts.models import Account, Post, SearchQueue

# Register your models here.

admin.site.register(Account)
admin.site.register(Post)
admin.site.register(SearchQueue)