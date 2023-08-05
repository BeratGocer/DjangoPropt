from django.shortcuts import render, redirect
from blog.forms import iletisimForm
from blog.models import IletisimModel

def contact(request):
    form = iletisimForm()

    if request.method == "POST":
        form = iletisimForm(request.POST)

        if form.is_valid():
            
            form.save()

            return redirect("Anasayfa")
        else:
            pass
            

    context = {
        'form': form
    }

    return render(request, "pages/iletisim.html", context=context)
