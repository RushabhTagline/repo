# Generated by Django 4.0.5 on 2022-07-27 03:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0012_comment_blogid_alter_comment_create_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 27, 3, 55, 25, 76520, tzinfo=utc), verbose_name='Date created'),
        ),
    ]
