# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0009_auto_20151202_0135'),
    ]

    operations = [
        migrations.CreateModel(
            name='Neighbour',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hid', models.ForeignKey(to='register.Hood')),
                ('nuid1', models.ForeignKey(to='register.Registration')),
                ('nuid2', models.ForeignKey(related_name='+', to='register.Registration')),
            ],
        ),
    ]
