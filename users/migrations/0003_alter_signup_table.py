# Generated by Django 3.2.4 on 2021-06-18 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210618_1619'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='signup',
            table='signups',
        ),
    ]