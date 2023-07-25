from django.db import models


class IletisimModel(models.Model):
    email = models.EmailField(max_length=250)
    isim_soyisim = models.CharField(max_length=150)
    mesaj = models.TextField()
    olusturulmaTarihi = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = "iletisim"
        verbose_name = "iletişim"
        verbose_name_plural = "iletişim"


    def __str__(self) -> str:
        return self.email
    