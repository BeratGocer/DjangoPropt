from django.shortcuts import render
from blog.models import yaziModel
from django.core.paginator import Paginator

def anasayfa(request):

    yazilar = yaziModel.objects.order_by("-id")
    sayfa = request.GET.get("sayfa")
    paginator = Paginator(yazilar, 4)
    
    return render(request, "pages/anasayfa.html", context={
        "yazilar": paginator.get_page(sayfa)
    })
