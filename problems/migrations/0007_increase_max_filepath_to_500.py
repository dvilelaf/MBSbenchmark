# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import problems.models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0006_Add_linearization_analysis_cathegory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='description',
            field=models.FileField(max_length=500, upload_to=problems.models.get_problem_path),
        ),
        migrations.AlterField(
            model_name='solution',
            name='miscellaneous',
            field=models.FileField(upload_to=problems.models.get_solution_misc_path, max_length=500, blank=True),
        ),
        migrations.AlterField(
            model_name='solution',
            name='results',
            field=models.FileField(max_length=500, upload_to=problems.models.get_solution_results_path),
        ),
    ]
