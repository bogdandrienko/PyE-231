from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

"""
Стратегии расширения модели пользователя:
Причина - недостаточно полей(столбцов), например аватар.

1. OOP - наследуемся от модели пользователя, перепределяем/добавляем свойства.
class UserExtend(User):
    avatar = models.ImageField()
    sex = models.BooleanField()
    def get_prefix(self):
        return ""
!TODO опасно, т.к. эта модель используется во всех сторонних библиотеках, есть риск всё сломать.

2. Proxy - промежуточная модель.
!TODO неудобно

3. Связь OneToOne - создание ещё одной таблицы и поле в ней, к таблице User с типом OneToOne.
Минус - ещё одна таблица.
"""


class Profile(models.Model):
    user = models.OneToOneField(
        verbose_name="Автор",
        db_index=True,
        primary_key=False,
        editable=True,
        blank=True,
        null=True,
        default=None,
        max_length=300,
        #
        to=User,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    #
    patronymic = models.CharField(
        verbose_name="Отчество",
        db_index=False,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="",
        max_length=300,
    )
    avatar = models.ImageField(
        verbose_name="Аватарка",
        validators=[FileExtensionValidator(["jpg", "png", "jpeg"])],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=None,
        upload_to="profile/avatars",
    )

    class Meta:
        app_label = "auth"
        ordering = ("-user",)

    def __str__(self):
        return f"<Profile {self.user.username} ({self.id})/>"

    def check_access(self, action_slug: str = ""):
        """
        Нам нужно проверить, имеет ли этот User доступ к этому Action.
        Проверить, есть ли группы с таким пользователей и таким действием.
        """
        try:
            user: User = self.user
            action: Action = Action.objects.get(slug=action_slug)
            intersections = GroupExtend.objects.filter(users=user, actions=action)
            if len(intersections) > 0:
                return True
            return False
        except Exception as error:
            print("error check_access: ", error)
            return False


@receiver(post_save, sender=User)
def profile_create(sender, instance: User, created: bool, **kwargs):
    # взять или создать
    profile = Profile.objects.get_or_create(user=instance)


class Action(models.Model):
    slug = models.SlugField(
        verbose_name="Ссылка",
        db_index=True,
        primary_key=False,
        unique=True,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=500,
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

    class Meta:
        app_label = "auth"
        ordering = ("slug",)
        verbose_name = "Действие"
        verbose_name_plural = "Действия"

    def __str__(self):
        return f"<Action {self.slug}({self.id}) = {self.description[:50]} />"


class GroupExtend(models.Model):
    name = models.CharField(
        verbose_name="Название группы",
        db_index=True,
        primary_key=False,
        unique=True,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=300,
    )
    users = models.ManyToManyField(
        verbose_name="Пользователи принадлежащие к группе",
        db_index=True,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        default="",
        max_length=300,
        to=User,
    )
    actions = models.ManyToManyField(
        verbose_name="Возможности доступные этой группе",
        db_index=True,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        default="",
        max_length=300,
        to=Action,
    )

    class Meta:
        app_label = "auth"
        ordering = ("name",)
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

    def __str__(self):
        return f"<Group {self.name}({self.id}) />"


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

    def count(self) -> int:
        """Этот метод возвращает количество товаров в своей категории"""

        # MVT - Model(сырые данные - чаще всего) - View(логика) - Template(внешний вид - только форматирование)
        # Паттерн - для адекватного разделения ответственности.
        # SOLID -
        _category = CategoryItem.objects.get(id=int(self.id))
        _items = Item.objects.filter(is_active=True, category=_category)
        return _items.count()


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
    author = models.ForeignKey(
        verbose_name="Автор",
        db_index=True,
        primary_key=False,
        editable=True,
        blank=True,
        null=False,
        default=None,
        max_length=100,
        #
        to=User,
        on_delete=models.CASCADE,
    )
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

    avatar = models.ImageField(
        verbose_name="Аватарка",
        validators=[FileExtensionValidator(["jpg", "png", "jpeg", "bmp"])],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=None,
        upload_to="item/avatars",
    )
    file = models.FileField(
        verbose_name="Инструкция",
        validators=[FileExtensionValidator(["xlsx", "docx", "pdf"])],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=None,
        upload_to="item/files",
    )

    is_active = models.BooleanField(
        verbose_name="Активеность объявления",
        null=False,
        default=True,
    )

    class Meta:
        app_label = "django_app"
        ordering = ("is_active", "title")
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        if self.is_active:
            act = "активен"
        else:
            act = "продано"
        return f"<Item {self.title}({self.id}) | {act} | {self.description[:30]} />"

    def comment_count(self) -> int:
        _article = Item.objects.get(id=self.id)
        _comments = CommentItem.objects.all().filter(article=_article, is_active=True)
        return _comments.count()

    def total_rating(self) -> int:
        _item = Item.objects.get(id=self.id)
        _ratings = ItemRating.objects.all().filter(item=_item)
        return _ratings.filter(is_like=True).count() - _ratings.filter(is_like=False).count()

    def is_my_rating_selection(self, user: User) -> int:
        _item = Item.objects.get(id=self.id)
        _ratings = ItemRating.objects.all().filter(item=_item)
        # пытаюсь найти "свою" отметку лайка, приходит пустой массив, если моей отметки нет
        _my_rating = _ratings.filter(author=user)
        if len(_my_rating) > 0:
            return 1 if _my_rating[0].is_like else -1
        else:
            return 0

    def get_all_comments(self):
        return CommentItem.objects.all().filter(is_active=True, article=self)

    def m_bugs_count(self) -> int:
        _bugs = ItemBug.objects.filter(item=self)
        return _bugs.count()


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


class ItemRating(models.Model):
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
    item = models.ForeignKey(
        verbose_name="Товар",
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
    is_like = models.BooleanField(
        verbose_name="Лайк или не лайк",
        db_index=True,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default=True,
    )

    class Meta:
        app_label = "django_app"
        ordering = ("-item", "-author")

    def __str__(self):
        return f"<ItemRating {self.item.title}({self.id}) | {self.is_like}/>"


class ItemBug(models.Model):
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
    item = models.ForeignKey(
        verbose_name="Товар",
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

    class Meta:
        app_label = "django_app"
        ordering = ("-item", "-author")

    def __str__(self):
        return f"<ItemBug {self.item.title}({self.id})/>"


class Room(models.Model):
    name = models.CharField(
        verbose_name="Наименование",
        db_index=True,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=255,
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
        ordering = ("-slug", "-name")

    def __str__(self):
        return f"<Room {self.name} {self.slug} ({self.id})/>"


class Message(models.Model):
    user = models.ForeignKey(
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
    room = models.ForeignKey(
        verbose_name="Комната",
        db_index=True,
        primary_key=False,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=100,
        #
        to=Room,
        on_delete=models.CASCADE,
    )
    content = models.TextField(
        verbose_name="Текст сообщения",
        db_index=False,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default="",
    )
    date_added = models.DateTimeField(
        verbose_name="дата и время добавления",
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
        ordering = ("-date_added", "-room")

    def __str__(self):
        return f"<Message {self.room.name} {self.user.username} {self.content[:30]} ({self.id})/>"
