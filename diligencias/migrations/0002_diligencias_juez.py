# Generated by Django 3.2.8 on 2021-10-08 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diligencias', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='diligencias',
            name='juez',
            field=models.CharField(default=2, max_length=80),
            preserve_default=False,
        ),
    ]
