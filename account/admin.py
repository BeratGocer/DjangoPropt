from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import customUserModel

@admin.register(customUserModel)
class customAdmin(UserAdmin):
    
    list_display = ("username", "email")
    fieldsets = UserAdmin.fieldsets + (
        ("Avatar degistirme alani", {
            "fields": ["avatar"]
        }),
    )
