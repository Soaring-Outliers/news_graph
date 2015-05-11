# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0012_auto_20150422_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='concept',
            name='articles_count',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
