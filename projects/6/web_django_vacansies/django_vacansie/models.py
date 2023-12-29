from django.db import models


class Vacansie(models.Model):
    title = models.CharField(
        verbose_name="Наименование",
        db_index=True,
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
    salary = models.PositiveIntegerField(
        verbose_name="Зарплата",
        db_index=False,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default=0,
    )
    is_active = models.BooleanField(
        verbose_name="Активность вакансии",
        null=False,
        default=True,
    )

    class Meta:
        app_label = "django_app"
        ordering = ("is_active", "-salary", "-title")
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"

    def __str__(self):
        if self.is_active:
            act = "активен"
        else:
            act = "закрыта"
        return f"<Vacansie {self.title}({self.id}) | {act} | {self.salary} />"
