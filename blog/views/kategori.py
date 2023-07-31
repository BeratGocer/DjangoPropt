from django.shortcuts import render, get_object_or_404
from blog.models import yaziModel, kategoriModel
from django.core.paginator import Paginator

def kategori(request, kategoriSlug):
    kategori = get_object_or_404(kategoriModel, slug=kategoriSlug)

    yazilar = kategori.yazi.order_by("-id")
    sayfa = request.GET.get("sayfa")
    paginator = Paginator(yazilar, 4)
    
    return render(request, "pages/kategori.html", context={
        "yazilar": paginator.get_page(sayfa),
        "kategorisim": kategori.isim
    })
