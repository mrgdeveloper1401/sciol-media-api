# Generated by Django 4.2.5 on 2023-09-24 12:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_rename_imageuser_imageusermodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageusermodel',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='image', to=settings.AUTH_USER_MODEL),
        ),
    ]
