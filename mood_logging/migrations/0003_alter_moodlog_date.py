# Generated by Django 5.1.2 on 2024-11-04 22:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mood_logging", "0002_alter_moodlog_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="moodlog",
            name="date",
            field=models.DateField(default=datetime.date.today),
        ),
    ]