# Generated by Django 5.0.6 on 2024-07-12 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='description',
        ),
    ]
