# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0015_auto_20151202_0330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='login_time',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='history',
            name='logout_time',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
