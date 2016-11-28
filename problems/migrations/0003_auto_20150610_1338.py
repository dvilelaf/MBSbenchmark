# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0002_auto_20150610_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='authors',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='solution',
            name='authors',
            field=models.CharField(max_length=256),
        ),
    ]
