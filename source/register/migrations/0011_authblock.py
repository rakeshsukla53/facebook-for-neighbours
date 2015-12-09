# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0010_neighbour'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthBlock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uapproved', models.BooleanField(default=False)),
                ('total_request_required', models.IntegerField()),
                ('approval_received', models.IntegerField()),
                ('status', models.BooleanField(default=False)),
                ('bid', models.ForeignKey(related_name='+', to='register.Block')),
                ('uid', models.ForeignKey(to='register.Registration')),
            ],
        ),
    ]
