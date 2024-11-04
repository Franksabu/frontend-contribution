from django import forms
from .models import Detail_cotisation
from parametrage.nemero import random_reference


class Detail_cotisationForm(forms.ModelForm):
    class Meta:
        model = Detail_cotisation
        fields = [
            "membre_id",
            "cotisation_id",
            "montant_paye",
        ]
        exclude = (
            "date_create",
            "date_update",
            "date_validate",
            "date_delete",
            "user_create",
            "user_validate",
            "user_delete",
        )
        widgets = {
            "membre_id": forms.Select(attrs={"class": "form-control"}),
            "cotisation": forms.Select(attrs={"class": "form-control"}),
            "montant_paye": forms.NumberInput(attrs={"class": "form-control"}),
        }
        labels = {
            "membre_id": "Membre:",
            "cotisation": "Cotisation",
            "montant_paye": "Montant total paye:",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
