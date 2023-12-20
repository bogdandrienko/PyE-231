# Generated by Django 5.0 on 2023-12-20 14:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("django_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="profile",
            options={
                "ordering": ("-exp", "-iin"),
                "verbose_name": "Профиль",
                "verbose_name_plural": "Профили",
            },
        ),
        migrations.AddField(
            model_name="profile",
            name="exp",
            field=models.PositiveIntegerField(default=0, verbose_name="Опыт"),
        ),
        migrations.AlterField(
            model_name="profile",
            name="iin",
            field=models.CharField(
                blank=True,
                db_index=True,
                default=None,
                max_length=12,
                unique=True,
                validators=[
                    django.core.validators.MinLengthValidator(12),
                    django.core.validators.MaxLengthValidator(12),
                ],
                verbose_name="Номер регистрации",
            ),
        ),
    ]
