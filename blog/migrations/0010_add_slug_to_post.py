# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-11 08:51
from __future__ import unicode_literals

from django.db import migrations, models


def update_slug(apps, schema_editor):
    Post = apps.get_model('blog', 'Post')
    for post in Post.objects.all():
        post.slug = str(post.id)
        post.save()


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20160711_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(unique=False, default='')
        ),
        migrations.RunPython(update_slug, ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(unique=True)
        ),
    ]