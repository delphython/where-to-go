# Generated by Django 3.2.10 on 2021-12-28 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_auto_20211228_0946'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='description_Long',
            new_name='description_long',
        ),
    ]
