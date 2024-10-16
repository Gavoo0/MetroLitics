# Generated by Django 5.1.1 on 2024-10-16 22:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mantenedor_metro',
            fields=[
                ('id_metro', models.AutoField(primary_key=True, serialize=False)),
                ('linea_metro', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
                ('aglomeracion', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id_reporte', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('f_id_metro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Metro.mantenedor_metro')),
            ],
        ),
    ]
