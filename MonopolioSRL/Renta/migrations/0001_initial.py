# Generated by Django 3.1.3 on 2021-03-24 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Oficina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('codigo_interno', models.CharField(max_length=100)),
                ('persona_encargada', models.CharField(max_length=200)),
                ('cantidad_personas', models.IntegerField()),
                ('telefono', models.BooleanField(default=True)),
                ('baño_privado', models.BooleanField(default=True)),
                ('wifi', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Oficina',
            },
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cliente', models.CharField(max_length=200)),
                ('nombre_reserva', models.CharField(max_length=200)),
                ('fecha_reserva', models.DateTimeField(auto_now=True)),
                ('fecha_comienzo', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('oficina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Renta.oficina')),
            ],
            options={
                'verbose_name': 'Reserva',
            },
        ),
    ]
