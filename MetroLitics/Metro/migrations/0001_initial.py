from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Metro',
            fields=[
                ('id_metro', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_metro', models.CharField(max_length=50)),
                ('linea_metro', models.IntegerField()),
                ('cantidad_aglomeracion', models.IntegerField(default=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
    ]
