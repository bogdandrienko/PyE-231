from django.http import JsonResponse


def index(request):
    return JsonResponse(data={"message": "OK"})


def settings_get(request):
    if request.headers.get("Authorization", "") != "Token=auth123":
        return JsonResponse(data={"error": "Not valid token"}, status=401)
    _data = {
        "temp_plan_high": -13,
        "temp_plan_down": -33
    }
    return JsonResponse(data={"data": _data}, status=200)
