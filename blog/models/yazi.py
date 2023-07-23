from django.db import models
from autoslug import AutoSlugField
from blog.models import kategoriModel
from django.contrib.auth.models import User

class yaziModel(models.Model):
    resim = models.ImageField(upload_to="yaziResimleri")
    baslik = models.CharField(max_length=50)
    icerik = models.TextField()
    olustulumaTarihi = models.DateTimeField(auto_now_add=True)
    duzenlenmeTarihi = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from = "baslik", unique=True)
    kategoriler = models.ManyToManyField(kategoriModel, related_name="yazi")
    yazar = models.ForeignKey(User, on_delete=models.CASCADE, related_name="yazilar")

    class Meta:
        verbose_name = "yazi"
        verbose_name_plural = "yazilar"
        db_name = "yazi"
