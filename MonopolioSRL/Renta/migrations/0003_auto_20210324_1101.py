# Generated by Django 3.1.7 on 2021-03-24 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Renta', '0002_auto_20210324_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oficina',
            name='baño_privado',
            field=models.BooleanField(choices=[('Sin baño privado', 'Con baño privado'), ('', '')], default=True),
        ),
        migrations.AlterField(
            model_name='oficina',
            name='telefono',
            field=models.BooleanField(choices=[('Sin Telefono', 'Con Telefono'), ('', '')], default=True),
        ),
        migrations.AlterField(
            model_name='oficina',
            name='wifi',
            field=models.BooleanField(choices=[('Sin wifi', 'Con wifi'), ('', '')], default=True),
        ),
    ]
