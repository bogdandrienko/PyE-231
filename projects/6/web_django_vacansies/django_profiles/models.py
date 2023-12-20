from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models


class Profile(models.Model):  # таблица
    """
    Этот класс хранит сущность пользователя
    """

    # default (pk)
    # id = models.BigAutoField()  # serial

    # имя столбца(поле) = параметры(свойства поля)
    # models.Field - типы данных ORM
    iin = models.CharField(
        db_index=True,  # индексировать ли поле? (уникальность, участвует в фильтрах, поиске и сортировке)
        primary_key=False,  # первичный ключ
        validators=[  # массив валидаторов
            MinLengthValidator(12),
            MaxLengthValidator(12),
        ],
        unique=True,  # уникальность - может ли быть в таблице ещё такие значения
        editable=True,  # можно ли редактировать(через ORM и через django-admin)
        blank=True,  #
        null=False,  # может ли быть пустым
        default=None,  # стандартное значение (123, "12", timezone.now)
        verbose_name="Номер регистрации",  # псевдоним поля в админке
        #
        # только для CharField - varchar(50)
        max_length=12,  # максимальный оптимизированный размер
    )
    exp = models.PositiveIntegerField(
        verbose_name="Опыт",
        default=0,
    )
    name = models.CharField(
        db_index=False,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default="",
        verbose_name="Имя",
        max_length=200,
    )
    is_active = models.BooleanField(
        # True, False, None
        null=False,
        default=True,
        verbose_name="Активен ли профиль",
    )

    class Meta:
        app_label = "django_app"
        ordering = ("is_active", "-name")
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    def __str__(self):
        if self.is_active:
            act = "активен"
        else:
            act = "забанен"
        return f"<Profile {self.name} {self.iin}({self.id}) = {self.exp} |{act} />"
