# Generated by Django 4.2 on 2023-04-17 10:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('e_panchayath_app', '0008_request'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='media/')),
                ('mobile', models.CharField(max_length=10, null=True)),
                ('qualification', models.CharField(max_length=20, null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('marital_status', models.CharField(max_length=10, null=True)),
                ('birth_date', models.DateField(null=True)),
                ('address_line1', models.CharField(max_length=20, null=True)),
                ('address_line2', models.CharField(max_length=20, null=True)),
                ('country', models.CharField(max_length=25, null=True)),
                ('state', models.CharField(max_length=25, null=True)),
                ('district', models.CharField(max_length=25, null=True)),
                ('pincode', models.CharField(max_length=6, null=True)),
                ('ward', models.IntegerField(null=True)),
                ('panchayat', models.CharField(max_length=25, null=True)),
                ('password', models.CharField(max_length=10, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]