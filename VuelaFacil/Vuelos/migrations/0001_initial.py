# Generated by Django 3.2.7 on 2021-10-05 04:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aeropuerto',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=200)),
                ('Ciudad', models.CharField(max_length=200)),
                ('Disponibilidad', models.BooleanField(verbose_name=True)),
            ],
        ),
        migrations.CreateModel(
            name='Avion',
            fields=[
                ('Id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Disponibilidad', models.BooleanField(verbose_name=True)),
                ('NumSillasEco', models.IntegerField(default=0)),
                ('NumSillasEje', models.IntegerField(default=0)),
                ('PesoBodega', models.FloatField(default=0)),
                ('norte', models.FloatField(default=0)),
                ('este', models.FloatField(default=0)),
                ('UbicacionInicial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vuelos.aeropuerto')),
            ],
        ),
        migrations.CreateModel(
            name='TipoVuelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tipo', models.CharField(max_length=200)),
                ('NumSillasEcoVendidas', models.IntegerField(default=0)),
                ('NumSillasEjeVendidas', models.IntegerField(default=0)),
                ('Peso', models.FloatField(default=0)),
                ('Fecha', models.DateTimeField()),
                ('NumeroSillasVendidas', models.IntegerField()),
                ('AeroLlegada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='Vuelos.aeropuerto')),
                ('AeroSalida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='Vuelos.aeropuerto')),
                ('id_Avion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vuelos.avion')),
            ],
        ),
    ]
