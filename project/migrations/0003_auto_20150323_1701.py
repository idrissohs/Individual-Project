# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0002_auto_20150311_2104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('about', models.TextField()),
                ('domain', models.CharField(max_length=20, choices=[(b'T', b'Tourism'), (b'E', b'Education'), (b'A', b'Agriculture'), (b'C', b'Technology'), (b'S', b'Service')])),
                ('tags', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('dislikes', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='match',
            name='funder',
        ),
        migrations.RemoveField(
            model_name='match',
            name='project',
        ),
        migrations.DeleteModel(
            name='Match',
        ),
        migrations.RemoveField(
            model_name='project',
            name='author',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
