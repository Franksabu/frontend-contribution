# Generated by Django 5.1.1 on 2024-10-04 14:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cotisation', '0002_alter_cotisation_periode'),
        ('membre', '0003_alter_membre_table'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assistance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=10, unique=True)),
                ('date_assistance', models.DateTimeField(auto_now_add=True)),
                ('montant_assistance', models.IntegerField()),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('date_validate', models.DateTimeField(blank=True, null=True)),
                ('date_delete', models.DateTimeField(null=True)),
                ('cotisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assistance_cotisation', to='cotisation.cotisation')),
                ('membre_assistant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assistance_membre', to='membre.membre')),
                ('user_create', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assistance_created', to=settings.AUTH_USER_MODEL)),
                ('user_delete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assistance_deleted', to=settings.AUTH_USER_MODEL)),
                ('user_valide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assistance_validated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'assistance_assistance',
                'ordering': ('-id',),
            },
        ),
    ]
