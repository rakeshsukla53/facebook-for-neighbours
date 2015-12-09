# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('bid', models.IntegerField(serialize=False, primary_key=True)),
                ('bname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Hood',
            fields=[
                ('hid', models.IntegerField(serialize=False, primary_key=True)),
                ('hname', models.CharField(max_length=100)),
                ('hcity', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='block',
            name='hid',
            field=models.ForeignKey(default=b'ABC', to='registration.Hood'),
        ),
    ]
