from django.urls import path
from blog.views.contact import contact

urlpatterns = [
    path("contact", contact),
]