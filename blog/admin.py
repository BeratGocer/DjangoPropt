from django.contrib import admin
from blog.models import kategoriModel, yaziModel

admin.site.register(kategoriModel)


class yaziAdmin(admin.ModelAdmin):
    search_fields = ("baslik", "icerik")
    list_display = (
        "baslik", "olusturulmaTarihi", "duzenlenmeTarihi"
    )


admin.site.register(yaziModel, yaziAdmin)
