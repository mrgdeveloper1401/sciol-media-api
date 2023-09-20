from django.contrib import admin
from .models import User, RecycleUser
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


@admin.register(RecycleUser)
class RecycleUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_active']

@admin.register(User)
class UsersAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", 'mobile')}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ("username", 'id', "email", "first_name", "last_name", "is_staff")

