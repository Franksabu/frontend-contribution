from django import forms
from .models import Assistance
from parametrage.nemero import random_reference


class AssistanceForm(forms.ModelForm):
    class Meta:
        model = Assistance
        fields = [
            "reference",
            "montant_assistance",
            "cotisation",
            "date_assistance",
            "membre_assistant",
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
            "reference": forms.TextInput(attrs={"placeholder": "référence...", "readonly": "readonly"}),
            "montant_assistance": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Montant de l'assistance..."}),
            "cotisation": forms.Select(attrs={"class": "form-control"}),
            "membre_assistant": forms.Select(attrs={"class": "form-control"}),
            "date_assistance": forms.DateTimeInput(attrs={"class": "form-control", "type": "date"}),
        }
        labels = {
            "reference": "Référence:",
            "montant_assistance": "Montant de l'Assistance:",
            "cotisation": "Cotisation:",
            "date_assistance": "Date de l'Assistance:",
            "membre_assistant": "Membre assistant:",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['reference'].initial = random_reference.new_numero("ASSI")
