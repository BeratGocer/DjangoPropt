from django.contrib.auth.forms import UserChangeForm
from account.models import customUserModel


class profilDuzenlemeForm(UserChangeForm):
    password = None
    class Meta:
        model = customUserModel
        fields = (
            "email", "first_name", "last_name", "avatar"
        )