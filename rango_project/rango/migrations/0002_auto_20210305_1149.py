# Generated by Django 3.0.12 on 2021-03-05 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='page',
            options={'verbose_name_plural': 'Pages'},
        ),
    ]
