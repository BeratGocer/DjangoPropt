from django.shortcuts import render, get_object_or_404
from blog.models import yaziModel
from blog.forms import yoruEkleForm


def detay(request, slug):
    yazi = get_object_or_404(yaziModel, slug = slug)
    yorumlar = yazi.yorumlar.all()
    yorumEkle = yoruEkleForm()

    if request.method == "POST":
        yorumEkle = yoruEkleForm(data=request.POST)
        if yorumEkle.is_valid():
            yorum = yorumEkle.save(commit=False)
            yorum.yazan = request.user
            yorum.yazi = yazi
            yorum.save()
            
        yorumEkle = yoruEkleForm()

    return render(request, "pages/detay.html", context={
        "yazi": yazi,
        "yorumlar": yorumlar,
        "yorumEkle": yorumEkle
    })