# Generated by Django 4.2.5 on 2023-09-21 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('channals', '0002_channalmodel_id_channal_channalmodel_image_channal_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='channalmodel',
            name='body',
        ),
    ]
