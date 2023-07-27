from django.contrib import admin
from blog.models import (
    kategoriModel, yaziModel, yorumModel, IletisimModel
)

admin.site.register(kategoriModel)


@admin.register(yaziModel)
class yaziAdmin(admin.ModelAdmin):
    search_fields = ("baslik", "icerik")
    list_display = (
        "baslik", "olusturulmaTarihi", "duzenlenmeTarihi"
    )


@admin.register(yorumModel)
class yorumAdmin(admin.ModelAdmin):
    search_fields = ("yazan__username",)
    list_display = (
        "yazan", "olusturulmaTarihi", "duzenlenmeTarihi"
    )


@admin.register(IletisimModel)
class IletisimAdmin(admin.ModelAdmin):
    search_fields = ("email",)
    list_display = (
        "email", "olusturulmaTarihi",
    )
