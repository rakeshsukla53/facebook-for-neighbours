# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0014_auto_20151202_0258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='login_time',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='history',
            name='logout_time',
            field=models.DateTimeField(blank=True),
        ),
    ]
