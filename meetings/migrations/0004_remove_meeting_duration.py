# Generated by Django 3.0.8 on 2020-07-27 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0003_auto_20200727_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meeting',
            name='duration',
        ),
    ]
