# Generated by Django 3.2.4 on 2021-06-18 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100, unique=True)),
                ('phone_number', models.CharField(max_length=20, null=True)),
                ('nickname', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
