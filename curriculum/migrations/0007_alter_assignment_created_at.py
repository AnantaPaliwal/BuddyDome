# Generated by Django 3.2.6 on 2021-10-08 09:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0006_auto_20211008_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 8, 9, 20, 47, 827019, tzinfo=utc)),
        ),
    ]