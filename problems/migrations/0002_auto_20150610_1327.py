# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solution',
            old_name='pub_date',
            new_name='sub_date',
        ),
        migrations.RemoveField(
            model_name='problem',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='problem',
            name='authors',
            field=models.CharField(max_length=256, default='user.name'),
        ),
        migrations.AddField(
            model_name='solution',
            name='authors',
            field=models.CharField(max_length=256, default='user.name'),
        ),
    ]
