from django import forms
from .models import BirthdayModel


class BirthdayForm(forms.ModelForm):
    class Meta:
        model = BirthdayModel
        fields = [
            "name",
            "date",
            "gift_idea"
        ]
