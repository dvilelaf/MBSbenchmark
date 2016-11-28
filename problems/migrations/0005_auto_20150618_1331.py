# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0004_auto_20150610_1713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='solutions',
        ),
        migrations.RemoveField(
            model_name='solution',
            name='number',
        ),
        migrations.RemoveField(
            model_name='user',
            name='problems',
        ),
        migrations.RemoveField(
            model_name='user',
            name='solutions',
        ),
    ]
