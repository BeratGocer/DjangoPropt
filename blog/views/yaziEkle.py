from django.shortcuts import render, redirect
from blog.forms import yaziEkleForm
from django.contrib.auth.decorators import login_required

@login_required(login_url="/")
def yaziEkle(request):
    form = yaziEkleForm(request.POST or None, files=request.FILES or None)

    if form.is_valid():
        yazi = form.save(commit=False)
        yazi.yazar = request.user
        yazi.save()
        form.save_m2m()

        return redirect("detay", slug=yazi.slug)


    return render(request, "pages/yazi-ekle.html", context={
        "form": form
    })
