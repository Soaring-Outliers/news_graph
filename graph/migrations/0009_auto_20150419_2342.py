# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0008_concept'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleConcept',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('relevance', models.FloatField()),
                ('article', models.ForeignKey(to='graph.Article')),
            ],
        ),
        migrations.RemoveField(
            model_name='concept',
            name='article',
        ),
        migrations.RemoveField(
            model_name='concept',
            name='relevance',
        ),
        migrations.AddField(
            model_name='articleconcept',
            name='concept',
            field=models.ForeignKey(to='graph.Concept'),
        ),
        migrations.AddField(
            model_name='article',
            name='concepts',
            field=models.ManyToManyField(to='graph.Concept', through='graph.ArticleConcept'),
        ),
        migrations.AddField(
            model_name='concept',
            name='articles',
            field=models.ManyToManyField(to='graph.Article', through='graph.ArticleConcept'),
        ),
    ]
