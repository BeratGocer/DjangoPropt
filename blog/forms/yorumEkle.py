from django import forms
from blog.models import yorumModel


class yoruEkleForm(forms.ModelForm):
    class Meta:
        model = yorumModel
        fields = ("yorum", )
