# Generated by Django 4.2 on 2023-04-26 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('e_panchayath_app', '0012_alter_application_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='e_panchayath_app.citizen'),
        ),
    ]
