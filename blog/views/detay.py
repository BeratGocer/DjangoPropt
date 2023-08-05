from django.shortcuts import render, get_object_or_404
from blog.models import yaziModel


def detay(request, slug):
    yazi = get_object_or_404(yaziModel, slug = slug)
    yorumlar = yazi.yorumlar.all()
    return render(request, "pages/detay.html", context={
        "yazi": yazi,
        "yorumlar": yorumlar
    })