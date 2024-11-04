from django import forms
from .models import Membre
from parametrage.enums import choix_sex, choix_identite
from parametrage.nemero import *


class MembreForm(forms.ModelForm):

    class Meta:
        model = Membre
        fields = [
            "reference",
            "nom",
            "prenom",
            "adresse",
            "telephone",
            "email",
            "sex",
            "type_id",
            "numero_id",
            "description",
        ]
        exclude = (
            "user_create",
            "user_valide",
            "user_delete",
            "date_create",
            "date_validate",
            "date_update",
            "date_delete",
        )
        widgets = {
            "reference": forms.TextInput(
                attrs={"placeholder": "référence...", "readonly": "readonly"}
            ),
            "nom": forms.TextInput(attrs={"class": "form-control"}),
            "prenom": forms.TextInput(attrs={"class": "form-control"}),
            "adresse": forms.TextInput(attrs={"class": "form-control"}),
            "telephone": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "numero_id": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(
                attrs={
                    "rows": 10,
                    "cols": 30,
                    "class": "form-control",
                    "placeholder": "Veuillez entrer votre description ici...",
                }
            ),
        }

        labels = {
            "reference": "Référence :",
            "nom": "Nom",
            "prenom": "Prénom :",
            "adresse": "Adresse :",
            "telephone": "Téléphone :",
            "email": "Email :",
            "sex": "Sexe :",
            "type_id": "Type d'identité :",
            "numero_id": "Numéro d'identité :",
            "description": "Description :",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["reference"].initial = random_reference.new_numero("MEMB")
