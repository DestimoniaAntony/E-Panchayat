# Generated by Django 4.2 on 2023-04-14 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_panchayath_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='citizen',
            name='surname',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
