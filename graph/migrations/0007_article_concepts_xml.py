# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0006_auto_20150419_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='concepts_xml',
            field=models.TextField(null=True, blank=True),
        ),
    ]
