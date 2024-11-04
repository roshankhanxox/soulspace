# Generated by Django 5.0.7 on 2024-11-04 08:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="MoodLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(auto_now_add=True)),
                (
                    "mood_type",
                    models.CharField(
                        choices=[
                            ("happy", "Happy"),
                            ("sad", "Sad"),
                            ("anxious", "Anxious"),
                            ("calm", "Calm"),
                            ("excited", "Excited"),
                            ("angry", "Angry"),
                        ],
                        max_length=20,
                    ),
                ),
                ("intensity", models.PositiveIntegerField(default=1)),
                ("context", models.TextField(blank=True, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]