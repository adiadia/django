# Generated by Django 2.2 on 2019-06-02 09:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20190602_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='helloworld',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2019, 6, 2, 9, 9, 33, 684302, tzinfo=utc)),
        ),
    ]
