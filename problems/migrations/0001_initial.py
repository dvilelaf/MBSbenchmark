# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import problems.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('published', models.BooleanField(default=False)),
                ('sub_date', models.DateTimeField(verbose_name='date submitted')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('solutions', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to=problems.models.get_problem_path)),
                ('description', models.FileField(upload_to=problems.models.get_problem_path)),
                ('comments', models.CharField(max_length=1024, blank=True)),
                ('application', models.CharField(max_length=2, choices=[('Aerospace Engineering', (('LG', 'Aircraft landing gear'), ('HB', 'Helicopter blades'), ('LV', 'Launch vehicle dynamics'), ('SS', 'Satellites and space structures'), ('SR', 'Space robotics'))), ('Automotive Dynamics', (('SS', 'Suspension systems'), ('TC', 'Torque converters'), ('TC', 'Transmission components'), ('VM', 'Vehicle dynamical models'))), ('Biomechanical Models', (('HM', 'Human-machine models'), ('MM', 'Musculoskeletal models'))), ('Didactic Models', (('GY', 'Gyrocompasses'), ('MS', 'Mass-spring systems'), ('PE', 'Pendula'))), ('Marine Systems', (('OM', 'Octopus-like manipulators'), ('RF', 'Robotic fish'), ('UV', 'Underwater vehicles'))), ('Mechanisms and Machinery', (('CD', 'Cable-driven mechanisms'), ('CL', 'Cam-linkage mechanisms'), ('GC', 'Gears, chains, and pulleys'), ('LK', 'Linkages'), ('WT', 'Wind turbines'))), ('Musical Instruments', (('HA', 'Harpsichord action mechanisms'), ('PA', 'Piano action mechanisms'))), ('Particle and Molecular Dynamics', (('FD', 'Fluid-multibody dynamics interaction'), ('GM', 'Granular media modeling'), ('PM', 'Protein models'))), ('Railroad Systems', (('RD', 'Railroad vehicle dynamics'), ('RS', 'Railroad vehicle suspensions'), ('TP', 'Trolley poles'))), ('Robotics', (('PR', 'Parallel robots'), ('SR', 'Serial robots'), ('WR', 'Walking robots'), ('WR', 'Wheeled robots'))), ('Sport Applications', (('AR', 'Archery'), ('BD', 'Bicycle dynamics'), ('CL', 'Climbing'), ('GL', 'Golf'), ('GY', 'Gymnastics'), ('HK', 'Hockey')))])),
                ('analysis', models.CharField(max_length=2, choices=[('FD', 'Forward Dynamic'), ('ID', 'Inverse Dynamic'), ('KI', 'Kinematic'), ('ST', 'Static')])),
                ('contact', models.CharField(max_length=2, choices=[('CT', 'With Contact'), ('NC', 'Without Contact')])),
                ('flexibility', models.CharField(max_length=2, choices=[('FL', 'Flexible'), ('RI', 'Rigid')])),
                ('topology', models.CharField(max_length=2, choices=[('CL', 'Closed-loop'), ('OP', 'Open-loop')])),
            ],
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('number', models.IntegerField(default=0)),
                ('accuracy', models.FloatField()),
                ('cputime', models.FloatField()),
                ('cpu', models.CharField(max_length=64)),
                ('os', models.CharField(max_length=64)),
                ('method', models.CharField(max_length=1024)),
                ('results', models.FileField(upload_to=problems.models.get_solution_results_path)),
                ('miscellaneous', models.FileField(blank=True, upload_to=problems.models.get_solution_misc_path)),
                ('problem', models.ForeignKey(to='problems.Problem')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('signup_date', models.DateTimeField(verbose_name='date signup')),
                ('problems', models.IntegerField(default=0)),
                ('solutions', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='solution',
            name='user',
            field=models.ForeignKey(to='problems.User'),
        ),
        migrations.AddField(
            model_name='problem',
            name='user',
            field=models.ForeignKey(default=-1, to='problems.User'),
        ),
    ]
