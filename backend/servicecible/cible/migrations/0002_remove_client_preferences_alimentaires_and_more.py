# Generated by Django 4.2.17 on 2024-12-20 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cible', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='preferences_alimentaires',
        ),
        migrations.RemoveField(
            model_name='client',
            name='preferences_sonore',
        ),
        migrations.AddField(
            model_name='client',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='client',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='client',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
