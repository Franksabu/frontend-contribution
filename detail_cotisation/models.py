from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User
from membre.models import Membre
from cotisation.models import Cotisation


class Detail_cotisation(models.Model):
    montant_paye = models.IntegerField()
    cotisation_id = models.ForeignKey(
        Cotisation,
        on_delete=models.CASCADE,
        related_name="cotisation_detail_cotisation",
    )

    membre_id = models.ForeignKey(
        Membre,
        on_delete=models.CASCADE,
        related_name="membre_detail_cotisation"
    )

    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    date_validate = models.DateTimeField(null=True, blank=True)
    date_delete = models.DateTimeField(null=True)
    user_create = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="detail_created"
    )
    user_delete = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="detail_deleted"
    )
    user_valide = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="detail_validated"
    )

    class Meta:
        ordering = ("-id",)
        db_table = "detail_cotisation_detail"

    def __str__(self):
        return f" {self.membre_id}  {self.cotisation_id} {self.montant_paye}"
