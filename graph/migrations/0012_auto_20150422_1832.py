# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0011_auto_20150421_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='url',
            field=models.URLField(max_length=255, blank=True),
        ),
    ]
