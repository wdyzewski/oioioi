# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0001_initial'),
        ('complaints', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaintsconfig',
            name='contest',
            field=models.OneToOneField(related_name='complaints_config', to='contests.Contest'),
            preserve_default=True,
        ),
    ]
