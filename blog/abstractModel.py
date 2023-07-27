from django.db import models

class DataAbstarctModel(models.Model):
    olusturulmaTarihi = models.DateTimeField(auto_now_add=True)
    duzenlenmeTarihi = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
