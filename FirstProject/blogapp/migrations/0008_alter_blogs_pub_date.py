# Generated by Django 4.0.5 on 2022-07-25 04:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0007_blogs_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='pub_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 7, 25, 4, 48, 39, 79182, tzinfo=utc)),
        ),
    ]
