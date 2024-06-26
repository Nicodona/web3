# Generated by Django 5.0.6 on 2024-06-08 22:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Candidates",
            fields=[
                (
                    "color",
                    models.CharField(max_length=12, primary_key=True, serialize=False),
                ),
                ("candidate_name", models.CharField(max_length=20)),
                ("votes", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Registration",
            fields=[
                (
                    "figerprint",
                    models.CharField(max_length=256, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=20)),
                ("center", models.CharField(max_length=40)),
                ("Nid", models.IntegerField()),
                ("Rid", models.CharField(blank=True, max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Poll",
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
                ("poll_harsh", models.CharField(max_length=256)),
                (
                    "choice",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="poll.candidates",
                    ),
                ),
                (
                    "voter",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="poll.registration",
                    ),
                ),
            ],
        ),
    ]
