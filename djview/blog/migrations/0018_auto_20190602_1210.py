# Generated by Django 2.2 on 2019-06-02 12:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20190602_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='helloworld',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2019, 6, 2, 12, 10, 31, 40692, tzinfo=utc)),
        ),
    ]