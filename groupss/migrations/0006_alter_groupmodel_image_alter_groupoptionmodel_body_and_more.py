# Generated by Django 4.2.5 on 2023-09-21 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groupss', '0005_remove_groupmodel_body_groupoptionmodel_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='group/image_group', verbose_name='image group'),
        ),
        migrations.AlterField(
            model_name='groupoptionmodel',
            name='body',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='groupoptionmodel',
            name='file',
            field=models.FileField(blank=True, upload_to='group/group_file'),
        ),
        migrations.AlterField(
            model_name='groupoptionmodel',
            name='image',
            field=models.ImageField(blank=True, upload_to='gruop/image_group'),
        ),
        migrations.AlterField(
            model_name='groupoptionmodel',
            name='video',
            field=models.FileField(blank=True, upload_to='group/group_video'),
        ),
    ]
