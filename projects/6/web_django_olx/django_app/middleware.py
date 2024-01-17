from django.http import HttpRequest


class CustomCorsMiddleware:
    """Отключает защиту Django от не валидных Origin/Headers"""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        response = self.get_response(request)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Headers"] = "*"

        # print(request.META)
        # request.

        with open("logs.txt", "a", encoding="utf-8") as f:
            f.write(f"{request.path}: {request.user.username}")
        return response
