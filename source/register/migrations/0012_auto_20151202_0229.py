# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0011_authblock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='uhid',
            field=models.ForeignKey(default=b'', to='register.Hood'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='uhood',
            field=models.CharField(default=b'', max_length=10),
        ),
    ]
