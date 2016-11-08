# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20150323_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='tags',
            field=models.CharField(default=datetime.datetime(2015, 3, 23, 17, 3, 36, 660922, tzinfo=utc), max_length=100, blank=True),
            preserve_default=False,
        ),
    ]
