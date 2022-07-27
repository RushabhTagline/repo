# Generated by Django 4.0.5 on 2022-07-26 12:51

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0011_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='BlogId',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='blogapp.blogs'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 26, 12, 50, 56, 998269, tzinfo=utc), verbose_name='Date created'),
        ),
    ]