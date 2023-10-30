# Generated by Django 4.2 on 2023-04-17 04:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('e_panchayath_app', '0006_rename_address_line1_staff_service_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='staff',
            old_name='service',
            new_name='address_line1',
        ),
        migrations.AddField(
            model_name='staff',
            name='address_line2',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='birth_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='gender',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='marital_status',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='mobile',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='password',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='pincode',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='qualification',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]