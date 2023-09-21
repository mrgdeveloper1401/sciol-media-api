from django.contrib import admin
from .models import ChatModel, ChatOptionModel, RecycleChat, RecycleChatOption


@admin.register(ChatModel)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'to_user', 'create_at')
    
    
@admin.register(RecycleChat)
class RecycleChatAdmin(admin.ModelAdmin):
    ...

@admin.register(ChatOptionModel)
class ChatOptionAdmin(admin.ModelAdmin):
    ...
    
    
@admin.register(RecycleChatOption)
class RecycleChatOption(admin.ModelAdmin):
    ...