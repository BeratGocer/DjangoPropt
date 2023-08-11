from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.forms import profilDuzenlemeForm

@login_required(login_url="/")
def profilDuzenleme(request):

    if request.method == "POST":
        form = profilDuzenlemeForm(request.POST, request.FILES, instance = request.user)

        if form.is_valid:
            form.save()
            messages.success(request, "Profil Güncellendi")
            redirect("profil-duzenleme")
    else:
        form = profilDuzenlemeForm(instance = request.user)

    return render(request, "pages/profil-duzenleme.html", context={
        "form" : form
    })