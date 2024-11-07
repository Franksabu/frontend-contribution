from django.db import models
from django.contrib.auth.models import User
from membre.models import Membre
from cotisation.models import Cotisation


class Assistance(models.Model):
    reference = models.CharField(max_length=30, unique=True)
    date_assistance = models.DateTimeField()
    montant_assistance = models.IntegerField()
    cotisation = models.ForeignKey(
        Cotisation, on_delete=models.CASCADE, related_name="assistance_cotisation"
    )

    membre_assistant = models.ForeignKey(
        Membre, on_delete=models.CASCADE, related_name="assistance_membre"
    )

    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    date_validate = models.DateTimeField(null=True, blank=True)
    date_delete = models.DateTimeField(null=True)
    user_create = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="assistance_created"
    )
    user_delete = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="assistance_deleted"
    )
    user_valide = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="assistance_validated"
    )

    class Meta:
        ordering = ("-id",)
        db_table = "assistance_assistance"

    def __str__(self):
        return f"{self.montant_assistance} {self.date_assistance} "
