# Generated by Django 3.2.16 on 2024-08-19 13:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Membre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=50, unique=True)),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('adresse', models.CharField(max_length=100)),
                ('telephone', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('sex', models.IntegerField(choices=[(0, 'Femme'), (1, 'Homme')], default=0)),
                ('type_id', models.IntegerField(choices=[(0, 'carte national'), (1, 'passport'), (2, 'laisser passe')], default=0)),
                ('numero_id', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('date_validate', models.DateTimeField(null=True)),
                ('date_delete', models.DateTimeField(null=True)),
                ('user_create', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='membre_create', to=settings.AUTH_USER_MODEL)),
                ('user_delete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='membre_delete', to=settings.AUTH_USER_MODEL)),
                ('user_valide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='membre_valide', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]
