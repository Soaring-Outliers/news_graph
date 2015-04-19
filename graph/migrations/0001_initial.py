# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rss_url', models.URLField(max_length=511)),
                ('url', models.URLField(max_length=511)),
                ('title', models.CharField(max_length=511)),
                ('description', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('url', models.URLField(max_length=255)),
                ('rss_url', models.URLField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='website',
            field=models.ForeignKey(to='graph.Website'),
        ),
    ]
