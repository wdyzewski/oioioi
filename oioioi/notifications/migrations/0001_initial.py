# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sessions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationsSession',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uid', models.CharField(unique=True, max_length=32)),
                ('session', models.OneToOneField(to='sessions.Session')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
