# Generated by Django 5.1.1 on 2024-10-08 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assistance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assistance',
            name='date_assistance',
            field=models.DateTimeField(),
        ),
    ]
