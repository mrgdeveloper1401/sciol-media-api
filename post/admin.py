from django.contrib import admin
from .models import PostModel, PostOptionModel, RecyclePost, TagPostModel


@admin.register(RecyclePost)
class RecyclePostAdmin(admin.ModelAdmin):
    ...
    

@admin.register(PostModel)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('body', )}
    list_display = ('user', 'slug', 'create_at', 'is_active')
    list_filter = ('is_active', )
    list_editable = ('is_active', )
    filter_horizontal = ('post_tag', )
    
@admin.register(TagPostModel)
class TagPostAdmin(admin.ModelAdmin):
    ...
    
    
@admin.register(PostOptionModel)
class PostModelAdmin(admin.ModelAdmin):
    ...


