# Generated by Django 4.2.5 on 2023-10-02 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channals', '0007_recyclechannal_recyclechannaloption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channalmodel',
            name='id_channal',
            field=models.SlugField(help_text='write id channal with start @any thing', null=True, verbose_name='id'),
        ),
    ]
