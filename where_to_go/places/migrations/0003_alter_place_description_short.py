# Generated by Django 3.2.10 on 2021-12-23 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_auto_20211213_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.CharField(max_length=255, verbose_name='Краткое описание'),
        ),
    ]