# Generated by Django 4.1 on 2022-10-30 08:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bin_bank', '0003_alter_feedback_date_alter_transaction_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 30, 8, 19, 42, 242382, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 30, 8, 19, 42, 241380, tzinfo=datetime.timezone.utc)),
        ),
    ]