# Generated by Django 4.1 on 2022-10-12 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0005_alter_profile_cover_alter_profile_dp"),
    ]

    operations = [
        migrations.CreateModel(
            name="follow",
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
                ("follower", models.CharField(max_length=1000)),
                ("user", models.CharField(max_length=1000)),
            ],
        ),
    ]
