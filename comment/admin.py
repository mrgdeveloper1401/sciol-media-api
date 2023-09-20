from django.contrib import admin
from .models import CommentModel, CommentsOptionModel, RecycleComment



class CommentOptionInline(admin.StackedInline):
    model = CommentsOptionModel

@admin.register(CommentModel)
class CommentAdminInline(admin.ModelAdmin):
    model = CommentModel
    list_display = ('id', 'user', 'body', 'create_at', 'is_reply')
    list_filter = ('create_at', 'is_reply')
    search_fields = ('body', 'reply', )
    raw_id_fields = ('user', )
    list_editable = ('is_reply', )
    inlines = [CommentOptionInline]

@admin.register(RecycleComment)
class RecycleCommentAdmin(admin.ModelAdmin):
    pass