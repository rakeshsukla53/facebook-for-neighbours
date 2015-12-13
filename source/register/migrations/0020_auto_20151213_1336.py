# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0019_authorize'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='tid',
            field=models.IntegerField(serialize=False, auto_created=True, primary_key=True),
        ),
    ]
