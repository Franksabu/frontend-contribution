# Generated by Django 5.1.1 on 2024-10-23 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assistance', '0002_alter_assistance_date_assistance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assistance',
            name='reference',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
