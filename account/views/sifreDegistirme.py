from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

@login_required(login_url="/")
def sifreDegistirme(request):

    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            kullanici = form.save()
            update_session_auth_hash(request, kullanici)
            messages.success(request, "Şifre Değiştirildi")
            return redirect("sifre-degistirme")

    else:
        form = PasswordChangeForm(request.user)

    return render(request, "pages/sifre-degistirme.html", context={
        "form": form
    })