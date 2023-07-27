from django.db import models
from blog.models import yaziModel
from blog.abstractModel import DataAbstarctModel


class yorumModel(DataAbstarctModel):
    yazan = models.ForeignKey("account.customUserModel", on_delete=models.CASCADE, related_name="yorum")
    yazi = models.ForeignKey(yaziModel, on_delete=models.CASCADE, related_name="yorumlar")
    yorum = models.TextField()


    class Meta:
        db_table = "yorum"
        verbose_name = "yorum"
        verbose_name_plural = "yorumlar"

    
    def __str__(self) -> str:
        return self.yazan.username
