from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import customUserModel


class customAdmin(UserAdmin):
    model = customUserModel
    list_display = ("username", "email")
    fieldsets = UserAdmin.fieldsets + (
        ("Avatar degistirme alani", {
            "fields": ["avatar"]
        }),
    )


admin.site.register(customUserModel, customAdmin)
