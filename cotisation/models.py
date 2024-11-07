# models.py
from django.db import models
from django.contrib.auth.models import User
from membre.models import Membre
from parametrage.enums import choix_periode, AUCUN


class TypeCotisation(models.Model):
    nom = models.CharField(max_length=20)
    montant_max_retrait = models.DecimalField(
        max_digits=10, decimal_places=2, default="0.00"
    )

    class Meta:
        ordering = ("-id",)

    def __str__(self):
        return f"{self.nom}"


class Cotisation(models.Model):
    reference = models.CharField(max_length=50, unique=True)
    montant_min = models.FloatField()
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)
    periode = models.IntegerField(choices=choix_periode, default=AUCUN)
    date_create = models.DateTimeField(auto_now_add=True)
    date_validate = models.DateTimeField(null=True, blank=True)
    date_update = models.DateTimeField(auto_now=True)
    date_delete = models.DateTimeField(null=True, blank=True)
    type_cotisation = models.ForeignKey(
        TypeCotisation,
        on_delete=models.CASCADE,
    )
    user_create = models.ForeignKey(
        User, related_name="cotisations_created", on_delete=models.CASCADE
    )
    user_validate = models.ForeignKey(
        User,
        related_name="cotisations_validated",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    user_delete = models.ForeignKey(
        User,
        related_name="cotisations_deleted",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ("-id",)
        db_table = "cotisation_cotisation"

    def __str__(self):
        return f"{self.montant_min} "


class Contribution(models.Model):
    reference = models.CharField(max_length=50, unique=True)
    montant = models.FloatField()
    date_contrib = models.DateField()
    membre = models.ForeignKey(Membre, on_delete=models.CASCADE)
    cotisation = models.ForeignKey(Cotisation, on_delete=models.CASCADE)
    date_create = models.DateTimeField(auto_now_add=True)
    date_validate = models.DateTimeField(null=True, blank=True)
    date_update = models.DateTimeField(auto_now=True)
    date_delete = models.DateTimeField(null=True, blank=True)
    user_create = models.ForeignKey(
        User, related_name="contribution_created", on_delete=models.CASCADE
    )
    user_validate = models.ForeignKey(
        User,
        related_name="contribution_validated",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    user_delete = models.ForeignKey(
        User,
        related_name="contribution_deleted",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ("-id",)

    def __str__(self):
        return f"{self.reference}"


class Detail_contribution(models.Model):
    montant_paye = models.DecimalField(max_digits=10, decimal_places=2, default="0.00")
    cotisation = models.ForeignKey(Cotisation, on_delete=models.CASCADE)
    membre = models.ForeignKey(Membre, on_delete=models.CASCADE)
    date_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-id",)
