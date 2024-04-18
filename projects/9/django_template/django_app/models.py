from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from django.utils import timezone


class Position(models.Model):
    name = models.CharField(
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(300),
        ],
        unique=True,
        editable=True,
        blank=True,
        null=True,
        default="",
        verbose_name="Наименование должности",
        help_text='<small class="text-muted">CharField [1, 300]</small><hr><br>',
        max_length=300,
    )

    class Meta:
        app_label = "django_app"
        # ordering = ("name",)
        verbose_name = "Должность"
        verbose_name_plural = "Должности"
        # db_table = "django_app_post_model_table"

    def __str__(self):
        return f"{self.name}({self.id})"


class Contact(models.Model):
    """
    Основная таблица данных адресной книги
    """

    username = models.CharField(
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(300),
        ],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="",
        verbose_name="Имя контакта",
        help_text='<small class="text-muted">CharField [1, 300]</small><hr><br>',
        max_length=300,
    )
    position = models.ForeignKey(
        Position,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="",
        verbose_name="Должность",
        help_text='<small class="text-muted">ForeignKey [Position]</small><hr><br>',
        max_length=300,
        on_delete=models.SET_NULL,  # models.CASCADE - УДАЛЯЕТ
    )
    number = models.CharField(
        validators=[
            MinLengthValidator(9),
            MaxLengthValidator(300),
        ],
        unique=True,
        editable=True,
        blank=True,
        null=True,
        default="",
        verbose_name="Номер",
        help_text='<small class="text-muted">CharField [9, 300]</small><hr><br>',
        max_length=300,
    )
    description = models.TextField(
        validators=[
            MinLengthValidator(0),
            MaxLengthValidator(3000),
        ],
        editable=True,
        blank=True,
        null=True,
        default="",
        verbose_name="Описание контакта",
        help_text='<small class="text-muted">TextField [0, 3000]</small><hr><br>',
        max_length=3000,
    )
    is_completed = models.BooleanField(
        editable=True,
        blank=True,
        null=False,
        default=True,
        verbose_name="Активность",
        help_text='<small class="text-muted">BooleanField</small><hr><br>',
    )
    created = models.DateTimeField(
        editable=True,
        blank=True,
        null=True,
        default=timezone.now,
        verbose_name="Дата и время создания",
        help_text='<small class="text-muted">DateTimeField</small><hr><br>',
        auto_now=False,
        auto_now_add=False,
    )

    class Meta:
        app_label = "django_app"
        ordering = ("-is_completed", "username")
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
        # db_table = "django_app_post_model_table"

    def __str__(self):
        if self.is_completed:
            completed = "Активно"
        else:
            completed = "Неактивно"
        return f"{self.username}({self.id}) | {self.number}... | {completed}"
