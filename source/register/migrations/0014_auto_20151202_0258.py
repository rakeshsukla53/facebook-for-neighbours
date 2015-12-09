# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0013_auto_20151202_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='uhood',
            field=models.CharField(default=b'Brooklyn', max_length=100),
        ),
    ]
