from django.contrib import admin
from .models import ChatModel, ChatOptionModel


@admin.register(ChatModel)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'to_user', 'create_at')
    

@admin.register(ChatOptionModel)
class ChatOptionAdmin(admin.ModelAdmin):
    ...