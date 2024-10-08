# Generated by Django 5.0.6 on 2024-08-18 11:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_p_receiver_remove_t_receiver_tr_howtocontact_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Uplift",
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
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.t_donor"
                    ),
                ),
            ],
        ),
    ]
