# Generated by Django 2.2 on 2019-06-02 12:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20190602_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='helloworld',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2019, 6, 2, 12, 4, 5, 489345, tzinfo=utc)),
        ),
    ]
