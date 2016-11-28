# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0003_auto_20150610_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='comments',
            field=models.TextField(max_length=1024, blank=True),
        ),
        migrations.AlterField(
            model_name='solution',
            name='method',
            field=models.TextField(max_length=1024),
        ),
    ]
