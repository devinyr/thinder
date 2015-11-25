# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.TimeField(default=datetime.datetime(2015, 11, 25, 19, 10, 21, 659502, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
