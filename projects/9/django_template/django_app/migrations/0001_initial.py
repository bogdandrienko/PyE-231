# Generated by Django 5.0.4 on 2024-04-18 14:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Position",
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
                (
                    "name",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text='<small class="text-muted">CharField [1, 300]</small><hr><br>',
                        max_length=300,
                        null=True,
                        unique=True,
                        validators=[
                            django.core.validators.MinLengthValidator(1),
                            django.core.validators.MaxLengthValidator(300),
                        ],
                        verbose_name="Наименование должности",
                    ),
                ),
            ],
            options={
                "verbose_name": "Должность",
                "verbose_name_plural": "Должности",
            },
        ),
    ]
