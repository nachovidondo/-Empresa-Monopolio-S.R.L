# Generated by Django 3.1.7 on 2021-03-24 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Renta', '0007_auto_20210324_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oficina',
            name='baño_privado',
            field=models.CharField(choices=[('Si', 'Si'), ('No', 'No')], default='Si', max_length=200),
        ),
        migrations.AlterField(
            model_name='oficina',
            name='telefono',
            field=models.CharField(choices=[('Si', 'Si'), ('No', 'No')], default='Si', max_length=200),
        ),
        migrations.AlterField(
            model_name='oficina',
            name='wifi',
            field=models.CharField(choices=[('Si', 'Si'), ('No', 'No')], default='Si', max_length=200),
        ),
    ]