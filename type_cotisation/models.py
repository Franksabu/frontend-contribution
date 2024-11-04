from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Type_cotisation(models.Model):
    nom = models.CharField(max_length=20)
    montant_max_retrait = models.FloatField()
    description = models.TextField()
    date_create = models.DateTimeField(default=timezone.now)
    date_update = models.DateTimeField(auto_now=True)
    date_validate = models.DateTimeField(null=True, blank=True)
    date_delete = models.DateTimeField(null=True)
    user_create = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="type_cotisation_created", default=1
    )
    user_delete = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="type_cotisation_deleted", default=1
    )
    user_valide = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="type_cotisation_validated", default=1
    )

    class Meta:
        ordering = ("-id",)
        db_table = "type_cotisation_type"

    def __str__(self):
        return f"{self.nom}"
