from django.urls import path
from blog.views import contact, anasayfa, kategori, yazilarim, detay, yaziEkle, yaziGuncelle

urlpatterns = [
    path("", anasayfa, name="Anasayfa"),
    path("contact", contact, name="iletisim"),
    path("kategori/<slug:kategoriSlug>", kategori, name="kategori"),
    path("yazilarim", yazilarim, name="yazilarim"),
    path("detay/<slug:slug>", detay, name="detay"),
    path("yazi-ekle", yaziEkle, name="yazi-ekle"),
    path("yazi-guncelle/<slug:slug>", yaziGuncelle, name="yazi-guncelle"),
]