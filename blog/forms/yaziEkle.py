from django import forms
from blog.models import yaziModel


class yaziEkleForm(forms.ModelForm):
    class Meta:
        model = yaziModel
        exclude = ("yazar", "slug")
