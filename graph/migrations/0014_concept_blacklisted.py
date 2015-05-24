# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0013_concept_articles_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='concept',
            name='blacklisted',
            field=models.BooleanField(default=False),
        ),
    ]
