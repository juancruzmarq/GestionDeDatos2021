# Generated by Django 3.2.4 on 2021-06-13 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museo', '0004_auto_20210613_2202'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empleado',
            options={'ordering': ['nombre'], 'verbose_name': 'empleado', 'verbose_name_plural': 'empleados'},
        ),
        migrations.AlterModelOptions(
            name='pared',
            options={'ordering': ['nombre'], 'verbose_name': 'Pared', 'verbose_name_plural': 'Paredes'},
        ),
    ]