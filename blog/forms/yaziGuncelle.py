from django import forms
from blog.models import yaziModel


class yaziGuncelleForm(forms.ModelForm):
    class Meta:
        model = yaziModel
        exclude = ("yazar", "slug")