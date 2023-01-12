from django.contrib import admin
from conversations.models import Conversation, Message, SearchQueue

admin.site.register(Conversation)
admin.site.register(Message)
admin.site.register(SearchQueue)