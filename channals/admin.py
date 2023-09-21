from django.contrib import admin
from .models import ChannalModel, PostChannal, RecycleChannal, RecycleChannalOption


@admin.register(ChannalModel)
class ChannalAdmin(admin.ModelAdmin):
    list_display = ('creator', 'channal_name', 'is_active', 'is_publish', 'create_at')
    list_editable = ('is_active', 'is_publish')
    list_filter = ('create_at', 'is_active', 'is_publish')
    filter_horizontal = ('members', )
    
    
@admin.register(RecycleChannal)
class RecycleChannalAdmin(admin.ModelAdmin):
    ...

    
@admin.register(PostChannal)
class ChannalOption(admin.ModelAdmin):
    list_display = ('channal', 'is_active', 'create_at')
    list_filter = ('create_at', )
    list_editable = ('is_active', )
    

@admin.register(RecycleChannalOption)
class RecycleOptionChannalAdmin(admin.ModelAdmin):
    ...