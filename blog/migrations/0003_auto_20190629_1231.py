# Generated by Django 2.2.2 on 2019-06-29 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190629_1227'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='skug',
            new_name='slug',
        ),
    ]
