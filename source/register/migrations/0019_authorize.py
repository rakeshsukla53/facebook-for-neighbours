# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0018_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authorize',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('auth_user', models.CommaSeparatedIntegerField(max_length=100)),
                ('author', models.ForeignKey(to='register.Registration')),
                ('hid', models.ForeignKey(to='register.Hood')),
                ('tid', models.ForeignKey(to='register.Thread')),
            ],
        ),
    ]
