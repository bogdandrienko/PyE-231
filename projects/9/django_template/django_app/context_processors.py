from django.contrib.auth.models import User


def user_count(request):
    try:
        count = User.objects.filter(is_active=True).count()
    except Exception as _:
        count = 0
    return dict(user_count=count)
