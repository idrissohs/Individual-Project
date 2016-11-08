# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20150323_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='tags',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
    ]
