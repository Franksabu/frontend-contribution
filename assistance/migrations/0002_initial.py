# Generated by Django 5.1.1 on 2024-11-04 13:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("assistance", "0001_initial"),
        ("cotisation", "0001_initial"),
        ("membre", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="assistance",
            name="cotisation",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="assistance_cotisation",
                to="cotisation.cotisation",
            ),
        ),
        migrations.AddField(
            model_name="assistance",
            name="membre_assistant",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="assistance_membre",
                to="membre.membre",
            ),
        ),
        migrations.AddField(
            model_name="assistance",
            name="user_create",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="assistance_created",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="assistance",
            name="user_delete",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="assistance_deleted",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="assistance",
            name="user_valide",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="assistance_validated",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
