from django.http import HttpResponse, JsonResponse


def index(request):
    return HttpResponse("Hello World")


def api(request):
    return JsonResponse(data={"message": "OK"}, safe=False)
