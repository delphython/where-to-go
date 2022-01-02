# Generated by Django 3.2.10 on 2022-01-02 11:56

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0011_alter_image_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(blank=True, default='', verbose_name='Полное описание'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.TextField(blank=True, default='', verbose_name='Краткое описание'),
            preserve_default=False,
        ),
    ]
