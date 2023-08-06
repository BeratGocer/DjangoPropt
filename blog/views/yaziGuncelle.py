from django.shortcuts import render, redirect, get_object_or_404
from blog.forms import yaziGuncelleForm
from django.contrib.auth.decorators import login_required
from blog.models import yaziModel

@login_required(login_url="/")
def yaziGuncelle(request, slug):

    yazi = get_object_or_404(yaziModel, slug=slug, yazar = request.user)
    form = yaziGuncelleForm(request.POST or None, files=request.FILES or None, instance=yazi)

    if form.is_valid():
        form.save()
        return redirect("detay", slug=yazi.slug)

    return render(request, "pages/yazi-guncelle.html", context={
        "form": form
    })
