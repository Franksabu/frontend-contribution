from django.db import models
from django.contrib.auth.models import User

# from enums import choix_sex, FEMME,choix_identite,CARTE_NATIONALE
from parametrage.enums import choix_sex, FEMME, choix_identite, CARTE_NATIONALE


class Membre(models.Model):
    reference = models.CharField(max_length=50, unique=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    sex = models.IntegerField(choices=choix_sex, default=FEMME)
    type_id = models.IntegerField(choices=choix_identite, default=CARTE_NATIONALE)
    numero_id = models.CharField(max_length=100)
    description = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    date_validate = models.DateTimeField(null=True, blank=True)
    date_delete = models.DateTimeField(null=True)
    user_create = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="membre_create", null=True
    )
    user_valide = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="membre_valide", null=True
    )

    class Meta:
        ordering = ("-id",)
        db_table = "membre_membre"

    def __str__(self):
        return f"{self.nom} {self.prenom}"
