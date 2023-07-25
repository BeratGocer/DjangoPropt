from django.db import models
from django.contrib.auth.models import User
from blog.models import yaziModel


class yorumModel(models.Model):
    yazan = models.ForeignKey(User, on_delete=models.CASCADE, related_name="yorum")
    yazi = models.ForeignKey(yaziModel, on_delete=models.CASCADE, related_name="yorumlar")
    yorum = models.TextField()
    olusturulmaTarihi = models.DateTimeField(auto_now_add=True)
    duzenlenmeTarihi = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = "yorum"
        verbose_name = "yorum"
        verbose_name_plural = "yorumlar"

    
    def __str__(self) -> str:
        return self.yazan.username
