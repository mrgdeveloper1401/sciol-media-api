# Generated by Django 4.2.5 on 2023-09-21 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('channals', '0004_postchannal_content_alter_channalmodel_image_channal'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postchannal',
            options={'verbose_name': 'channal option', 'verbose_name_plural': 'channal options'},
        ),
        migrations.AlterModelTable(
            name='postchannal',
            table='channal-option-model',
        ),
    ]
