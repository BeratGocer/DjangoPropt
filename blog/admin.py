from django.contrib import admin
from blog.models import (
    kategoriModel, yaziModel, yorumModel
)

admin.site.register(kategoriModel)


class yaziAdmin(admin.ModelAdmin):
    search_fields = ("baslik", "icerik")
    list_display = (
        "baslik", "olusturulmaTarihi", "duzenlenmeTarihi"
    )


admin.site.register(yaziModel, yaziAdmin)


class yorumAdmin(admin.ModelAdmin):
    search_fields = ("yazan__username",)
    list_display = (
        "yazan", "olusturulmaTarihi", "duzenlenmeTarihi"
    )


admin.site.register(yorumModel, yorumAdmin)
