# Generated by Django 3.1.7 on 2021-03-24 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Renta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oficina',
            name='baño_privado',
            field=models.BooleanField(choices=[('Con baño privado', 'Sin baño privado'), ('', '')], default=True),
        ),
        migrations.AlterField(
            model_name='oficina',
            name='telefono',
            field=models.BooleanField(choices=[('Con Telefono', 'Sin Telefono'), ('', '')], default=True),
        ),
        migrations.AlterField(
            model_name='oficina',
            name='wifi',
            field=models.BooleanField(choices=[('Con wifi', 'Sin wifi'), ('', '')], default=True),
        ),
    ]