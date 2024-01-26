from django import forms
from .models import UserProfile


class UserProfileFormUpdate(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            "cpf",
            "birth_date",
            "discord_nickname",
        ]


class UserProfileFormInput(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            "user",
            "cpf",
            "birth_date",
            "discord_nickname",
        ]
