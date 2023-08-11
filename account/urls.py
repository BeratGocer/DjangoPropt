from django.urls import path
from account.views import cikis, sifreDegistirme, profilDuzenleme, kayit
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("giris", auth_views.LoginView.as_view(
        template_name = "pages/giris.html"
    ), name="giris"),

    path("cikis", cikis, name="cikis"),
    path("sifre-degistirme", sifreDegistirme, name="sifre-degistirme"),
    path("profil-duzenleme", profilDuzenleme, name="profil-duzenleme"),
    path("kayit", kayit, name="kayit")
]