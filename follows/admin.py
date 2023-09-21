from django.contrib import admin
from .models import RelationUserModel, RecycleRelationUser


@admin.register(RelationUserModel)
class RelationUserModel(admin.ModelAdmin):
    list_display = ('from_user', 'to_user', "create_at")


@admin.register(RecycleRelationUser)
class RecycleRelationAdmin(admin.ModelAdmin):
    ...