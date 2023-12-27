from django.db import models


class Item(models.Model):
    """Главная сущность веб-приложение - 'товар'"""

    # id
    title = models.CharField(
        verbose_name="Наименование",
        db_index=True,  # будет использоваться в поиске
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=300,
    )
    description = models.TextField(
        verbose_name="Описание",
        db_index=False,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default="",
    )
    price = models.PositiveIntegerField(
        verbose_name="Цена",
        db_index=False,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default="",
    )
    # Связи:
    # One2Many (ForeignKey)
    # Many2Many
    # One2One
    # joins: left/right/inner
    category = models.CharField(
        verbose_name="Категория",
        db_index=True,  # будет использоваться в фильтрации
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=100,
    )
    is_active = models.BooleanField(
        verbose_name="Активеность объявления",
        null=False,
        default=True,
    )

    class Meta:  # вспомогательный
        app_label = "django_app"
        ordering = ("is_active", "-title")
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        if self.is_active:
            act = "активен"
        else:
            act = "продано"
        return f"<Item {self.title}({self.id}) | {act} | {self.description[:30]} />"
