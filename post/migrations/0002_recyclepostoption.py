# Generated by Django 4.2.5 on 2023-09-22 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecyclePostOption',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('post.postoptionmodel',),
        ),
    ]
