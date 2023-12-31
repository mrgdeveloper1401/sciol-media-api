# Generated by Django 4.2.5 on 2023-09-21 08:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='create_at')),
                ('body', models.TextField(max_length=500)),
                ('slug', models.SlugField()),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
                'db_table': 'post-model',
                'ordering': ('-create_at', 'body'),
            },
        ),
        migrations.CreateModel(
            name='TagPostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'tag post',
                'verbose_name_plural': 'tag posts',
                'db_table': 'tag-post-model',
            },
        ),
        migrations.CreateModel(
            name='PostOptionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='post/image')),
                ('video', models.FileField(blank=True, null=True, upload_to='post/video')),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='post.postmodel')),
            ],
            options={
                'verbose_name': 'PostOptionModel',
                'verbose_name_plural': 'PostOptionModels',
                'db_table': 'post-option-models',
            },
        ),
        migrations.AddField(
            model_name='postmodel',
            name='post_tag',
            field=models.ManyToManyField(blank=True, related_name='Ptag', to='post.tagpostmodel'),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='RecyclePost',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('post.postmodel',),
        ),
    ]
