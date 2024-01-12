# Generated by Django 5.0 on 2024-01-12 13:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("django_app", "0010_itemrating"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ItemBug",
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
                    "author",
                    models.ForeignKey(
                        blank=True,
                        default="",
                        max_length=100,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор",
                    ),
                ),
                (
                    "item",
                    models.ForeignKey(
                        blank=True,
                        default="",
                        max_length=100,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="django_app.item",
                        verbose_name="Товар",
                    ),
                ),
            ],
            options={
                "ordering": ("-item", "-author"),
            },
        ),
    ]
