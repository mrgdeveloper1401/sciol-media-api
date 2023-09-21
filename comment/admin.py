from django.contrib import admin
from .models import CommentModel, CommentsOptionModel, RecycleComment, RecycleCommentOption
    
    
@admin.register(CommentModel)
class CommentAdminInline(admin.ModelAdmin):
    model = CommentModel
    list_display = ('id', 'post_id', 'reply_id', 'user', 'body', 'create_at', 'is_reply')
    list_filter = ('create_at', 'is_reply')
    search_fields = ('body', 'reply', )
    raw_id_fields = ('user', )
    list_editable = ('is_reply', )


@admin.register(RecycleComment)
class RecycleCommentAdmin(admin.ModelAdmin):
    pass


@admin.register(CommentsOptionModel)
class CommentOptionAdmin(admin.ModelAdmin):
    pass



@admin.register(RecycleCommentOption)
class RecycleCommentOptionAsmin(admin.ModelAdmin):
    ...