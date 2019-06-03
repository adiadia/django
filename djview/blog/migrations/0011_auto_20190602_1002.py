# Generated by Django 2.2 on 2019-06-02 10:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20190602_0909'),
    ]

    operations = [
        migrations.AddField(
            model_name='helloworld',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='helloworld',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2019, 6, 2, 10, 2, 45, 663291, tzinfo=utc)),
        ),
    ]