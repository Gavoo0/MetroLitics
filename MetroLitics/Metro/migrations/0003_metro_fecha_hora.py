# Generated by Django 5.1.1 on 2024-10-12 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Metro', '0002_rename_nombre_metro_metro_estacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='metro',
            name='fecha_hora',
            field=models.DateTimeField(auto_now=True),
        ),
    ]