# Generated by Django 5.1.1 on 2024-10-15 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Metro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mantenedor_metro',
            name='linea_metro',
            field=models.CharField(max_length=50),
        ),
    ]
