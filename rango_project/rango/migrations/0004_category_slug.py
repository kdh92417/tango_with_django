# Generated by Django 3.0.12 on 2021-03-09 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_auto_20210308_0317'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
