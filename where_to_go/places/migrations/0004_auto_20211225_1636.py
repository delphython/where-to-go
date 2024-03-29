# Generated by Django 3.2.10 on 2021-12-25 13:36

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_alter_place_description_short'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['image_order']},
        ),
        migrations.AlterField(
            model_name='image',
            name='image_order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_Long',
            field=tinymce.models.HTMLField(verbose_name='Полное описание'),
        ),
    ]
