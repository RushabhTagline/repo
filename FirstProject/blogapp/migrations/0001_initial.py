# Generated by Django 4.0.5 on 2022-07-20 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=250)),
                ('LastName', models.CharField(max_length=250)),
                ('UserMail', models.EmailField(max_length=100)),
                ('Password', models.CharField(max_length=15)),
                ('ConfirmPassword', models.CharField(max_length=15)),
            ],
        ),
    ]
