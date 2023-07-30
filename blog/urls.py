from django.urls import path
from blog.views import contact, anasayfa

urlpatterns = [
    path("", anasayfa, name="Anasayfa"),
    path("contact", contact, name="iletisim"),
]