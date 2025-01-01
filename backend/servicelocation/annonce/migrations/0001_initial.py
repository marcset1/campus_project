# Generated by Django 4.2.17 on 2024-12-30 04:25

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bailleur_id', models.IntegerField(null=True)),
                ('typeLocation', models.CharField(max_length=50, null=True)),
                ('address', models.CharField(max_length=255, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(null=True, srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Characteristic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('count', models.IntegerField(null=True)),
                ('image', models.ImageField(upload_to='characteristics/')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='characteristics', to='annonce.location')),
            ],
        ),
    ]