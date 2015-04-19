# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(default='No content'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 19, 17, 32, 13, 530394, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
