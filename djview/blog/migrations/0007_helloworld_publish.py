# Generated by Django 2.2 on 2019-06-02 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190602_0530'),
    ]

    operations = [
        migrations.AddField(
            model_name='helloworld',
            name='publish',
            field=models.CharField(choices=[('draft', 'Draft'), ('private', 'Private'), ('public', 'Public')], default='draft', max_length=30),
        ),
    ]