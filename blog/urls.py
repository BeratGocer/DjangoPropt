from django.urls import path
from blog.views import contact, anasayfa

urlpatterns = [
    path("", anasayfa),
    path("contact", contact),
]