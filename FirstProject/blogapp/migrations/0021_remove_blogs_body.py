# Generated by Django 4.0.5 on 2022-08-01 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0020_alter_users_otp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogs',
            name='body',
        ),
    ]