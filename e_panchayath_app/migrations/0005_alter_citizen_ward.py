# Generated by Django 4.2 on 2023-04-14 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_panchayath_app', '0004_citizen_panchayat_citizen_ward_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citizen',
            name='ward',
            field=models.IntegerField(null=True),
        ),
    ]
