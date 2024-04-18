# Generated by Django 5.0.4 on 2024-04-18 14:42

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("django_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                    "username",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text='<small class="text-muted">CharField [1, 300]</small><hr><br>',
                        max_length=300,
                        null=True,
                        validators=[
                            django.core.validators.MinLengthValidator(1),
                            django.core.validators.MaxLengthValidator(300),
                        ],
                        verbose_name="Имя контакта",
                    ),
                ),
                (
                    "number",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text='<small class="text-muted">CharField [9, 300]</small><hr><br>',
                        max_length=300,
                        null=True,
                        unique=True,
                        validators=[
                            django.core.validators.MinLengthValidator(9),
                            django.core.validators.MaxLengthValidator(300),
                        ],
                        verbose_name="Номер",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        default="",
                        help_text='<small class="text-muted">TextField [0, 3000]</small><hr><br>',
                        max_length=3000,
                        null=True,
                        validators=[
                            django.core.validators.MinLengthValidator(0),
                            django.core.validators.MaxLengthValidator(3000),
                        ],
                        verbose_name="Описание контакта",
                    ),
                ),
                (
                    "is_completed",
                    models.BooleanField(
                        blank=True,
                        default=True,
                        help_text='<small class="text-muted">BooleanField</small><hr><br>',
                        verbose_name="Активность",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        blank=True,
                        default=django.utils.timezone.now,
                        help_text='<small class="text-muted">DateTimeField</small><hr><br>',
                        null=True,
                        verbose_name="Дата и время создания",
                    ),
                ),
                (
                    "position",
                    models.ForeignKey(
                        blank=True,
                        default="",
                        help_text='<small class="text-muted">ForeignKey [Position]</small><hr><br>',
                        max_length=300,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="django_app.position",
                        validators=[
                            django.core.validators.MinLengthValidator(1),
                            django.core.validators.MaxLengthValidator(300),
                        ],
                        verbose_name="Должность",
                    ),
                ),
            ],
            options={
                "verbose_name": "Контакт",
                "verbose_name_plural": "Контакты",
                "ordering": ("-is_completed", "username"),
            },
        ),
    ]
