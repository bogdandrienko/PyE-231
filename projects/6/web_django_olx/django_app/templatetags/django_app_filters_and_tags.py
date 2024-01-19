from django import template
from django.contrib.auth.models import User
from django.http import HttpRequest

from django_app import models

register = template.Library()


@register.filter(name="custom_upper")  # filter - простая логика, вызываемая в django Jinja - шаблонизаторе
def custom_upper(text: any) -> str:
    return str(text).upper()


@register.filter(name="custom_cut")
def custom_cut(text: any, length: int) -> str:
    # django cut
    # return str(text)[:length]

    if len(str(text)) > length:
        return str(text)[:length] + "..."
    return str(text)


@register.simple_tag()
def digit_beautify(value: float):
    # -> 14135245245254
    # <- 14 135 245 245 254
    # <- 14 135 245 245 254.28

    src = str(value)
    # out, rnd = src.split(".")
    out, rnd = src, 0
    # TODO костыль
    if 3 < len(out) <= 6:  # 90 000
        out = out[0:3] + " " + out[3:]
    elif 6 < len(out) <= 9:  # 90 000 000
        out = out[6:] + " " + out[3:6] + " " + out[0:3]
    elif 9 < len(out) <= 12:  # 90 000 000 000
        out = out[9:] + " " + out[6:9] + " " + out[3:6] + " " + out[0:3]
    elif 12 < len(out) <= 15:
        out = out[12:] + " " + out[9:12] + " " + out[6:9] + " " + out[3:6] + " " + out[0:3]
    return f"{out},{rnd}"  # out = out.replace(".", ",")  # TODO русификация разрядов


@register.simple_tag(takes_context=True)
def item_rating(context: dict, item_id: str) -> int:  # simple_tag - сложная логика, вызываемая в django Jinja - шаблонизаторе
    # request: HttpRequest = context["request"]
    _item = models.Item.objects.get(id=int(item_id))
    _ratings = models.ItemRating.objects.all().filter(item=_item)
    return _ratings.filter(is_like=True).count() - _ratings.filter(is_like=False).count()


@register.simple_tag(takes_context=True)
def check_is_my_comment(context: str, comment_id: str) -> bool:
    """Проверяет, является ли текущий пользователь автором Товара"""

    try:
        user: User = context["request"].user
        _comment = models.CommentItem.objects.get(id=int(comment_id))

        if user.username == _comment.author.username:
            return True
        return False
    except Exception as _:
        return False


@register.simple_tag(takes_context=True)
def check_user_access(context: str, groups: str = "") -> bool:
    try:
        user: User = context["request"].user
        group_objs = user.groups.all()
        group_strs = [str(x.name).lower().strip() for x in group_objs]
        if str(groups).lower().strip() in group_strs:
            return True
        return False
    except Exception as error:
        print("error simple_tag check_user_access: ", error)
        return False


@register.simple_tag(takes_context=True)
def t_bugs_count(context: dict, item_id: str) -> int:
    # request: HttpRequest = context["request"]
    _item = models.Item.objects.get(id=int(item_id))
    _bugs = models.ItemBug.objects.filter(item=_item)
    return _bugs.count()


@register.simple_tag(takes_context=True)
def check_access(context: dict, action_slug: str = "") -> bool:
    user: User = context["request"].user
    if not user.is_authenticated:
        return False
    profile: models.Profile = user.profile
    is_access: bool = profile.check_access(action_slug)
    return is_access
