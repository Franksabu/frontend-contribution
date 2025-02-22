# Generated by Django 5.1.1 on 2024-11-04 13:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('membre', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeCotisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('montant_max_retrait', models.DecimalField(decimal_places=2, default='0.00', max_digits=10)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Cotisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=50, unique=True)),
                ('montant_min', models.FloatField()),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField(blank=True, null=True)),
                ('periode', models.IntegerField(choices=[(0, 'Aucun periode'), (1, 'Mensuel'), (2, 'Trimestriel'), (3, 'Semestreil'), (4, 'Annuel')], default=0)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_validate', models.DateTimeField(blank=True, null=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('date_delete', models.DateTimeField(blank=True, null=True)),
                ('user_create', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cotisations_created', to=settings.AUTH_USER_MODEL)),
                ('user_delete', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cotisations_deleted', to=settings.AUTH_USER_MODEL)),
                ('user_validate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cotisations_validated', to=settings.AUTH_USER_MODEL)),
                ('type_cotisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cotisation.typecotisation')),
            ],
            options={
                'db_table': 'cotisation_cotisation',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Contribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=50, unique=True)),
                ('date_contrib', models.DateField()),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_validate', models.DateTimeField(blank=True, null=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('date_delete', models.DateTimeField(blank=True, null=True)),
                ('membre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='membre.membre')),
                ('user_create', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contribution_created', to=settings.AUTH_USER_MODEL)),
                ('user_delete', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contribution_deleted', to=settings.AUTH_USER_MODEL)),
                ('user_validate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contribution_validated', to=settings.AUTH_USER_MODEL)),
                ('cotisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cotisation.cotisation')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='DetailCotisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant_paye', models.DecimalField(decimal_places=2, default='0.00', max_digits=10)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('cotisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cotisation.cotisation')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]
