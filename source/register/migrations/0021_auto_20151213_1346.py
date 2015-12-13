# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0020_auto_20151213_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='tid',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
