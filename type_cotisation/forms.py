from .models import Type_cotisation
from django import forms
from parametrage.nemero import random_reference


class Type_cotisationForm(forms.ModelForm):

    class Meta:
        model = Type_cotisation
        fields = ["nom", "montant_max_retrait", "description"]
        exclude = (
            "user_create",
            "user_valide",
            "user_delete",
            "date_create",
            "date_validate",
            "date_update",
            "date_delete"
        )
        widgets = {
            "nom": forms.TextInput(
                attrs={"placeholder": "nom...", "class": "form-control"}
            ),
            "montant_max_retrait": forms.TextInput(
                attrs={"placeholder": "montant_max_retrait...", "class": "form-control"}
            ),
            "description": forms.Textarea(
                attrs={
                    "rows": 5,
                    "cols": 30,
                    "placeholder": "description...",
                    "class": "form-control",
                }
            ),
        }

        labels = {
            "nom": "Nom",
            "montant_max_retrait": "Montant max retrait",
            "description": "Description",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['reference'].initial = random_reference.new_numero("TYCO")
