# Generated by Django 5.1.1 on 2024-10-12 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Metro', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='metro',
            old_name='nombre_metro',
            new_name='estacion',
        ),
    ]