# Generated by Django 4.2.5 on 2023-09-22 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groupss', '0006_alter_groupmodel_image_alter_groupoptionmodel_body_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecycleGroup',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('groupss.groupmodel',),
        ),
        migrations.CreateModel(
            name='RecycleGroupOption',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('groupss.groupoptionmodel',),
        ),
    ]