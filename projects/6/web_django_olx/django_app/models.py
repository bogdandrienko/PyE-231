from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class CategoryItem(models.Model):
    title = models.CharField(
        verbose_name="Наименование",
        db_index=True,
        primary_key=False,
        unique=True,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=300,
    )
    slug = models.SlugField(  # slug - строка, которая может использоваться как url
        verbose_name="Ссылка",
        db_index=True,
        primary_key=False,
        unique=True,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=300,
    )

    class Meta:
        app_label = "django_app"
        ordering = ("-title",)
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"<CategoryItem {self.title}({self.id}) = {self.slug} />"


class TagItem(models.Model):  # товар дня, распродажа, на доставке...
    title = models.CharField(
        verbose_name="Наименование",
        db_index=True,
        primary_key=False,
        unique=True,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=300,
    )
    slug = models.SlugField(
        verbose_name="Ссылка",
        db_index=True,
        primary_key=False,
        unique=True,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=300,
    )

    class Meta:
        app_label = "django_app"
        ordering = ("-title",)
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"

    def __str__(self):
        return f"<TagItem {self.title}({self.id}) = {self.slug} />"


class Item(models.Model):
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
    category = models.ForeignKey(
        verbose_name="Категория",
        db_index=True,
        primary_key=False,
        unique=False,  # !TODO OneToONe=True
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=100,
        #
        to=CategoryItem,
        on_delete=models.CASCADE,
    )
    tags = models.ManyToManyField(
        verbose_name="Тэги",
        db_index=True,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        default="",
        max_length=100,
        #
        to=TagItem,
    )
    is_active = models.BooleanField(
        verbose_name="Активеность объявления",
        null=False,
        default=True,
    )

    class Meta:
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


class Vip(models.Model):
    article = models.OneToOneField(
        verbose_name="Объявление",
        db_index=True,
        primary_key=False,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=100,
        #
        to=Item,
        on_delete=models.CASCADE,
    )
    priority = models.IntegerField(
        verbose_name="Приоритет",  # сколько заплатили
        db_index=True,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default=5,
    )
    expired = models.DateTimeField(
        verbose_name="дата и время истечения",
        db_index=True,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default=timezone.now,
        max_length=300,
    )

    class Meta:
        app_label = "django_app"
        ordering = ("priority", "-expired")
        verbose_name = "Vip объявление"
        verbose_name_plural = "Vip объявления"

    def __str__(self):
        return f"<Vip {self.article.title}({self.id}) | {self.priority}/>"


class CommentItem(models.Model):
    author = models.ForeignKey(
        verbose_name="Автор",
        db_index=True,
        primary_key=False,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=100,
        #
        to=User,
        on_delete=models.CASCADE,
    )
    article = models.ForeignKey(
        verbose_name="Объявление",
        db_index=True,
        primary_key=False,
        editable=True,
        unique=False,
        blank=True,
        null=False,
        default="",
        max_length=100,
        #
        to=Item,
        on_delete=models.CASCADE,
    )
    text = models.TextField(
        verbose_name="Текст комментария",
        db_index=False,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default="",
    )
    created = models.DateTimeField(
        verbose_name="дата и время создания",
        db_index=True,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default=timezone.now,
        max_length=300,
    )
    is_active = models.BooleanField(
        verbose_name="Активеность",
        null=False,
        default=True,
    )

    class Meta:
        app_label = "django_app"
        ordering = ("-created",)
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return f"<CommentItem {self.article.title}({self.id})/>"
