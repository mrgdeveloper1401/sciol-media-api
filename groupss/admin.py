from django.contrib import admin
from .models import GroupModel, GroupOptionModel


@admin.register(GroupModel)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('creator', 'group_name', 'is_active', 'create_at')
    list_editable = ('is_active', )
    list_filter = ('is_active', 'create_at')
    filter_horizontal = ('members', )


@admin.register(GroupOptionModel)
class groupOptionAdmin(admin.ModelAdmin):
    list_display = ('grup', 'is_active', )
    list_editable = ('is_active', )
    list_filter = ('is_active', 'create_at')