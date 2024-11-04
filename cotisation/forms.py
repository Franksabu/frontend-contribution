from django import forms
from .models import Contribution, Cotisation
from parametrage.nemero import random_reference


class CotisationForm(forms.ModelForm):
    class Meta:
        model = Cotisation
        fields = [
            "reference",
            "montant_min",
            "date_debut",
            "date_fin",
            "periode",
            "type_cotisation",
        ]
        exclude = (
            "date_create",
            "date_validate",
            "date_update",
            "date_delete",
            "user_create",
            "user_validate",
            "user_delete",
        )
        widgets = {
            "reference": forms.TextInput(
                attrs={"placeholder": "référence...", "readonly": "readonly"}
            ),
            "type_cotisation": forms.Select(
                attrs={"class": "form-control"}
            ),
            "montant_min": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Montant minimum..."}
            ),
            "date_debut": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "date_fin": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "periode": forms.Select(),
        }
        labels = {
            "reference": "Référence",
            "type_cotisation": "Type de cotisation",
            "montant_min": "Montant Minimum",
            "date_debut": "Date de Début",
            "date_fin": "Date de Fin",
            "periode": "Periode",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["reference"].initial = random_reference.new_numero("COTI")


# --------------------ContributionForm --------------------------------------#

class ContributionForm(forms.ModelForm):
    class Meta:
        model = Contribution
        fields = [
            "reference",
            "montant",
            "date_contrib",
            "membre",
            "cotisation"
        ]
        exclude = (
            "date_create",
            "date_validate",
            "date_update",
            "date_delete",
            "user_create",
            "user_validate",
            "user_delete",
        )
        widgets = {
            "reference": forms.TextInput(
                attrs={"placeholder": "référence...", "readonly": "readonly"}
            ),
            "montant": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Montant minimum..."}
            ),
            "date_contrib": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "membre": forms.Select(
                attrs={"class": "form-control"}
            ),
            "cotisation": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            )
        }
        labels = {
            "reference": "Référence",
            "membre": "Membre",
            "cotisation": "Cotisation",
            "date_contrib": "Date de contribution",
            "montant": "Montant de contribution"
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["reference"].initial = random_reference.new_numero("CONTRI")
