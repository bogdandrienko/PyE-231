from django.contrib.auth.models import User
from django.http import HttpRequest


def get_user_count(request: HttpRequest) -> dict[str, any]:
    """
    Возвращает количество активных аккаунтов в веб-платформе.

    context_processors - контекстный процессор -
    функции, которые вызываются КАЖДЫЙ ВЫЗОВ render(...)
    """

    return {"user_count": User.objects.filter(is_active=True).count()}
