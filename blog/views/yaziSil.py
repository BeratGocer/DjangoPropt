from django.contrib.auth.decorators import login_required
from blog.models import yaziModel
from django.shortcuts import get_object_or_404, redirect


@login_required(login_url="/")
def yaziSil(request, slug):
    get_object_or_404(yaziModel, slug=slug, yazar=request.user).delete()
    return redirect("yazilarim")