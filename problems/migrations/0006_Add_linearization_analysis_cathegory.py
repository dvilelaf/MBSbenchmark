# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0005_auto_20150618_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='analysis',
            field=models.CharField(max_length=2, choices=[('FD', 'Forward Dynamic'), ('ID', 'Inverse Dynamic'), ('KI', 'Kinematic'), ('ST', 'Static'), ('LI', 'Linearization')]),
        ),
    ]
