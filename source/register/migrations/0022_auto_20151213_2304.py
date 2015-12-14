# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0021_auto_20151213_1346'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='neighbour',
            unique_together=set([('nuid1', 'nuid2')]),
        ),
    ]
